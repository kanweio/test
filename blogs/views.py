from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from blogs import models


# Create your views here.

def main(request):
    if request.method == 'GET':
        posts = models.Post.objects.all()

        data = {
            'post': posts
        }
        return render(request, 'layouts/main.html', context=data)



def blogs_view(request):
    if request.method == 'GET':
        posts = models.Post.objects.all()

        data = {
            'post': posts
        }

        return render(request, 'posts/posts.html', context=data)

def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project!')


def now_data(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye!')


