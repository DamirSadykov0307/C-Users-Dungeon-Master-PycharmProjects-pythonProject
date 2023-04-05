from django.shortcuts import render
from django.template import RequestContext
from myapp.templatetags.menu_tags import draw_menu

def draw_menu(request, menu_name):
    return render(request, 'menu.html', {'menu': draw_menu(context=RequestContext(request), menu_name=menu_name)})
