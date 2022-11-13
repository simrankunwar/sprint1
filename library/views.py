from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post


def home(request):
    return render(request, 'library/home.html')


def mylists(request):
    context = {
        'lists': Post.objects.all()
    }
    return render(request, 'library/mylists.html', context)
