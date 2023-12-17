from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "User not found")
            return render(request, "accaunt/login.html")
        login(request, user)
        messages.info(request, "Login succsesfly ")
        return redirect('blog:home')
    return render(request, "accaunt/login.html")


def logaut_view(request):
    logout(request)
    messages.info(request, 'Logaut saccsesfuly')
    return redirect('accaunt:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'R M O')
            return redirect('accaunt:login')
        messages.warning(request, 'R M O')
    form = SignUpForm()

    context = {'form': form}
    return render(request, 'accaunt/register.html', context)


