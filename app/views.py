from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from app.forms import UserForm


# Create your views here.
def index(request):
    return render(
        request,
        "index.html",
    )


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(
        request,
        "register.html",
        context={"user_form": user_form, "registered": registered},
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(reverse("index"))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Datos de inicio de sesión inválidos.")
    else:
        return render(request, "login.html")
