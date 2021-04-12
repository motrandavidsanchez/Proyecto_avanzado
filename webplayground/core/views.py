from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'


class SamplePageView(TemplateView):
    template_name = 'core/sample.html'
