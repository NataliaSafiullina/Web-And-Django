"""
Модуль urls.py
Описывает связь между шаблонами и представлениями

У нас две страницы web-сайта:
- стартовая
- user/search

Им соответствуют обработчики:
- get_name()
- user_by_name()
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_name, name='user_name'),
    path('user/search', views.user_by_name, name='user_by_name'),
]