from django import template

register = template.Library()


@register.filter()
def my_filter_2(data):
    data = f"{data} - это наши данные"
    return data
