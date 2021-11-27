from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "accounts/login.html", context=context)


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
