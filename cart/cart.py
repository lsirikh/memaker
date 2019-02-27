from decimal import Decimal
from django.conf import settings
#from shop.models import Product 변경해야 됨
from products.models import Content


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, content, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity
        :param content:
        :param quantity:
        :param update_quantity:
        :return:
        """

        content_id = str(content.pk)


        if content_id not in self.cart: #현재 상품이 카트 세션에 존재하지 않으면,
            if content.isDiscount:
                print("할인 항목")
                self.cart[content_id] = {'quantity': 0,
                                         'cost': str(content.discount)}
            else:
                self.cart[content_id] = {'quantity': 0,
                                         'cost': str(content.cost)}
        if update_quantity:
            self.cart[content_id]['quantity'] = quantity
        else:
            self.cart[content_id]['quantity'] += quantity

        self.save()

    def remove(self, content):
        """
        Remove a content from the cart
        :param content:
        :return:
        """

        content_id = str(content.id)
        if content_id in self.cart:
            del self.cart[content_id]
            self.save()

    def checkContent(self, content):
        """

        :param content:
        :return:
        """

        content_id = str(content.id)
        if content_id in self.cart:
            return True


    def __iter__(self):
        """
        Iterate over the items in the cart and get the contents
        from the database
        :return:
        """

        content_ids = self.cart.keys()
        #print("cart key : ",content_ids)
        #get the product objects and add them to the cart
        contents = Content.objects.filter(id__in=content_ids)
        #print(contents)

        cart =self.cart.copy()
        for content in contents:
            cart[str(content.id)]['content'] = content

        for item in cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item


    def __len__(self):
        """
        Count all items in the cart
        :return:
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_cost(self):
        return sum(Decimal(item['cost']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        #remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def isExist(self):
        #장바구니에 몇 개의 튜플이 담겼나....
        key = list(self.cart.keys())
        return int(len(key))

    def save(self):
        #mark the session as "modified" to make sure it gets saved
        self.session.modified = True



