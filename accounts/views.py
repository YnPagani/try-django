from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    form = UserCreationForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        context["form"] = form
        if form.is_valid():
            user_obj = form.save()
            return redirect("/login")

    return render(request, "accounts/register.html", context)


def login_view(request):
    """
    Handles the user login and redirect to admin page if loggin successfully
    """
    username, password = -1, -1
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html", context=context)

        login(request, user)
        return redirect("/admin")

    return render(request, "accounts/login.html", {})


def logout_view(request):
    """
    Handles the user logout
    """
    if request.method == "POST":
        logout(request)
        return redirect("/login/")

    return render(request, "accounts/logout.html", {})


# def register_view(request):

#     return render(request, "accounts/register.html", {})
