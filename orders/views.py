from django.shortcuts import render, redirect
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from orders.models import Order
from cart.models import Cart as CM
import datetime

import time

from iamporter import Iamporter

from orders.tasks import order_created


def generate_order_number():

    last_order_default = '000000'

    try:
        last_order = Order.objects.all().order_by('id').last()
        print("last_order : " ,last_order)
    except:
        print("last_order does not exist.")

    dt = datetime.datetime.now()
    gen_code = 'me' + str(dt.year)\
               +'{:02d}'.format(dt.month)\
               +'{:02d}'.format(dt.day)

    if not last_order:
        return gen_code + last_order_default

    #생성된 Order항목이 존재하므로 exception 발생 안할 듯
    order_no = last_order.id + 1
    new_order_no = gen_code + '{:06d}'.format(order_no)

    return new_order_no

@login_required(login_url="accounts:login")
def order_create(request):
    cart = Cart(request)
    totalCost = cart.get_total_cost()
    order_no = generate_order_number()
    user = auth.get_user(request)
    user_profile = UserProfile.objects.get(user=user)
    dbCart = CM.objects.filter(user=user)

    print(order_no)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print("form was executed as the way of POST")
        if form.is_valid():
            order = form.save(commit=False)

            client = Iamporter(imp_key="1286359584086938",
                               imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

            time.sleep(0.3)


            order.user = user
            order.order_no = order_no
            imp_uid = request.POST.get('imp_uid')
            print('imp_uid : ', imp_uid)
            order.imp_uid = imp_uid

            payment = client.find_payment(merchant_uid=order.order_no)

            order.paid = payment['status']

            def delivery_decide(x):
                return {
                    '001': 2500, #일반배송
                    '002': 5000, #도서산간
                    '003': 0, #착불
                    '004': 0, #직접찾기
                    '005': 0, #기타
                }.get(x, 2500)

            charge = delivery_decide(order.delivery_fee)
            print('배송료 : ' + str(charge))
            order.totalCost = totalCost + charge
            print('최종금액 : ' + str(order.totalCost))


            infoSave = request.POST.get('infoSave')
            if infoSave:
                user = user
                user_profile = user_profile
                user_profile.phone = form.cleaned_data.get('phone')
                user_profile.postal_code = form.cleaned_data.get('postal_code')
                user_profile.address = form.cleaned_data.get('address')
                user_profile.extraAddress = form.cleaned_data.get('extraAddress')
                user_profile.detailAddress = form.cleaned_data.get('detailAddress')
                user_profile.save()

            order.save()

            #order item 생성과정
            for item in cart:
                OrderItem.objects.create(order=order,
                                         content=item['content'],
                                         cost=item['cost'],
                                         quantity=item['quantity'])

            # launch asynchronous task
            order_created.delay(order.id)

            # clear the cart
            cart.clear()
            print("session cart is cleared")
            dbCart.delete()
            print("database cart is cleared")

            return redirect('accounts:order_status')
    else:


        form = OrderCreateForm(initial={
            'order_no':order_no,
            'name':user.first_name,
            'email':user.email,
            'phone':user_profile.phone,
            'postal_code':user_profile.postal_code,
            'address':user_profile.address,
            'extraAddress':user_profile.extraAddress,
            'detailAddress':user_profile.detailAddress,
        })

    return render(request,
                  'orders/order_created.html',
                  {
                      'cart': cart,
                      'order_no': order_no,
                      'name': user.first_name,
                      'phone': user_profile.phone,
                      'postal_code': user_profile.postal_code,
                      'address': user_profile.address,
                      'extraAddress': user_profile.extraAddress,
                      'detailAddress': user_profile.detailAddress,
                      'totalCost': totalCost,
                      'form': form,
                      'username':user.first_name
                  })
