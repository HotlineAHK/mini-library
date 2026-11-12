# Мини-библиотека

Учебный проект на Django (ДЗ 6, уроки 37-38).

Модели со связью:

- Author: name (строка, до 100)
- Book: title, author (ForeignKey на Author, on_delete=models.CASCADE), year (целое)

Форма добавления книги: BookForm (ModelForm), поля title, author, year.
Представление book_create: GET показывает пустую форму, POST валидирует,
сохраняет и редиректит на список книг.

Список книг: страница /books/, показывает название, автора, год,
запрос через Book.objects.select_related('author').

Запуск:

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Страницы: http://127.0.0.1:8000/books/ (список), http://127.0.0.1:8000/books/create/ (форма).
