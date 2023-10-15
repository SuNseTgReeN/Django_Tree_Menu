from django import template

register = template.Library()


@register.simple_tag
def draw_menu(menu):
    return _render_menu(menu)


def _render_menu(menu):
    if not menu:
        return ''

    menu_html = '<ul>'
    for item in menu.menu_set.all():
        menu_html += '<li>'
        menu_html += f'<a href="{item.url}">{item.name}</a>'
        menu_html += _render_menu(item)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
