from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    a=2
    return HttpResponse('test哈哈哈~')
