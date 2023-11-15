from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from app.forms import UserForm
from app.models import Transaction


# Create your views here.
def index(request):
<<<<<<< HEAD
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user).order_by("-date")

        balance = sum(t.amount if t.is_income() else -t.amount for t in transactions)

        return render(
            request,
            "index.html",
            context={"transactions": transactions, "balance": balance},
        )

    return render(request, "index.html")
=======
    transactions = Transaction.objects.filter(user=request.user).order_by("-date")

    balance = sum(t.amount if t.is_income() else -t.amount for t in transactions)

    return render(
        request,
        "index.html",
        context={"transactions": transactions, "balance": balance},
    )
>>>>>>> c06149610b5ffd1e31887b0754a4cc08fe2b4159


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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("index"))
