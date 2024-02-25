from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Password
import random
import string

def index(request):
    return render(request, 'PasswordManager/index.html')

def signup(request):
    if request.method == "POST":
        Cname = request.POST.get("Cname", "")
        Cemail = request.POST.get("Cemail", "")
        Cpass1 = request.POST.get("cpass1", "")
        try:
            user = User.objects.get(username=Cname)
            return render(request, "PasswordManager/signup.html", {"message": "Username is already in use by another user!"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=Cname, email=Cemail, password=Cpass1)
            # Redirect to login page after successful signup
            return redirect(reverse('login'))
    return render(request, "PasswordManager/signup.html")

def Ulogin(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("login-home"))
    return render(request, "PasswordManager/login.html")

@login_required(login_url='/login')
def after_login(request):
    data = Password.objects.filter(user_name=request.user)
    return render(request, "PasswordManager/afterlogin.html", {"data": data})

def logout_page_user(request):
    logout(request)
    print("logginout")
    return redirect(reverse("home"))

def add_password(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        url = request.POST.get("url")
        password = request.POST.get("Password")
        Password.objects.create(Username=username, Url=url, Password=password, user_name=request.user)
        return redirect(reverse("login-home"))
    return render(request, "PasswordManager/add_password.html")

def generate_password_page(request):
    generated_password = generate_password(16)
    return render(request, "PasswordManager/generate_password.html", {"password": generated_password})

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    length = max(min(length, 21), 8)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def delete_pwd(request, pk):
    pwd = get_object_or_404(Password, id=pk)
    pwd.delete()
    return redirect(reverse("login-home"))

def update_pwd(request, pk):
    pwd = get_object_or_404(Password, id=pk)
    if request.method == "POST":
        url = request.POST.get("url")
        username = request.POST.get("Username")
        passwd = request.POST.get("Password")
        pwd.Url = url
        pwd.Password = passwd
        pwd.Username = username
        pwd.save()
        return redirect(reverse("login-home"))
    return render(request, "PasswordManager/update_pass.html", {"data": pwd})
def FAQ(request):
    return render(request,'PasswordManager\FAQ-logout.html')
def FAQlogin(request):
    return render(request,'PasswordManager\FAQlogin.html')
