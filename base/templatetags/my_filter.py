from django import template

register = template.Library()


@register.filter()
def my_upper(word):
    return word.upper()
