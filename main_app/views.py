from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ExampleView(TemplateView):
    template_name = "home.html"


