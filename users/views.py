from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def register(request):

    if request.user.is_authenticated:
        return redirect("todos:home")

    elif request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect("users:register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("users:register")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                messages.success(request, "Successfully created account")
                return redirect("users:login")

        else:
            messages.info(request, "Passwords don't match")
            return redirect("users:register")

    return render(request, "users/register.html")


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("todos:home")

        else:
            messages.info(request, "Invalid Credentials")
            return redirect("users:login")

    elif request.user.is_authenticated:
        return redirect("todos:home")

    return render(request, "users/login.html")


@login_required(login_url="users:login")
def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("users:login")
