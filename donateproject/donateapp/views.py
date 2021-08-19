from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *
from .models import Users, Offers


def homepage(request):
    print(request)

    all_users_qs = Users.objects.all()

    return render(request, 'homepage.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/offers')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'User was created for ' + username)
                return redirect('/login')

        context = {'form': form}
        return render(request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/offers')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/offers')
            else:
                messages.info(request, 'Username or password is incorrect.')

        return render(request, 'login.html')


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def offers(request):
    offers = Offers.objects.all()
    return render(request, 'offers.html', {'offers': offers})


@login_required(login_url='/login')
def specific_offer(request, pk):
    offer = Offers.objects.get(id=pk)

    context = {'offer': offer}
    return render(request, 'specific_offer.html', context)


@login_required(login_url='/login')
def add_offer(request):
    form = AddOffer()
    context = {'form': form}
    if request.method == 'POST':
        form = AddOffer(request.POST, request.FILES, initial={'name': request.user})
        print(request.user)
        if form.is_valid():
            form.save()
            return redirect('/offers')
    return render(request, 'add_offer.html', context)


@login_required(login_url='/login')
def my_offers(request, username):
    offers = Offers.objects.filter(name=username)
    context = {'offers': offers}

    if request.GET.get('delete-btn'):
        Offers.objects.filter(id=request.GET.get('delete-btn')).delete()

    return render(request, 'my_offers.html', context)
