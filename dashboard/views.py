from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     return HttpResponse("Allahu Akbar")
def index(request):
        template=loader.get_template('index.html')
        return HttpResponse(template.render())
# Create your views here.
