from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url="accounts:login")
def order_create(request):
    cart = Cart(request)
    totalCost = cart.get_total_cost()
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print("form was executed as the way of POST")
        if form.is_valid():

            order = form.save(commit=False)
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
            return render(request,
                          'orders/order_created.html',
                          {'order': order})
    else:

        user = auth.get_user(request)
        user_profile = UserProfile.objects.get(user__username=user)
        form = OrderCreateForm(initial={
            'name':user.first_name,
            'phone':user_profile.phone,
            'postal_code':user_profile.postal_code,
            'address':user_profile.address,
            'extraAddress':user_profile.extraAddress,
            'detailAddress':user_profile.detailAddress,
        })

    return render(request,
                  'orders/order_created.html',
                  {'cart': cart, 'form': form})
