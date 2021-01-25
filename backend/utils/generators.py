from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

allowed_chars = 'abcdefghjkmnpqrstuvwxyzBCDEFGHJKLMNPQRSTUVWXYZ23456789'


def primary_generator(length=10, allowed_chars=allowed_chars) -> str:
    return get_random_string(length, allowed_chars)

def generate_random_email() -> str:
    """
    Генерирует случайный емаил. Используется для тестов
    """
    while True:
        generated_email = primary_generator() + '@gmail.com'
        if not get_user_model().objects.filter(email=generated_email).exists():
            return generated_email
