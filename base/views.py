from django.shortcuts import render
from datetime import datetime


# # Пример 1
# def home_view(request):
#     return render(request, "base/home.html")
#     # В отличии от HttpResponse мы полностью управляем нашим шаблоном


# Пример 2 - Контекст
# def home_view(request):
#     # Вывод контекста в шаблон
#     return render(request,  "base/home.html", context={"name": "Bob"},)


# Пример 3 - Еще Контекст - передаем объект
# def home_view(request):
#     class User:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#     user = User("Bob", 19)
#     context = {"person": user}
#
#     return render(request, "base/home.html", context)


# Пример 4 - Еще Контекст - передаем объект и вызываем метод
# def home_view(request):
#     class User:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#         def info(self):
#             return f"Пользователь - {self.name} возраст - {self.age}"
#
#     user = User("Bob", 19)
#     context = {"person": user}
#
#     return render(request, "base/home.html", context)


# Пример 5 - ТЕГИ - тег for
# def home_view(request):
#     class User:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#         def info(self):
#             return f"Пользователь - {self.name} возраст - {self.age}"
#
#     user_0 = User("Bob", 19)
#     user_1 = User("Ray", 20)
#     user_2 = User("Man", 25)
#     context = {"data": [user_0, user_1, user_2]}
#
#     return render(request, "base/home.html", context)


# Пример 6 - ТЕГИ - тег for + if
# def home_view(request):
#     class User:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#         def info(self):
#             return f"Пользователь - {self.name} возраст - {self.age}"
#
#     user_0 = User("Bob", 19)
#     user_1 = User("Ray", 20)
#     user_2 = User("Man", 25)
#     context = {"data": [user_0, user_1, user_2]}
#
#     return render(request, "base/home.html", context)


# Пример 7/8 - ТЕГИ - тег for + cycle
# def home_view(request):
#     class User:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#         def info(self):
#             return f"Пользователь - {self.name} возраст - {self.age}"
#
#     data = [
#         User("Bob", 19),
#         User("Ray", 20),
#         User("Bob", 19),
#         User("Jey", 20),
#         User("Wey", 19),
#         User("Say", 20),
#         User("Yuma", 19),
#         User("Led", 20),
#         User("Ney", 19),
#         User("Ken", 20),
#
#     ]
#
#     context = {"data": data}
#
#     return render(request, "base/home.html", context)


# Пример 9 - Фильтры - задача преобразовать данные
# def home_view(request):
#     data = [i for i in range(100)]
#
#     context = {"data": data, "datetime": datetime.today()}
#
#     return render(request, "base/home.html", context)


# Пример 10 - Фильтры - пишем свой фильтр
def home_view(request):
    context = {"data": 'текст с Каком-то регистре'}

    return render(request, "base/home.html", context)
