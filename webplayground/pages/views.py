from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Page


class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
