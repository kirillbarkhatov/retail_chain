from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Кастомная команда создания суперпользователя"""

    def handle(self, *args, **options):
        User = get_user_model()

        # Удалим пользователя, если существует
        existing_user = User.objects.filter(username="admin").first()
        if existing_user:
            existing_user.delete()

        # Создаем нового
        user = User.objects.create(
            username="admin",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("123qwe456rty")
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f"Успешно создан суперпользователь {user.username}")
        )
