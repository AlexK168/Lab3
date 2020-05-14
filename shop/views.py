from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from .decorators import *


class OutletList(ListView):
    template_name = 'shop/outlets/index.html'
    model = Outlet


class TagList(ListView):
    template_name = 'shop/tags/index.html'
    model = Tag


class ProductList(ListView):
    template_name = 'shop/products/index.html'
    model = Product


class OrderList(ListView):
    template_name = 'shop/orders/index.html'
    model = Order

    def get_queryset(self):
        if self.request.user.groups.exists():
            group = self.request.user.groups.all()[0].name
        return Order.objects.filter(customer=self.request.user.customer)


class OutletDetail(DetailView):
    template_name = 'shop/outlets/show.html'
    model = Outlet


class ProductDetail(DetailView):
    template_name = 'shop/products/show.html'
    model = Product


class OrderDetail(DetailView):
    template_name = 'shop/orders/show.html'
    model = Order


def home(request):
    return render(request, 'shop/home.html')


# Outlet views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def create_outlet(request):
    form = OutletForm()
    if request.method == 'POST':
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_outlets')
    context = {'form': form}
    return render(request, 'shop/outlets/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def delete_outlet(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    if request.method == 'POST':
        outlet.delete()
        return redirect('index_outlets')
    context = {'outlet': outlet}
    return render(request, 'shop/outlets/destroy.html', context)


# Tag views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def create_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_tags')
    context = {'form': form}
    return render(request, 'shop/tags/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('index_tags')
    context = {'tag': tag}
    return render(request, 'shop/tags/destroy.html', context)


# Products views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def create_product(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    form = ProductForm(initial={'outlet': outlet})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_outlet', pk=outlet.id)
    context = {'form': form}
    return render(request, 'shop/products/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    outlet = get_object_or_404(Outlet, pk=product.outlet.id)
    form = ProductForm(instance=product, initial={'outlet': outlet})
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product, initial={'outlet': outlet})
        if form.is_valid():
            form.save()
            return redirect('show_outlet', pk=product.outlet.id)
    context = {'form': form}
    return render(request, 'shop/products/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index_products')
    context = {'product': product}
    return render(request, 'shop/products/destroy.html', context)


# order views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'customers'])
def create_order(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_orders')
    context = {'form': form}
    return render(request, 'shop/orders/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'customers'])
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    customer = get_object_or_404(Customer, pk=order.customer.id)
    form = OrderForm(instance=order, initial={'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order, initial={'customer': customer})
        if form.is_valid():
            form.save()
            return redirect('index_orders')
    context = {'form': form}
    return render(request, 'shop/orders/new.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'customers'])
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('index_orders')
    context = {'order': order}
    return render(request, 'shop/orders/destroy.html', context)


# auth views
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'shop/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='customers')
                user.groups.add(group)
                username = form.cleaned_data.get('username')
                Customer.objects.create(user=user, name=username)
                messages.success(request, 'Account was successfully created for ' + username)
                return redirect('login')
        return render(request, 'shop/register.html', context)


def sign_out(request):
    logout(request)
    return redirect('login')
