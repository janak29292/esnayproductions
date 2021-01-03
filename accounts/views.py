from django.shortcuts import render


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'index.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def team(request, *args, **kwargs):
    return render(request, 'team.html')


def portfolio(request, *args, **kwargs):
    return render(request, 'portfolio-four-columns.html')


def blog(request, *args, **kwargs):
    return render(request, 'blog-fullwidth.html')


def contact(request, *args, **kwargs):
    return render(request, 'contact.html')
