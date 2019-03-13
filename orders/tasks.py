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
    if order.orderitem.count() > 1:
        subject = '주문번호:{} - 미메이커에서 {} 외 {}개 상품 주문이 완료되었습니다.'.format(order.order_no,
                                                                 order.orderitem.first().content,
                                                                 order.orderitem.count()-1)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미미에커 입니다.' \
                  '\n\n요청하신 {} 외 {} 개 상품이 잘 주문접수되었습니다.\n\n'.format(order.name,
                                                                    order.orderitem.first().content,
                                                                    order.orderitem.count() - 1)
    else:
        subject = '주문번호:{} - 미메이커에서 {} 상품 주문이 완료되었습니다.'.format(order.order_no,
                                                                     order.orderitem.first().content)
        message = '{}님 안녕하세요. ' \
                  '\n만들면서 배우는 코딩교육서비스 미미에커 입니다.' \
                  '\n\n요청하신 {} 상품이 잘 주문접수되었습니다.\n\n'.format(order.name,
                                                                   order.orderitem.first().content)
    print(subject)
    print(message)
    mail_sent = send_mail(subject,
                          message,
                          'openfingers@openfingers.com',
                          [order.user.email])

    # 운영자 확인용 메일 송부
    auth_subject = '{}님께서 {}을 주문하셨습니다.(금액:{})'.format(order.name,
                                                      order.orderitem.first().content,
                                                      order.totalCost)
    auth_message = '주문완료'
    send_mail(auth_subject,
              auth_message,
              'openfingers@openfingers.com',
              ['openfingers@openfingers.com'])

    return mail_sent