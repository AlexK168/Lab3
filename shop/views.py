from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


class OutletList(ListView):
    template_name = 'shop/outlets/index.html'
    model = Outlet


class TagList(ListView):
    template_name = 'shop/tags/index.html'
    model = Tag


class OutletDetail(DetailView):
    template_name = 'shop/outlets/show.html'
    model = Outlet


def home(request):
    return render(request, 'shop/home.html')


# Outlet views
def create_outlet(request):
    form = OutletForm()
    if request.method == 'POST':
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_outlets')
    context = {'form': form}
    return render(request, 'shop/outlets/new.html', context)


def update_outlet(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    form = OutletForm(instance=outlet)
    if request.method == 'POST':
        form = OutletForm(request.POST, instance=outlet)
        if form.is_valid():
            form.save()
            return redirect('show_outlet', pk=pk)
    context = {'form': form}
    return render(request, 'shop/outlets/new.html', context)


def delete_outlet(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    if request.method == 'POST':
        outlet.delete()
        return redirect('index_outlets')
    context = {'outlet': outlet}
    return render(request, 'shop/outlets/destroy.html', context)


# Tag views
def create_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_tags')
    context = {'form': form}
    return render(request, 'shop/tags/new.html', context)


def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(instance=tag)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('index_tags')
    context = {'form': form}
    return render(request, 'shop/tags/new.html', context)


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('index_tags')
    context = {'tag': tag}
    return render(request, 'shop/tags/destroy.html', context)


# auth views
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'shop/login.html', context)


def register(request):
    form = UserCreationForm
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'shop/register.html', context)
