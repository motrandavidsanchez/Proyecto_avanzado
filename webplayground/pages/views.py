from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Page


class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
