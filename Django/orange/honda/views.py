from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gray(request):
    return HttpResponse('HI.... i am gray fanction views')
