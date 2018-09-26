from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Thing


class AllThingsList(ListView):
    context_object_name = 'things_list'
    template_name = 'things_list.html'
    model = Thing


class ThingDetail(DetailView):
    model = Thing
    template_name = 'thing_detail.html'