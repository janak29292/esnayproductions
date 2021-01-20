from django.http import Http404
from django.shortcuts import render


# Create your views here.
from accounts.models import Team, Portfolio, PortfolioCategory, Blog


def index(request, *args, **kwargs):
    team_players = Team.objects.all()
    portfolios = Portfolio.objects.filter(active=True)[:11]
    categories = PortfolioCategory.objects.all()
    blogs = Blog.objects.all().order_by('-id')[:10]
    context = {
        "team": team_players,
        "portfolios": portfolios,
        "categories": categories,
        "blogs": blogs
    }
    return render(request, 'index.html', context=context)


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def team(request, *args, **kwargs):
    team_players = Team.objects.all()
    context = {"team": team_players}
    return render(request, 'team.html', context=context)


def portfolio(request, *args, **kwargs):
    portfolios = Portfolio.objects.filter(active=True)[:50]
    categories = PortfolioCategory.objects.all()
    context = {
        "portfolios": portfolios,
        "categories": categories
    }
    return render(request, 'portfolio-four-columns.html', context=context)


def portfolio_detail(request, *args, **kwargs):
    pk = kwargs.get('pk')
    try:
        instance = Portfolio.objects.get(id=pk)
    except Portfolio.DoesNotExist:
        raise Http404
    context = {
        "portfolio": instance
    }
    return render(request, 'portfolio-single-item.html', context=context)


def blog(request, *args, **kwargs):
    blogs = Blog.objects.all().order_by('-id')
    context = {
        "blogs": blogs
    }
    return render(request, 'blog-fullwidth.html', context=context)


def blog_detail(request, *args, **kwargs):
    return render(request, 'blog-single-post.html')


def contact(request, *args, **kwargs):
    return render(request, 'contact.html')
