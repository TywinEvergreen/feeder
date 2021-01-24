from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model


def primary_generator(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyz' \
                                                'ABCDEFGHJKLMNPQRSTUVWXYZ' \
                                                '23456789'):
    return get_random_string(length, allowed_chars)

def generate_random_email():
    """
    Генерирует случайный емаил. Используется для тестов
    """
    while True:
        generated_email = primary_generator() + '@gmail.com'
        if not get_user_model().objects.filter(email=generated_email).exists():
            return generated_email
