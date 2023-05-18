from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@login_required(login_url="/login/")
def index(request):
    return render(request,'Task1/index.html')

def login_page(request):
    if request.method == "GET":
        return render(request, "Task1/login.html")
    user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        return render(request, "Task1/login.html", {"error": "Invalid Credentials"})


def user_registration(request):
    if request.method == "GET":
        return render(request, "Task1/user_registration.html")
    User.objects.create_user(username=request.POST["user_name"], email=request.POST["user_email"],
                             password=request.POST["password"])
    return HttpResponseRedirect("/login/")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")

