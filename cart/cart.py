from decimal import Decimal
from django.conf import settings
from kitchen.models import Choice


class Cart(object):

    def __init__(self, request):
        """
        Инициализируйте корзину.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраните пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
       Перебирайте меню в корзине и получайте продукты из базы данных
        """
        choice_ids = self.cart.keys()
        # получите выбранные объекты и добавьте их в корзину
        wide_choice = Choice.objects.filter(id__in=choice_ids)

        cart = self.cart.copy()
        for choice in wide_choice:
            cart[str(choice.id)]['choice'] = choice

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчитайте все товары в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, choice, quantity=1, update_quantity=False):
        """
        Добавьте товар в корзину или обновите его количество.
        """
        choice_id = str(choice.id)
        if choice_id not in self.cart:
            self.cart[choice_id] = {'quantity': 0,
                                     'price': str(choice.price)}
        if update_quantity:
            self.cart[choice_id]['quantity'] = quantity
        else:
            self.cart[choice_id]['quantity'] += quantity
        self.save()

    def save(self):
        # отметьте сеанс как "измененный", чтобы убедиться, что он будет сохранен
        self.session.modified = True

    def remove(self, choice):
        """
        Извлеките товар из корзины.
        """
        choice_id = str(choice.id)
        if choice_id in self.cart:
            del self.cart[choice_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.save()