from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Content
from django.contrib.auth.models import User
from django.contrib import auth
from cart.cart import Cart
from cart.forms import CartAddContentForm
from cart.models import Cart as CM

from django.forms import formset_factory
import json
from pprint import pprint

from decimal import *

@require_POST
def cart_add(request, content_id):
    cart = Cart(request)
    content = get_object_or_404(Content, id=content_id)

    form = CartAddContentForm(request.POST)
    print("cart_add 실행")
    quantity=0
    ######## cart_detail.html에서 실행된 form의 validity검증######
    if form.is_valid():
        quantity = form.cleaned_data.get('quantity')
        update = form.cleaned_data.get('update')
        print("form is valid")
        print(quantity, update)
    ##########################################################

    ############## 사용자가 로그인 된 경우 DB와 session cart를 동기화 시켜준다.################
    if auth.get_user(request).is_authenticated:
        print("카트에서 로그인된 계정 확인")
        user = auth.get_user(request)
        try:
            ####해당 카트의 내용의 있는지 확인한다.###########
            userCart = get_object_or_404(CM, user=user, content=content)
            print("카트DB에 있는 데이터")
            ##########################################

            #############cart_detail.html에서 update를 한 항목인지 확인##################
            ######업데이트 여부에 따라 추가할 지 아니면 그 값을 그냥 넣을지 결정#################
            if update:
                userCart.quantity = quantity
            else:
                userCart.quantity += quantity
            ########################################################################


        except:
            print("카트DB에 없는 데이터")
            userCart = CM.objects.create(user=user, content=content)
            userCart.quantity = quantity
            if content.isDiscount:
                userCart.cost = content.discount
            else:
                userCart.cost = content.cost

        ####session cart에도 동일하게 적용한다.######################################
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                content=content,
                quantity=userCart.quantity,
                update_quantity=cd['update']
            )
        ########################################################################
        ###########최종적으로 cart db에 반영한다.####################################
        userCart.save()
        ########################################################################

    else:
        ##############로그인이 안된경우 그냥 cart session에만 적용한다.#################
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                content=content,
                quantity=cd['quantity'],
                update_quantity=cd['update']
            )
        ########################################################################

    return redirect('cart:cart_detail')

def cart_remove(request, content_id):

    cart = Cart(request)
    content = get_object_or_404(Content, id=content_id)

    ############## 사용자가 로그인 된 경우 DB와 session cart를 동기화 시켜준다.################
    if auth.get_user(request).is_authenticated:
        print("카트에서 로그인된 계정 확인")
        user = auth.get_user(request)
        try:
            ####해당 카트의 내용의 있는지 확인한다.###########
            userCart = get_object_or_404(CM, user=user, content=content)
            print("카트DB에 있는 데이터")
            ##########################################

            ##삭제##
            userCart.delete()

        except:
            print("session cart와 Cart DB 동기화 오류")

    ###cart session 데이터 삭제 과정####################
    cart.remove(content)
    ################################################
    return redirect('cart:cart_detail')

def cart_detail(request):

    cart = Cart(request)

    pprint(cart)
    for item in cart:
        item['update_quantity_form'] = CartAddContentForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    return render(request, 'cart/cart_detail.html',
                  {
                      'cart': cart,
                      'prev_page': request.META.get('HTTP_REFERER'),
                  })

    



