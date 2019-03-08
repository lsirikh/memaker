from django.shortcuts import render
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


def generate_order_number():
    try:
        last_order = Order.objects.all().order_by('id').last()
    except:
        last_order = 000

    dt = datetime.datetime.now()
    gen_code = 'me' + str(dt.year)\
               +'{:02d}'.format(dt.month)\
               +'{:02d}'.format(dt.day)

    if not last_order:
        return gen_code + '0'
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
    user_profile = UserProfile.objects.get(user__username=user)
    dbCart = CM.objects.filter(user=user)

    print(order_no)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print("form was executed as the way of POST")
        if form.is_valid():
            order = form.save(commit=False)
            order.order_no = order_no
            order.totalCost = totalCost


            infoSave = request.POST.get('infoSave')
            if infoSave:
                user = auth.get_user(request)
                #user.first_name = request.POST.get('name')
                user_profile = UserProfile.objects.get(user__username=user)
                user_profile.phone = form.cleaned_data.get('phone')
                user_profile.postal_code = form.cleaned_data.get('postal_code')
                user_profile.address = form.cleaned_data.get('address')
                user_profile.extraAddress = form.cleaned_data.get('extraAddress')
                user_profile.detailAddress = form.cleaned_data.get('detailAddress')
                user_profile.save()

            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         content=item['content'],
                                         cost=item['cost'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            print("session cart is cleared")
            dbCart.delete()
            print("database cart is cleared")

            return render(request,
                          'orders/order_created.html',
                          {
                              'order': order,
                              'username': user.first_name,
                           })
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
