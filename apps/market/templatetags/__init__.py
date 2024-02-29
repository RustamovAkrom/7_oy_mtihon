from django import template

from apps.users.models import Author

register = template.Library()


def check_like(opnion, user):
    return Author.objects.filter(opinion=opnion, user=user).exists()
register.filter(check_like)