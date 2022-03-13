from django.utils.crypto import get_random_string

from user.models import User

chars = "abcdefghjkmnpqrstuvwxyzBCDEFGHJKLMNPQRSTUVWXYZ23456789"


def generate_random_string(length=10, allowed_chars=chars) -> str:
    return get_random_string(length, allowed_chars)


def generate_random_email() -> str:
    """
    Генерирует случайный емаил. Используется для тестов
    """
    while True:
        generated_email = generate_random_string() + "@gmail.com"
        if not User.objects.filter(email=generated_email).exists():  # type: ignore
            return generated_email
