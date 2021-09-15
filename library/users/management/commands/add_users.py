from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import Users


class Command(BaseCommand):
    help = 'Автоматическое создания суперпользователя и нескольких тестовых пользователей'

    def handle(self, *args, **options):
        users = [
            {
                'username': 'admin',
                'email': 'admin@sitename.com',
                'password': make_password('secret')
            },
            {
                'username': 'user_one',
                'email': 'user_one@sitename.com',
                'password': make_password('secret')
            },
            {
                'username': 'user_two',
                'email': 'user_two@sitename.com',
                'password': make_password('secret')
            }
        ]

        for user in users:
            try:
                new_user = Users(
                    username=user['username'], email=user['email'], password=user['password'])
                new_user.save()
                print(f'Пользователь {user["username"]} добавлен')
            except IntegrityError as e:
                print(e)
