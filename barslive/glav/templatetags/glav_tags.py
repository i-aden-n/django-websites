from django import template


register = template.Library()

@register.inclusion_tag('glav/z_header.html')
def header(links, cat_selected, user):
    return {'links': links, 'cat_selected': cat_selected, 'user': user}

@register.inclusion_tag('glav/z_footer.html')
def footer(links):
    return {'links': links}

@register.inclusion_tag('glav/z_item_card.html')
def item_card(news):
    return {'news': news}