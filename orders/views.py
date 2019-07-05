from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from orders.models import OrderItem, OrderCancel, OrderDelivery, ImportInfo
from orders.forms import OrderCreateForm, OrderCancelForm
from cart.cart import Cart
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from orders.models import Order
from cart.models import Cart as CM
import datetime
import json
import time
import datetime
from iamporter import Iamporter

from accounts.tasks import order_notified
from orders.tasks import order_created, order_canceled
from products.models import Content


def generate_order_number():


    dt = datetime.datetime.now()
    gen_code = 'me' + str(dt.year)\
               +'{:02d}'.format(dt.month)\
               +'{:02d}'.format(dt.day)\
               +'{:02d}'.format(dt.hour)\
               +'{:02d}'.format(dt.minute)\
               +'{:02d}'.format(dt.second)


    #생성된 Order항목이 존재하므로 exception 발생 안할 듯
    new_merchant_uid = gen_code
    print('generate_order_number() : {}'.format(new_merchant_uid))

    return new_merchant_uid


@login_required(login_url="accounts:login")
def order_create_mobile(request):

    print('order_create_mobile')
    success=request.GET.get('success')
    imp_uid=request.GET.get('imp_uid')
    merchant_uid=request.GET.get('merchant_uid')

    client = Iamporter(imp_key="1286359584086938",
                       imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

    payment = client.find_payment(imp_uid=imp_uid,merchant_uid=merchant_uid)

    context = {
        'payment': payment,
    }

    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required(login_url="accounts:login")
def order_payment_confirm(request):
    # 결제 성공 결과 GET 확인
    # 성공과 실패에 따라서 다른 프로세스
        # 성공
        # merchant_uid, imp_uid GET 확인
        # Import 인스턴스 생성후, 결과 find
        # ImportInfo에 데이터 입력
        # 메일 발송
        # isDirect에 따른 구분
            # 참
                # 확인
            # 거짓
                # # clear the cart
                # cart.clear()
                # print("session cart is cleared")
                # dbCart.delete()
                # print("database cart is cleared")

        # 실패
        # merchant_uid GET 확인
        # Order 쿼리 찾기
        # 해당 쿼리 삭제(보류)

    print('order_payment_confirm')
    # 유저의 정보를 retrieve한다.
    user = auth.get_user(request)

    client = Iamporter(imp_key="1286359584086938",
                       imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

    success=''
    imp_uid=''
    merchant_uid=''

    if request.method == 'POST':
        success = request.POST.get('success')
        if success == 'true' or success == 'True':
            success = True
        else:
            success = False
        print('success:{}'.format(success))

        imp_uid = request.POST.get('imp_uid')
        merchant_uid = request.POST.get('merchant_uid')
    else:
        success = request.GET.get('imp_success')
        if success == 'true' or success == 'True':
            success = True
        else:
            success = False
        print('success:{}'.format(success))

        imp_uid = request.GET.get('imp_uid')
        merchant_uid = request.GET.get('merchant_uid')


    print('imp_uid : {}, merchant_uid : {}'.format(imp_uid, merchant_uid))

    # 아임포트 API로 구매 정보 들고오기
    payment = client.find_payment(merchant_uid=merchant_uid, imp_uid=imp_uid)
    paid = payment['status']
    print('결제상태 : {}'.format(paid))

    try:
        print("payment['tex_free'] : {}".format(payment['tex_free']))
    except:
        print("payment['tex_free'] Non existence Error 발생")
        pass

    order = ''
    importInfo = ''

    print('order 쿼리 호출')
    try:
        order = Order.objects.get(merchant_uid=merchant_uid)
        order.imp_uid = imp_uid
        importInfo = order.importInfo
    except:
        print("order 쿼리 호출 실패")

    print('importInfo 데이터 입력')
    ##########################################ImportInfo 데이터 입력##########################################
    importInfo.amount = payment['amount']
    importInfo.apply_num = payment['apply_num']
    importInfo.bank_code = payment['bank_code']
    importInfo.bank_name = payment['bank_name']
    importInfo.buyer_addr = payment['buyer_addr']
    importInfo.buyer_email = payment['buyer_email']
    importInfo.buyer_name = payment['buyer_name']
    importInfo.buyer_postcode = payment['buyer_postcode']
    importInfo.buyer_tel = payment['buyer_tel']
    importInfo.cancel_amount = payment['cancel_amount']
    importInfo.cancel_history = payment['cancel_history']
    importInfo.cancel_reason = payment['cancel_reason']
    importInfo.cancel_receipt_urls = payment['cancel_receipt_urls']
    importInfo.cancelled_at = payment['cancelled_at'] \
        if payment['cancelled_at'] == 0 \
        else datetime.datetime.fromtimestamp(payment['cancelled_at'])
    importInfo.card_code = payment['card_code']
    importInfo.card_name = payment['card_name']
    importInfo.card_quota = payment['card_quota']
    importInfo.cash_receipt_issued = payment['cash_receipt_issued']
    importInfo.channel = payment['channel']
    importInfo.currency = payment['currency']
    importInfo.custom_data = payment['custom_data']
    importInfo.escrow = payment['escrow']
    importInfo.fail_reason = payment['fail_reason']
    importInfo.failed_at = payment['failed_at'] \
        if payment['failed_at'] == 0 \
        else datetime.datetime.fromtimestamp(payment['failed_at'])
    importInfo.imp_uid = payment['imp_uid']
    importInfo.merchant_uid = payment['merchant_uid']
    importInfo.name = payment['name']
    importInfo.paid_at = payment['paid_at'] \
        if payment['paid_at'] == 0 \
        else datetime.datetime.fromtimestamp(payment['paid_at'])
    importInfo.pay_method = payment['pay_method']
    importInfo.pg_id = payment['pg_id']
    importInfo.pg_provider = payment['pg_provider']
    importInfo.pg_tid = payment['pg_tid']
    importInfo.receipt_url = payment['receipt_url']
    importInfo.status = payment['status']
    importInfo.user_agent = payment['user_agent']
    importInfo.vbank_code = payment['vbank_code']
    importInfo.vbank_date = payment['vbank_date'] \
        if payment['vbank_date'] == 0 \
        else datetime.datetime.fromtimestamp(payment['vbank_date'])
    importInfo.vbank_holder = payment['vbank_holder']
    importInfo.vbank_issued_at = payment['vbank_issued_at'] \
        if payment['vbank_issued_at'] == 0 \
        else datetime.datetime.fromtimestamp(payment['vbank_issued_at'])
    importInfo.vbank_name = payment['vbank_name']
    importInfo.vbank_num = payment['vbank_num']
    ######################################################################################################

    print('order 및 importInfo 내용 DB 저장')
    order.save()
    importInfo.save()

    if success:
        #결제상태가 성공이면 order.result에 Boolean Field를 True로 잡아준다.
        order.result = True
        order.save()

        #결제가 성공하였고, 결제 상태가 완료이면, 메일을 보낸다.
        #보통 카드나 실시간 계좌 이체에 경우 해당할 듯하다.
        if importInfo.status == 'paid':
            ############## launch asynchronous task(이메일)#################
            order_created.delay(order.id)
            order_notified.delay(order.id)

        print('order.isDirect:{}'.format(order.isDirect))

        if not order.isDirect:
            # 직접 구매로 진행하는 경우가 아니면, 카트로 구매를 진행하는 경우이다.
            ########################################################
            # 카트 세션의 정보와 dbCart의 정보를 retrieve한다.
            cart = Cart(request)
            dbCart = CM.objects.filter(user=user)

            # clear the cart
            cart.clear()
            print("session cart is cleared")
            dbCart.delete()
            print("database cart is cleared")
            ########################################################

    # else:
    #     # merchant_uid = request.POST.get('merchant_uid')
    #     # imp_uid = request.POST.get('imp_uid')
    #     # 결제 실패를 쿼리에서 삭제하지 말자
    #     # print('order 쿼리 호출')
    #     # try:
    #     #     order = Order.objects.get(merchant_uid=merchant_uid)
    #     #     order.delete()
    #     #     print("결제 실패로 Order 데이터 삭제")
    #     # except:
    #     #     print("order 쿼리 호출 실패")
    #     #success = False


    context = {
        'merchant_uid': merchant_uid,
        'imp_uid': imp_uid,
        'success': success,
    }
    if request.method == 'POST':
        #그냥 PC에서 진행이 되는 것이라고 가정하면 됨.
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        #GET 방식으로 들어오는 정보는 모바일로 결제를 진행하는 경우라고 봐야함
        #따라서 성공과 실패에 따른 redirection을 고려해야함
        if order.result:
            return redirect('accounts:order_status')
        else:
            if order.isDirect:
                content=order.orderItem.first().content
                quantity=order.orderItem.first().quantity
                return redirect('orders:order_one_create', pk=content.pk, quantity=quantity)
            else:
                return redirect('orders:order_create')



@login_required(login_url="accounts:login")
def order_initial_processing(request):
    print('order_initial_processing')

    #유저의 정보를 retrieve한다.
    user = auth.get_user(request)
    user_profile = UserProfile.objects.get(user=user)

    # 제품 비용 계산
    totalCost = 0

    # 면세 제품 비용 계산 변수
    tex_free_cost = 0

    isDirect = request.POST.get('isDirect')
    if isDirect == 'True' or isDirect == 'true':
        isDirect = True
    else:
        isDirect = False

    print('isDirect : {}'.format(isDirect))


    #isDirect에 따라서 Cart방식으로 저장할지 Direct방식으로 저장할지 결정.
    if isDirect:
        print('isDirect is True')
        ########################################################
        pk = request.POST.get('pk')
        quantity = int(request.POST.get('quantity'))

        # Content모델을 들고와서 처리한다.
        content = get_object_or_404(Content, pk=pk)

        print('pk:{}({}), quantity:{}'.format(content.title, pk, quantity))

        # 면세 제품의 정보를 확인한다.
        if content.category.title == '교재':
            tex_free_cost = content.cost * quantity

        print("면제 제품 비용 : {}원".format(tex_free_cost))

        # 결제비용의 총액을 계산
        if content.isDiscount:
            totalCost = content.discount * quantity
        else:
            totalCost = content.cost * quantity
        ########################################################
    else:
        ########################################################
        # 카트 세션의 정보와 dbCart의 정보를 retrieve한다.
        cart = Cart(request)
        dbCart = CM.objects.filter(user=user)

        # 면세 제품의 정보를 확인한다.
        for newItem in dbCart:
            if newItem.content.category.title == '교재':
                tex_free_cost += newItem.cost * newItem.quantity
        # 결제비용의 총액을 계산
        totalCost = cart.get_total_cost()

        ########################################################



    print("총 제품 비용 : {}원".format(totalCost))

    #context데이터 미리 설정
    success = False
    merchant_uid = ''

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print("form was executed as the way of POST")

        #merchant_uid를 통해서 결제 유효성 확인
        #1. Order DB에 imp_uid가 0인(즉, 결제가 올바르게 진행되지 않은) 데이터가 있는지 확인하고 있다면, 삭제
        #2. 결제창이 의도대로 작동하지 않아 imp_uid를 부여받고 결제 결과를 알지 못하는 경우
        ####2-1. 그 상태에서 제 결제 시도를 할 경우 : 기존의 Order DB를 삭제하고 다시 진행
        ####2-2. 그 상태로 다른 페이지 리다이렉션을 할 경우 : Celery를 활용하여 1일 1회 삭제 작업해주기(보류)

        merchant_uid = request.POST.get('merchant_uid')
        print('merchant_uid : ', merchant_uid)

        #1. Order DB에 imp_uid가 0인(즉, 결제가 올바르게 진행되지 않은) 데이터가 있는지 확인하고 있다면, 삭제
        try:
            #imp_uid가 0인 Order DB의 정보를 list로 만들고 하나씩 삭제 진행
            order_list=user.order.filter(imp_uid='0')
            for order in order_list:
                print('오류: imp_uid가 0인 Order DB({})의 내용이 발견되어 삭제합니다.'.format(order))
                order.delete()

        except :
            print('통과: imp_uid가 0인 Order DB의 내용이 없습니다.'.format(merchant_uid))

        # 2. 결제창이 의도대로 작동하지 않아 imp_uid를 부여받고 결제 결과를 알지 못하는 경우
        ####2-1. 그 상태에서 제 결제 시도를 할 경우 : 기존의 Order DB를 삭제하고 다시 진행
        ####2-2. 그 상태로 다른 페이지 리다이렉션을 할 경우 : Celery를 활용하여 1일 1회 삭제 작업해주기(보류)
        try:
            #동일한 merchant_uid가 있고, imp_uid가 0이면 삭제 진행
            order=Order.objects.get(merchant_uid=merchant_uid)
            if order.imp_uid=='0' or order.imp_uid==0:
                print('실패:Order DB에 등록된 merchant_uid({})입니다.'.format(merchant_uid))
                order.delete()
        except Order.DoesNotExist:
            print('성공:Order DB에 등록되지 않은 merchant_uid({})입니다.'.format(merchant_uid))



        if form.is_valid():
            #form data 가져오기
            method=form.cleaned_data.get('method')
            delivery_fee=form.cleaned_data.get('delivery_fee')# OrderDelivery에 사용
            note=form.cleaned_data.get('note')# OrderDelivery에 사용
            name=form.cleaned_data.get('name') #user_profile에 사용, OrderDelivery에 사용
            email=form.cleaned_data.get('email')# OrderDelivery에 사용
            phone=form.cleaned_data.get('phone') #user_profile에 사용, OrderDelivery에 사용
            postal_code=form.cleaned_data.get('postal_code') #user_profile에 사용, OrderDelivery에 사용
            address=form.cleaned_data.get('address') #user_profile에 사용, OrderDelivery에 사용
            extraAddress=form.cleaned_data.get('extraAddress') #user_profile에 사용, OrderDelivery에 사용
            detailAddress=form.cleaned_data.get('detailAddress') #user_profile에 사용, OrderDelivery에 사용
            infoSave=form.cleaned_data.get('infoSave') #user_profile에 사용


            def delivery_decide(x):
                return {
                    '001': 2500, #일반배송
                    '002': 5000, #도서산간
                    '003': 0, #착불
                    '004': 0, #직접찾기
                    '005': 0, #기타
                }.get(x, 2500)

            charge = delivery_decide(delivery_fee)
            print('배송료 : ' + str(charge))
            totalCost = totalCost + charge
            tex_free_cost = tex_free_cost
            print('최종금액 : ' + str(totalCost))



            if infoSave:
                user.first_name = name
                user_profile.phone = phone
                user_profile.postal_code = postal_code
                user_profile.address = address
                user_profile.extraAddress = extraAddress
                user_profile.detailAddress = detailAddress
                user.save()
                user_profile.save()

            ################################Order 생성#############################
            try:
                order = Order.objects.create(user=user,
                                             merchant_uid=merchant_uid,
                                             # imp_uid=imp_uid,
                                             totalCost=totalCost,
                                             tex_free_cost=tex_free_cost,
                                             isDirect=isDirect,
                                             )
            except:
                print('Order 모델 생성 오류')

            ################################ImportInfo 생성#############################
            try:
                importInfo = ImportInfo.objects.create(
                    order = order,
                    # amount = payment['amount'],
                    # apply_num = payment['apply_num'],
                    # bank_code = payment['bank_code'],
                    # bank_name = payment['bank_name'],
                    # buyer_addr = payment['buyer_addr'],
                    # buyer_email = payment['buyer_email'],
                    # buyer_name = payment['buyer_name'],
                    # buyer_postcode = payment['buyer_postcode'],
                    # buyer_tel = payment['buyer_tel'],
                    # cancel_amount = payment['cancel_amount'],
                    # cancel_history = payment['cancel_history'],
                    # cancel_reason = payment['cancel_reason'],
                    # cancel_receipt_urls = payment['cancel_receipt_urls'],
                    # cancelled_at = payment['cancelled_at'] if payment['cancelled_at'] == 0 else datetime.datetime.fromtimestamp(payment['cancelled_at']),
                    # card_code = payment['card_code'],
                    # card_name = payment['card_name'],
                    # card_quota = payment['card_quota'],
                    # cash_receipt_issued = payment['cash_receipt_issued'],
                    # channel = payment['channel'],
                    # currency = payment['currency'],
                    # custom_data = payment['custom_data'],
                    # escrow = payment['escrow'],
                    # fail_reason = payment['fail_reason'],
                    # failed_at = payment['failed_at'] if payment['failed_at']==0 else datetime.datetime.fromtimestamp(payment['failed_at']),
                    # imp_uid = payment['imp_uid'],
                    # merchant_uid = payment['merchant_uid'],
                    # name = payment['name'],
                    # paid_at = payment['paid_at'] if payment['paid_at']==0 else datetime.datetime.fromtimestamp(payment['paid_at']),
                    # pay_method = payment['pay_method'],
                    # pg_id = payment['pg_id'],
                    # pg_provider = payment['pg_provider'],
                    # pg_tid = payment['pg_tid'],
                    # receipt_url = payment['receipt_url'],
                    # status = payment['status'],
                    # user_agent = payment['user_agent'],
                    # vbank_code = payment['vbank_code'],
                    # vbank_date = payment['vbank_date'] if payment['vbank_date']==0 else datetime.datetime.fromtimestamp(payment['vbank_date']),
                    # vbank_holder = payment['vbank_holder'],
                    # vbank_issued_at = payment['vbank_issued_at'] if payment['vbank_issued_at']==0 else datetime.datetime.fromtimestamp(payment['vbank_issued_at']),
                    # vbank_name = payment['vbank_name'],
                    # vbank_num = payment['vbank_num'],
                )
            except:
                print('ImportInfo 모델 생성 오류')

            ################################OrderDelivery 생성##########################
            try:
                OrderDelivery.objects.create(
                    order=order,
                    delivery_fee=delivery_fee,
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    detailAddress=detailAddress,
                    extraAddress=extraAddress,
                    postal_code=postal_code,
                    delivery_note=note

                )
            except:
                print('OrderDelivery 모델 생성 오류')


            if isDirect:
                ###############################OrderItem 생성################################

                newItem=OrderItem.objects.create(order=order,
                                                 content=content,
                                                 cost=content.discount if content.isDiscount else content.cost,
                                                 quantity=quantity)
                ############################################################################
            else:
                ###############################OrderItem 생성################################
                for item in cart:
                    newItem = OrderItem.objects.create(order=order,
                                                       content=item['content'],
                                                       cost=item['cost'],
                                                       quantity=item['quantity'])
                    if newItem.content.category == '교재':
                        tex_free_cost += newItem.cost
                        print("면제 제품 비용 : {}원".format(tex_free_cost))

                ############################################################################


            success = True

            context={
                'merchant_uid' : merchant_uid,
                'success' : success,
            }

    else:

        context = {
            'merchant_uid': merchant_uid,
            'success': success,
        }


    return HttpResponse(json.dumps(context), content_type="application/json")



@login_required(login_url="accounts:login")
def order_one_create(request, pk, quantity):
    print('order_one_create')
    #merchant_uid로 활용할 정보를 생성한다.
    merchant_uid = generate_order_number()

    #유저의 정보를 retrieve한다.
    user = auth.get_user(request)
    user_profile = UserProfile.objects.get(user=user)

    # 제품 비용 계산
    totalCost = 0
    # 면세 제품 비용 계산 변수
    tex_free_cost = 0

    ########################################################
    #Content모델을 들고와서 처리한다.
    content = get_object_or_404(Content, pk=pk)

    #면세 제품의 정보를 확인한다.
    if content.category.title == '교재':
        tex_free_cost = content.cost * quantity

    # 결제비용의 총액을 계산
    if content.isDiscount:
        totalCost = content.discount * quantity
    else:
        totalCost = content.cost * quantity
    ########################################################

    print("면제 제품 비용 : {}원".format(tex_free_cost))
    print("총 제품 비용 : {}원".format(totalCost))

    print("no.{} order_one_create executed in orders.views.py".format(merchant_uid))


    form = OrderCreateForm(initial={
        'merchant_uid':merchant_uid,
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
                      # 'cart': cart,
                      'merchant_uid': merchant_uid,
                      'name': user.first_name,
                      'content': content,
                      'quantity': quantity,
                      'phone': user_profile.phone,
                      'postal_code': user_profile.postal_code,
                      'address': user_profile.address,
                      'extraAddress': user_profile.extraAddress,
                      'detailAddress': user_profile.detailAddress,
                      'totalCost': totalCost,
                      'form': form,
                      'username':user.first_name,
                      'tex_free_cost': tex_free_cost,
                      'isDirect': True,
                  })

@login_required(login_url="accounts:login")
def order_create(request):
    print('order_create')
    #merchant_uid로 활용할 정보를 생성한다.
    merchant_uid = generate_order_number()

    #유저의 정보를 retrieve한다.
    user = auth.get_user(request)
    user_profile = UserProfile.objects.get(user=user)

    # 제품 비용 계산
    totalCost = 0
    # 면세 제품 비용 계산 변수
    tex_free_cost = 0

    ########################################################
    # 카트 세션의 정보와 dbCart의 정보를 retrieve한다.
    cart = Cart(request)
    dbCart = CM.objects.filter(user=user)

    # 면세 제품의 정보를 확인한다.
    for newItem in dbCart:
        if newItem.content.category.title == '교재':
            tex_free_cost += newItem.cost * newItem.quantity
    #결제비용의 총액을 계산
    totalCost = cart.get_total_cost()

    ########################################################

    print("면제 제품 비용 : {}원".format(tex_free_cost))
    print("총 제품 비용 : {}원".format(totalCost))

    print("no.{} order_create executed in orders.views.py".format(merchant_uid))


    form = OrderCreateForm(initial={
        'merchant_uid':merchant_uid,
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
                      'merchant_uid': merchant_uid,
                      'name': user.first_name,
                      # 'content': content,
                      # 'quantity': quantity,
                      'phone': user_profile.phone,
                      'postal_code': user_profile.postal_code,
                      'address': user_profile.address,
                      'extraAddress': user_profile.extraAddress,
                      'detailAddress': user_profile.detailAddress,
                      'totalCost': totalCost,
                      'form': form,
                      'username':user.first_name,
                      'tex_free_cost': tex_free_cost,
                      'isDirect': False,
                  })


@login_required(login_url="accounts:login")
def order_confirm(request):
    user = auth.get_user(request)

    confirm = ''
    result = False
    msg = ''


    print("order_confirm executed!")
    try:
        merchant_uid=request.POST.get('merchant_uid')
        order = Order.objects.get(merchant_uid=merchant_uid)
        order.confirm ='002'
        order.save()

        print(order.confirm)
        print("Product no.{} is confirmed to {}".format(merchant_uid, order.confirm))

        # ('001', '미정'),
        # ('002', '확정'),
        # ('003', '취소'),
        if order.confirm == '001':
            confirm = '미정'
        elif order.confirm == '002':
            confirm = '확정'
        elif order.confirm == '003':
            confirm = '취소'
        msg='confirm decision commit succeeded.'
        result = True
    except:
        print('error 발생')
        msg = 'confirm decision commit failed.'



    context = {
                'confirm': confirm,
                'result': result,
                'msg': msg,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required(login_url="accounts:login")
def order_cancel(request):
    #주문 취소를 위한 전달 context
    context = {}

    confirm=''
    result=False
    msg=''

    if request.method == 'POST':

        #POST로 전달된 폼 데이터 확인
        #현재 유저의 정보를 받아온다.
        user = auth.get_user(request)
        print("order_cancel executed with POST format data!")

        form = OrderCancelForm(request.POST)
        print("구매취소 폼이 유효한 상태로 전달 되었나? {}".format(form.is_valid()))
        print("구매취소로 전달된 데이터(주문번호:{}, 요청사항:{})".format(
            form.cleaned_data.get('merchant_uid'),
            form.cleaned_data.get('note')))

        if form.is_valid():
            #form save를 통한 OrderCancel 모델의 입력 수행 잠시 홀딩
            order_cancel = form.save(commit=False)
            #아임포트 API를 활용한 인스턴스 생성
            client = Iamporter(imp_key="1286359584086938",
                               imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

            #전달받은 Form 데이터에서 merchant_uid데이터를 확보후 Order인스턴스 retrieve함.
            merchant_uid = form.cleaned_data.get('merchant_uid')
            order = Order.objects.get(merchant_uid=merchant_uid)

            #Order인스턴스에 OneToOne모델로 매칭된 ImportInfo 모델을 별도로 인스턴스로 연결해서 편집작업 수행 준비
            importInfo = order.importInfo

            if order.confirm == '001':
                confirm = '미정'
            elif order.confirm == '002':
                confirm = '확정'
            elif order.confirm == '003':
                confirm = '취소'


            #OrderCancel 모델에 들어갈 내용을 입력
            order_cancel.order = order
            order_cancel.merchant_uid = merchant_uid
            order_cancel.note = form.cleaned_data.get('note')
            print("order_cancel({}) : {}".format(order_cancel.merchant_uid, order_cancel.note))

            #아임포트 API주문정보 인스턴스 생성
            payment = client.find_payment(merchant_uid=merchant_uid)
            print('주문 취소를 위해 호출한 payment의 정보 : {}'.format(payment))


            msg='validation was checked.'


            #아임포트 API를 활용한 취소 처리
            #확인을 위한 변수 Boolean 설정
            try:
                #취소 작업은 반드시, 결제 상태가 '결제완료(paid)' 상태로 되어있을 때,
                if payment['status'] == 'paid':
                    #현재 홈페이지에서 취소가 가능한 내역은 카드만 가능
                    if payment['pay_method'] == 'card':
                        print('아임포트 취소결과 : {}'.format(
                            client.cancel_payment(merchant_uid=merchant_uid,
                                                  amount=order.totalCost,
                                                  tax_free=order.tex_free_cost,
                                                  reason=order_cancel.note)))
                    #실시간 계좌이체와 가상 계좌를 통한 이체 방식은 환불에 제약이 있음.
                    else:
                        print('현재 결제 수단({})의 자동환불은 제한됩니다.'.format(payment['pay_method']))

                # launch asynchronous task
                order_canceled.delay(order.id)


                # ('001', '미정'),
                # ('002', '확정'),
                # ('003', '취소'),
                order.confirm = '003'
                print("Product no.{} is canceled".format(merchant_uid))

                if order.confirm == '001':
                    confirm = '미정'
                elif order.confirm == '002':
                    confirm = '확정'
                elif order.confirm == '003':
                    confirm = '취소'

                result= True
            except:
                print("############결제 취소 실패#############")


            if result:
                ########################아임포트 정보 갱신##########################
                importInfo.amount = payment['amount']
                importInfo.apply_num = payment['apply_num']
                importInfo.bank_code = payment['bank_code']
                importInfo.bank_name = payment['bank_name']
                importInfo.buyer_addr = payment['buyer_addr']
                importInfo.buyer_email = payment['buyer_email']
                importInfo.buyer_name = payment['buyer_name']
                importInfo.buyer_postcode = payment['buyer_postcode']
                importInfo.buyer_tel = payment['buyer_tel']
                importInfo.cancel_amount = payment['cancel_amount']
                importInfo.cancel_history = payment['cancel_history']
                importInfo.cancel_reason = payment['cancel_reason']
                importInfo.cancel_receipt_urls = str(payment['cancel_receipt_urls']).replace("['", "").replace("']", "")
                importInfo.cancelled_at = payment['cancelled_at'] \
                    if payment['cancelled_at'] == 0 \
                    else datetime.datetime.fromtimestamp(payment['cancelled_at'])
                importInfo.card_code = payment['card_code']
                importInfo.card_name = payment['card_name']
                importInfo.card_quota = payment['card_quota']
                importInfo.cash_receipt_issued = payment['cash_receipt_issued']
                importInfo.channel = payment['channel']
                importInfo.currency = payment['currency']
                importInfo.custom_data = payment['custom_data']
                importInfo.escrow = payment['escrow']
                importInfo.fail_reason = payment['fail_reason']
                importInfo.failed_at = payment['failed_at'] \
                    if payment['failed_at'] == 0 \
                    else datetime.datetime.fromtimestamp(payment['failed_at'])
                importInfo.imp_uid = payment['imp_uid']
                importInfo.merchant_uid = payment['merchant_uid']
                importInfo.name = payment['name']
                importInfo.paid_at = payment['paid_at'] \
                    if payment['paid_at'] == 0 \
                    else datetime.datetime.fromtimestamp(payment['paid_at'])
                importInfo.pay_method = payment['pay_method']
                importInfo.pg_id = payment['pg_id']
                importInfo.pg_provider = payment['pg_provider']
                importInfo.pg_tid = payment['pg_tid']
                importInfo.receipt_url = payment['receipt_url']
                importInfo.status = payment['status']
                importInfo.user_agent = payment['user_agent']
                importInfo.vbank_code = payment['vbank_code']
                importInfo.vbank_date = payment['vbank_date'] \
                    if payment['vbank_date'] == 0 \
                    else datetime.datetime.fromtimestamp(payment['vbank_date'])
                importInfo.vbank_holder = payment['vbank_holder']
                importInfo.vbank_issued_at = payment['vbank_issued_at'] \
                    if payment['vbank_issued_at'] == 0 \
                    else datetime.datetime.fromtimestamp(payment['vbank_issued_at'])
                importInfo.vbank_name = payment['vbank_name']
                importInfo.vbank_num = payment['vbank_num']
                ###############################################################

                importInfo.save()
                order.save()
                order_cancel.save()
                msg = "The order({}) was successfully cancelled.".format(order_cancel.merchant_uid)
                print("order_cancel : {}".format(order_cancel))


            # clear the cart
            # return redirect('accounts:order_status')

            context = {
                'confirm': confirm,
                'result' : result,
                'msg' : msg,
            }

    else:

            context = {
                'cancelForm' : OrderCancelForm(),
                'confirm': confirm,
                'result' : result,
                'msg': msg,
            }

    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")

