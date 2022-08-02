from django.shortcuts import render


def home(request):
    return render(request, './tophatter/home.html')


def about(request):
    return render(request, './tophatter/about.html')


def services(request):
    return render(request, './tophatter/services.html')
