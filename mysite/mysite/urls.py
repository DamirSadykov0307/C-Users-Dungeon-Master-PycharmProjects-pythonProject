from django.urls import path
from . import views

urlpatterns = [
    path('menu/<str:menu_name>/', views.draw_menu, name='draw_menu'),
]
