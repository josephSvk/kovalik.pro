
from .models import Post
from django.shortcuts import render


def testfoto(request):
    # Príklad: načítanie príspevkov z modelu Post
    posts = Post.objects.all()
    return render(request, 'testfoto.html', {'posts': posts})