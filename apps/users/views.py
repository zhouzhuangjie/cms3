from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    return HttpResponse('test哈哈哈~')
