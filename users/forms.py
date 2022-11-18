"""
Модуль forms.py.
Описыват формы Django
"""

from django import forms


class NameForm(forms.Form):
    """
    Объявляем форму с именем NameForm принадлежащую классу Form.

    Форма имеет одно поле, строкового типа
    - имеет подпись - label
    - имеет максимальную длину пол 100 символов
    """

    user_name = forms.CharField(label='The username contains:', max_length=100)
