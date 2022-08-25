from atexit import register
from django import template

register = template.Library()

@register.inclusion_tag('msite/needs/header.html')
def header():
    return {}

@register.inclusion_tag('msite/needs/footer.html')
def footer():
    return {}

@register.simple_tag
def nav_links():
    return [
        {'link': 'home', 'name': 'Home'},
        {'link': 'home', 'name': 'About'},
        {'link': 'home', 'name': 'Contacts '},
        {'link': 'home', 'name': 'Suggession'},
    ]

@register.inclusion_tag('msite/needs/news_card.html')
def news_card(value):
    return {'n': value}