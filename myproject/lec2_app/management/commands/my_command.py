from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Выведите "Привет, мир!" для вывода.'


def handle(self, *args, **kwargs):
    self.stdout.write('Привет, мир!')
