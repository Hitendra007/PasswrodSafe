from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from safe.models import Data
@login_required(login_url='signin')
def Home(request):
    user_obj=User.objects.get(username=request.user.username)
    pass_obj=Data.objects.filter(user=user_obj)
    category=[]
    website=[]
    username=[]
    password=[]
    objects = []
    for obj in pass_obj:
        entry = {
            'category': obj.category,
            'website': obj.website,
            'username': obj.username,
            'password': obj.password,
        }
        objects.append(entry)
    if request.method=="POST":
        Category=request.POST["category"]
        account=request.POST["website"]
        username=request.POST["username"]
        password=request.POST["password"]
        if Data.objects.filter(user=user_obj,category=Category,username=username,website=account,password=password).exists():
            messages.info(request,"Already saved in Database")
            return redirect('home')
        else:
            data_obj=Data.objects.create(user=user_obj,category=Category,website=account,username=username,password=password)
            data_obj.save()
            print("Data saved")
            messages.info(request,"saved!")
            return redirect('home')
    return render(request, 'home.html',{"objects":objects})


def signin(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('signin')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email=request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already exisits")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, "Password mismatch")
            return redirect('signup')
    return render(request, 'signup.html',)
@login_required(login_url="signin")
def logout(request):
    auth.logout(request,)
    return redirect('signin')
