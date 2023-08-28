from django.core.management.base import BaseCommand
from lec2_app.models import User
from django.db import models

class Command(BaseCommand):
    help = "Create user."


    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='Роман', email='rrb13@example.com', password='secret', age=43)
        user.save()
        self.stdout.write(f'{user}')
