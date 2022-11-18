"""
Модуль models.py.
Описыват модели Django
"""

from django.db import models


class SearchingUsers(models.Model):
    """
    Создание модели данных с именем SearchingUsers класса Model.
    Модель имеет одно текстовое поле: ByName, длиной 100 символов
    """

    ByName = models.CharField(max_length=100)
