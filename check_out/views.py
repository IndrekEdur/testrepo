from django.shortcuts import render
from .models import Check_out
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

class Check_outListView(ListView):
    queryset = Check_out.objects
    template_name = 'check_out/check_out_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Check_outs'] = Check_out.objects.all

        return context
