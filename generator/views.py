# Python
import random

from django.shortcuts import render
#from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    special = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"""
    numbers = '0123456789'
    generated_password = ''
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters = characters + characters.upper()
    if request.GET.get('special'):
        characters = characters + special
    if request.GET.get('numbers'):
        characters = characters + numbers
    
    for x in range(length):
        generated_password += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': generated_password})