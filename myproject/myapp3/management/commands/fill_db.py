from random import choices
from django.core.management.base import BaseCommand
from datetime import date, timedelta
from myapp3.models import Client, Product, Order

LOREM = ('Сказка о мёртвой царевне и семи богатырях Пушкина по сюжету едва ли не точь-в-точь похожа на сказку '
         'Белоснежка братьев Гримм. Написанная в стихах, она рассказывает о царице, которая родила прекрасную дочь, '
         'но вскоре умерла, а царь женился вновь и у девочки появилась мачеха. Та всё время спрашивала своё волшебное '
         'зеркальце “Свет мой, зеркальце! скажи, да всю правду доложи: я ль на свете всех милее, всех румяней и белее?” '
         'и однажды зеркальце ответило, что это не так')


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Client_{i}',
                            email=f'mail{i}@mail.ru',
                            address=" ".join(choices(text, k=3)),
                            date_registration=date.today()-timedelta(days=i*35))
            client.save()
            for j in range(1, count + 1):
                product = Product(
                    name=f'Product-{j}',
                    pdescription=" ".join(choices(text, k=64)),
                    price=15*j*i,
                    quantity=i,
                    date_added=date.today() - timedelta(days=i*j)
                )
                product.save()
                order = Order(
                    customer=client,
                    products=product,
                    date_ordered=date.today()-timedelta(days=j*i*10)
                )
                order.save()
