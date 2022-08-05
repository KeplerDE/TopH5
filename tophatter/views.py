from django.shortcuts import render


def home(request):
    return render(request, './tophatter/home.html')


def registry(request):
    return render(request, './tophatter/registry.html')


def news(request):
    return render(request, './tophatter/news.html')

def contact(request):
    return render(request, './tophatter/contact.html')


def story(request):
    return render(request, './tophatter/story.html')