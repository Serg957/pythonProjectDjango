from django.shortcuts import render
from django.views.generic import TemplateView


def platform(reguest):
    return render(reguest, 'third_task/platform.html')

def cart(reguest):
    return render(reguest, 'third_task/cart.html')

def games(reguest):
    return render(reguest, 'third_task/games.html')
