from celery import task
from django.core.mail import send_mail
from products.models import Content
from orders.models import Order, OrderCancel, OrderDelivery, ImportInfo
from django.contrib.auth.models import User

from iamporter import Iamporter
import datetime

# celery -A memaker worker -l info
# celery -A memaker bea
@task
def order_notified(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)

    if order.importInfo.status == 'paid':
        # 운영자 확인용 메일 송부
        auth_subject = '{}님께서 {}을 주문하셨습니다.(금액:{})'.format(order.user.first_name,
                                                          order.orderItem.first().content,
                                                          order.totalCost)
        auth_message = '주문완료'
        mail_sent=send_mail(auth_subject,
                  auth_message,
                  'openfingers@openfingers.com',
                  ['openfingers@openfingers.com'])

    return mail_sent

@task
def order_canceled(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    if order.orderItem.count() > 1:
        subject = '주문번호:{} - 미메이커에서 {} 외 {}개 상품 주문을 취소하였습니다.'.format(order.merchant_uid,
                                                                 order.orderItem.first().content,
                                                                 order.orderItem.count()-1)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미메이커 입니다.' \
                  '\n\n요청하신 {} 외 {} 개 상품 주문취소가 완료되었습니다.' \
                  '\n항상 더 노력하는 미메이커가 될 수 있도록 하겠습니다.' \
                  '\n진심으로 감사드립니다. ' \
                  '\n\n만들면서 배우는 코딩교육 \'미메이커\''.format(order.user.first_name,
                                                                order.orderItem.first().content,
                                                                order.orderItem.count() - 1)
    else:
        subject = '주문번호:{} - 미메이커에서 {} 상품 주문을 취소하였습니다.'.format(order.merchant_uid,
                                                                     order.orderItem.first().content)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미메이커 입니다.' \
                  '\n\n요청하신 {} 상품의 주문취소가 완료되었습니다.' \
                  '\n항상 더 노력하는 미메이커가 될 수 있도록 하겠습니다.' \
                  '\n진심으로 감사드립니다. ' \
                  '\n\n만들면서 배우는 코딩교육 \'미메이커\''.format(order.user.first_name,
                                                                   order.orderItem.first().content)
    # print(subject)
    # print(message)
    mail_sent = send_mail(subject,
                          message,
                          'openfingers@openfingers.com',
                          [order.user.email])

    # 운영자 확인용 메일 송부
    auth_subject = '{}님께서 {}을 취소하셨습니다.(금액:{}, 결제수단:{})'.format(order.user.first_name,
                                                      order.orderItem.first().content,
                                                      order.totalCost, order.importInfo.pay_method)
    auth_message = '취소요청'
    send_mail(auth_subject,
              auth_message,
              'openfingers@openfingers.com',
              ['openfingers@openfingers.com'])

    return mail_sent


@task
def import_refresh():
    """
    Task to every minute refresh import data
    """

    #print('import_refresh() executed.')
    ########################### 아임포트 API 오브젝트 활용하여 미메이커 상점 정보 인스턴스 생성 #####################################
    client = Iamporter(imp_key="1286359584086938",
                       imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

    ####### 해당 유저가 보유한 모든 주문정보 확보 ######
    order_list = Order.objects.all()

    ######################유저가 현재 가지고 있는 주문 정보를 모두 가지고와 지속적인 업데이트 및 편집 작업###############################
    index = 0
    for order in order_list:

        payment = client.find_payment(merchant_uid=order.merchant_uid, imp_uid=order.imp_uid)
        importInfo = order.importInfo
        # print('{}.order information method : {}, status :{}'.format(index, order.merchant_uid, order.imp_uid))
        # print('{}.payment information method : {}, status :{}'.format(index, payment['merchant_uid'], payment['imp_uid']))

        # 지속적 검사를 통한 결제상태 확인
        if str(importInfo.status) != str(payment['status']):
            # 가상계좌의 결제상태가 paid가 되는 순간 관리자에게 메일을 보낸다.
            if importInfo.status == 'ready' and payment['status'] == 'paid':
                ############## launch asynchronous task(이메일)#################
                order_notified.delay(order.id)
            # print("order.importInfo.status : {} , payment['status'] : {}".format(importInfo.status,
            #                                                                           payment['status']))
            # print("payment정보가 갱신되어 ImportInfo 모델을 갱신합니다.")
            index += 1
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

            importInfo.save()
            # print(importInfo.__dict__)

        # CONFIRM_CAT = (
        #     ('001', '미정'),
        #     ('002', '확정'),
        #     ('003', '취소'),
        # )
        # 현재 order.confirm 상태가 취소가 아닌 상태에서 결제상태가 취소면 결제 확정/취소/미정도 그냥 따라서 취소로 변경해주도록 한다.
        if importInfo.status == 'cancelled' and order.confirm != '003' :
            # print('결제상태가 취소로 전환되어 주문 확정이 취소로 바뀝니다.')
            order.confirm = '003'
            order.save()
            order_canceled(order.id)

    message = '{}개의 importInfo tuple이 수정됨.'.format(index)

    return message



@task
def order_db_refresh():
    """
    Task to every minute refresh order data in DB
    """
    #운영자가 결제상태를 홈페이지에 order 모델 confirm을 취소(003)으로 설정만 해놓고,
    #실제 결제된 상황은 처리 하지 않은 경우
    #자동화를 위한 코드

    #print('order_db_refresh() executed.')
    ########################### 아임포트 API 오브젝트 활용하여 미메이커 상점 정보 인스턴스 생성 #####################################
    client = Iamporter(imp_key="1286359584086938",
                       imp_secret="QLVYiaFsqw5L43jRxmHbk61Vvic1a211OX068FyycDkgHD8f0QqkWsgrKssVvuXjsXqACZ9ODu5k7dz8")

    order_list = Order.objects.filter(confirm='003').filter(importInfo__status='paid')
    message = '특이사항 없음'

    for order in order_list:
        if not hasattr(order, 'orderCancel'):

            # launch asynchronous task
            order_canceled(order.id)

            message = '주문번호({})는 취소되었지만, 취소 모델이 생성되지 않았습니다. 결제수단: {}'.format(order.merchant_uid, order.importInfo.pay_method)
            #OrderCancel 모델을 추가로 생성해서 할당
            OrderCancel.objects.create(order=order, merchant_uid=order.merchant_uid, note='운영자에 의해서 취소가 된 품목입니다.')
            payment = client.find_payment(merchant_uid=order.merchant_uid)

            #실제 PG서버 내용이 PAID이면 다음과 같은 사항을 진행
            if payment['status'] == 'paid':
                #카드로 결제된 내역은 취소가 가능하지만, 가상계좌와 실시간 계좌이체는 지원안됨.
                if payment['pay_method'] == 'card':
                    client.cancel_payment(merchant_uid=order.merchant_uid,
                                          amount=order.totalCost,
                                          reason=order.orderCancel.note)


    return message