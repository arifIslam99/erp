from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     return HttpResponse("Allahu Akbar")
def index(request):
        template=loader.get_template('master.html')
        return HttpResponse(template.render())
def staff(request):
        template=loader.get_template('master.html')
        return HttpResponse(template.render())
def products(request):
        template=loader.get_template('master.html')
        return HttpResponse(template.render())
def orders(request):
        template=loader.get_template('master.html')
        return HttpResponse(template.render())
def profile(request):
        template=loader.get_template('master.html')
        return HttpResponse(template.render())
