"""
Модуль urls.py
Описывает связь между шаблонами и представлениями
"""

from django.urls import path
from . import views

"""
У нас два страницы web-сайта:
- стартовая
- user/search

Им соответствуют обработчики:
- get_name()
- user_by_name()
"""

urlpatterns = [
    path('', views.get_name, name='user_name'),
    path('user/search', views.user_by_name, name='user_by_name'),
]