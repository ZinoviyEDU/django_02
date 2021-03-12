from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def test_view(request):
    main_dict = {'name': 'Alisa',
         'age': 21,
         'point': 100,
         'is_big': True}

    data = {'title': 'Main page',
            'main_dict': main_dict}
    return render(request, 'test.html', data)
