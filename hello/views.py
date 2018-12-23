from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from hello.models import Post

# Create your views here.


def index(request):
    # return HttpResponse('Hi! this is django')
    data = Post.objects.all()
    return render(request, 'index.html', {'data': data})


def hellojson(request):
    return JsonResponse({'foo': 'bar'})
