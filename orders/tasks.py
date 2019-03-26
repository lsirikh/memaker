from celery import task
from django.core.mail import send_mail
from .models import Order
from django.contrib.auth.models import User

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    if order.orderItem.count() > 1:
        subject = '주문번호:{} - 미메이커에서 {} 외 {}개 상품 주문이 완료되었습니다.'.format(order.merchant_uid,
                                                                 order.orderItem.first().content,
                                                                 order.orderItem.count()-1)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미미에커 입니다.' \
                  '\n\n요청하신 {} 외 {} 개 상품이 잘 주문접수되었습니다.\n\n'.format(order.user.first_name,
                                                                    order.orderItem.first().content,
                                                                    order.orderItem.count() - 1)
    else:
        subject = '주문번호:{} - 미메이커에서 {} 상품 주문이 완료되었습니다.'.format(order.merchant_uid,
                                                                     order.orderItem.first().content)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미미에커 입니다.' \
                  '\n\n요청하신 {} 상품이 잘 주문접수되었습니다.\n\n'.format(order.user.first_name,
                                                                   order.orderItem.first().content)
    mail_sent = send_mail(subject,
                          message,
                          'openfingers@openfingers.com',
                          [order.user.email])

    # 운영자 통보를 별도로 알림
    # if order.importInfo.status == 'paid':
    #     # 운영자 확인용 메일 송부
    #     auth_subject = '{}님께서 {}을 주문하셨습니다.(금액:{}) from order_created'.format(order.user.first_name,
    #                                                       order.orderItem.first().content,
    #                                                       order.totalCost)
    #     auth_message = '주문완료'
    #     send_mail(auth_subject,
    #               auth_message,
    #               'openfingers@openfingers.com',
    #               ['openfingers@openfingers.com'])

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

    # 운영자 통보를 함께 알림
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