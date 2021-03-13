from django.shortcuts import render
from django.shortcuts import HttpResponse

def home_page(request):
    return HttpResponse('Wellcome to home page !!!')