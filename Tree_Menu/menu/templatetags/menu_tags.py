from django import template

register = template.Library()


@register.inclusion_tag('menu/menu_list_tag.html')
def render_menu(menu):
    return {'menu': menu}
