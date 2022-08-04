from django.shortcuts import render


def home(request):
    return render(request, './tophatter/home.html')


def about(request):
    return render(request, './tophatter/about.html')


def services(request):
    return render(request, './tophatter/services.html')

def contact(request):
    return render(request, './tophatter/contact.html')


def story(request):
    return render(request, './tophatter/story.html')