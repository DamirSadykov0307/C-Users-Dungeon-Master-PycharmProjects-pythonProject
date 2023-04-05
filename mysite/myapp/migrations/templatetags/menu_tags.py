from django import template
from django.urls import resolve, reverse
from myapp.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path

    menu_items = MenuItem.objects.filter(parent=None, name=menu_name)

    def render_children(menu_item):
        children = menu_item.children.all()
        if children:
            return '<ul>' + ''.join(['<li><a href="{}"{}>{}</a>{}</li>'.format(
                child.url, ' class="active"' if current_url.startswith(child.url) else '', child.name, render_children(child)
            ) for child in children]) + '</ul>'
        else:
            return ''

    return '<ul>' + ''.join(['<li><a href="{}"{}>{}</a>{}</li>'.format(
        item.url, ' class="active"' if current_url.startswith(item.url) else '', item.name, render_children(item)
    ) for item in menu_items]) + '</ul>'