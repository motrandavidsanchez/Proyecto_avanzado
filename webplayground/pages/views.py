from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PageForm
from .models import Page


class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
    form_class = PageForm


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
