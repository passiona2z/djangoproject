from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 아주 간단한 뷰
def hello_world(request):
    return HttpResponse("Hello World")
