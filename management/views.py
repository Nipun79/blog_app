from django.db import models
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from . models import Entry
# Create your views here.
class HomeView(ListView):
    model=Entry
    template_name = 'management/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(DetailView):
    model =Entry
    template_name = 'management/entry_detail.html'

class CreateEntryView(CreateView):
    model = Entry
    template_name = "management/create_entry.html"
    fields = ['entry_title','entry_text']
    def form_valid(self, form) :
        form.instance.entry_author = self.request.user
        return super().form_valid(form)
