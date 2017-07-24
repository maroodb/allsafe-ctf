from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect

from blog.models import News
from design.models import Slide


def blog(request, page=1):
    slides = Slide.objects.all()

    all_news = News.objects.all()

    paginator = Paginator(all_news, 3)
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, "blog/blog.html", locals())


def news(request, id_news=1):
    slides = Slide.objects.all()
    try:
        target_news = News.objects.get(pk=id_news)
    except News.DoesNotExist:
        return redirect('/blog')

    return render(request, "blog/news.html", locals())
