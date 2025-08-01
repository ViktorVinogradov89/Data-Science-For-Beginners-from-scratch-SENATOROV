"""Изучение CPython и сравнение с PyPy."""

# ### Введение в Python и CPython
#
# 1) Что такое CPython и чем он отличается от Python?
# - Python это язык, а CPython это его реализация написанная на C.
# Cpython это и язык программирования, и интерпретатор.
# 2) Сколько существует реализаций Python, и какая из них самая популярная?
# - У Python 6 реализаций, самая популярная CPython
# 3) На каком языке написан CPython?
# - На языке C
#
# ### Поиск и установка CPython
# 4) (опционально) Кто создал CPython?
# - Guido van Rossum
# 5) Почему Python считается быстрым, несмотря на то, что это интерпретируемый
# язык?
# Python «быстрый», потому что:
# - Позволяет быстро писать код
# - Использует оптимизированные C-библиотеки(потому что написан на C)
# - Достаточно шустрый для 90% задач
# 6) Напишите путь к Интерпретатору CPython на вашем компьютере
# C:\Users\USER\AppData\Local\Programs\Python\Python313\python.exe
#
# ### Структура CPython
# 7) Что содержится в папке include в CPython?
# Папка include — это «инструкция по сборке» в ней находятся исходники для:
# - C-расширений
# - встраивания Python в C
# - модификации самого интерпретатора.
# 8) Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб
# - https://github.com/python/cpython
# 9) (опционально) Как работает интерпретатор CPython при выполнении кода?
# читает и запускает код построчно
#
# ### Запуск файла с помощью CPython
# 10) Какая команда используется для запуска файла с помощью CPython?
# - сначало указываем путь до интерпритатора, затем путь до файла
# 11) Можно ли запускать текстовые файлы через интерпретатор Python? Почему?
# - можно,интерпретатору всё рвно какое расширение файла запускать
# 12) Как указать путь к интерпретатору и файлу для выполнения кода?
# - В проводнике или консоли ищем местонахождение интерпретатора и файла,
# копируем путь через свойства, далее указываем путь до интерпритатора,
# затем путь до файла
#
# ### Введение в PyPy
# 13) Чем PyPy отличается от CPython?
# - PyPy - это нитрепретатор который работает в 10 раз быстрее чем CPython,
# единственный минут что он пока не совместим со всеми проектами на питоне,
# так как достаточно новый
# 14) Почему PyPy не может использоваться для всех проектов на Python?
# - Он пока не совместим со всеми проектами на питоне так как достаточно новый
# 15) Где можно скачать PyPy?
# - https://pypy.org
#
# # Практические задания
# ### Задание 1: Поиск и установка CPython
# Проверьте, установлен ли CPython на вашем компьютере:
# - Используйте поиск в меню "Пуск" (Windows) или терминале (Linux/Mac).
# - Введите команду python --version или python3 --version в терминале.
# Если CPython не установлен, скачайте его с официального сайта Python
# https://www.python.org/downloads/ и установите.
# - Установил
#
# ### Задание 2: Исследование структуры CPython
# Найдите папку, где установлен Python (например, через команду which python в
# терминале или свойства ярлыка).
# Откройте папку include и изучите её содержимое. Какое количество файлов на C
# там есть?
# - 74
# Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython)
# и найдите файл README. Прочитайте информацию о проекте.
# - прочитал
#
# ### Задание 3: Запуск файла с помощью CPython
# Создайте текстовый файл example.txt с содержимым:
# print("Hello from CPython!")
# Запустите файл через команду python <путь_до_файла> (замените
# <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на
# .py и повторите запуск.
# Оба варианта запустились, на экране появилась надпись Hello from CPython!
#
# ### Задание 4: Установка и использование PyPy
# Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте
# подходящую версию для вашей операционной системы.
# Распакуйте скачанный архив в удобное место.
# Создайте файл example_pypy.py с кодом:
# print("Hello from pypy!")
# Запустите файл через PyPy
# pypy <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему
# файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на
# .py и повторите запуск.
# Интерпритатор так же читает оба формата, выводит надпись Hello from pypy!
#
# Задание 5: Сравнение производительности CPython и PyPy
#
#  Создайте файл performance_test.py с кодом:
#      import time
#      start_time = time.time()
#      total = 0
#      for i in range(1, 10000000):
#          total += i
#      end_time = time.time()
#
#      print("Result:", total)
#      print("Execution time:", end_time - start_time, "seconds")
#
# Запустите этот файл сначала через CPython, а затем через PyPy. Запишите
# результаты времени выполнения для обоих интерпретаторов
# Сделайте вывод о разнице в производительности.
# CPython:
# - Execution time: 1.8961944580078125 seconds
# PyPy:
# - Execution time: 0.02500152587890625 seconds
# PyPy работает значительно быстрее чем CPython
