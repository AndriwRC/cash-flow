from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from app.forms import UserForm, TransactionForm
from app.models import Transaction


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user).order_by("-date")

        balance = sum(t.amount if t.is_income() else -t.amount for t in transactions)

        return render(
            request,
            "index.html",
            context={"transactions": transactions, "balance": balance},
        )

    return render(request, "index.html")


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("index")
    else:
        form = TransactionForm()
    return render(request, "add_transaction.html", {"form": form})


def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TransactionForm(instance=transaction)

    return render(
        request, "edit_transaction.html", {"form": form, "transaction": transaction}
    )


def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    return redirect("index")


def delete_transaction_confirm(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    return render(
        request, "delete_transaction_confirm.html", {"transaction": transaction}
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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("index"))
