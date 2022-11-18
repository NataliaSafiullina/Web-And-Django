"""
Модуль views.py
Содержит бизнес-логику приложения.
В нем описаны представления, т.е. обработчики.
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from manage import cursor
from .forms import NameForm
from .models import SearchingUsers


def get_name(request):
    """
    Представление get_name(). Отрисовывает форму и сохраняет введенные значения в модель.
    """

    print('Получен метод запроса: ', request.method)
    if request.method == 'POST':
        """ Если это запрос POST, нам нужно обработать данные формы """
        """ Создать экземпляр формы и заполнить данным из web-запроса """
        form = NameForm(request.POST)
        print('Сырые данные: ', request.POST)

        if form.is_valid():
            print('Введённое значение: ', form.cleaned_data['user_name'])
            """ Сохраним значение из формы в модель данных django """
            SearchingUsers.ByName = form.cleaned_data['user_name']
            """ Перенаправляем по адресу search """
            return HttpResponseRedirect('user/search')
        else:
            print('Form is not valid')

    else:
        """ Если GET (или любой другой метод), мы создадим пустую форму """
        form = NameForm()

    return render(request, 'users/index.html', {'form': form})


def user_by_name(request):
    """
    Представление user_by_name().
    Получает значения из модели и ищет данные в БД
    """

    print('Получили: ', SearchingUsers.ByName)

    """ Получим значение из модели и обрамляем их в % так как будем искать вхождение подстроки """
    substring = '%' + SearchingUsers.ByName + '%'

    """ Записываем текст запроса в строку с именем sql """
    sql = "select first_name, last_name, date_of_birth from user where first_name like %s order by first_name"
    """ Обращаемся к MySQL через созданный в manage.py курсор БД cursor"""
    cursor.execute(sql, substring)

    """ Объявляем переменую user_info как List """
    user_info = list()

    """ В цикле перебираем значения cursor """
    for r in cursor:
        #print(r[0], r[1], '\t', r[2])
        #user_info = str(r[0]) + str(r[1]) + str(r[2])
        """ Добавлем по одной записи данных об user в список user_info """
        sublist = [[r[0], r[1], str(r[2])]]
        user_info += sublist

    """ Показываем результат на странице user/search """
    return render(request, 'users/results.html', {'user': user_info, 'substring': substring})