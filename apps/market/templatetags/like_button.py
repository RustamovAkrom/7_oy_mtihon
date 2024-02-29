from django import template

from apps.users.models import AuthorLike

register = template.Library()
def check_like(opnion, user):
    return AuthorLike.objects.filter(opinion=opnion, user=user).exists()
register.filter(check_like)