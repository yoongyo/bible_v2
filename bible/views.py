from django.shortcuts import render, get_object_or_404
from .models import Bible


def bible_list(request):
    bible = Bible.objects.all()
    return render(request, 'bible/bible_list.html', {
        'bible': bible
    })


def bible_detail(request, pk):
    bible = get_object_or_404(Bible, pk=pk)
    return render(request, 'bible/bible_detail.html', {
        'bible': bible
    })


def shortcut(request):
    return render(request, 'bible/shortcut.html')


def introduction(request):
    return render(request, 'bible/introduction.html')


def shape(request):
    return render(request, 'bible/shape.html')