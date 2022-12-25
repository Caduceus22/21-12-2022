from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tkp_new


class HomePageView(ListView):
    model = Tkp_new
    template_name = 'home.html'
    context_object_name = 'all_tkp_list'


class TkpDetailView(DetailView):
    model = Tkp_new
    template_name = 'tkp_detail.html'
    context_object_name = 'tkp_detail'


class TkpCreateView(CreateView):
    model = Tkp_new
    template_name = 'tkp_new.html'
    fields = ['title', 'author', 'body']


class TkpUpdateView(UpdateView):
    model = Tkp_new
    template_name = 'tkp_new_update_form.html'
    fields = ['title', 'body']
    template_name_suffix = '_update_form'


class TkpDeleteView(DeleteView):
    model = Tkp_new
    template_name = 'tkp_delete.html'
    success_url = reverse_lazy('home')
