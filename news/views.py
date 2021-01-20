from django.shortcuts import render, get_object_or_404

from news.models import NewsPost


def news_list(request):
    posts = NewsPost.objects.filter(active=True).order_by('-reference_date')
    return render(request, 'news/news.html', {'items': posts})


def news_detail(request, id):
    item = get_object_or_404(NewsPost, pk=id)
    return render(request, 'news/newsdetail.html', {'item': item})
