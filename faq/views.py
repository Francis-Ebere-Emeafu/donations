from django.shortcuts import render

from faq.models import Question


def questions(request):
    items = Question.objects.all()
    return render(request, 'faq/about.html', {'items': items})
