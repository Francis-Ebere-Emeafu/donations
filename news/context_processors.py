from news.models import NewsPost


def news_items(request):
    posts = NewsPost.objects.order_by('-reference_date')[:3]
    return {'posts': posts}
