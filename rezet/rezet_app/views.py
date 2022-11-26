from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import datetime
from .templates import *

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['uid'] = user.uid
                return redirect(profile)
            else:
                data = {'status':"Incorrect Password!!!"}
                print(data)
                return render(request, 'login.html', context=data)
        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            print(email,password)
            return render(request, 'signup.html', context=data)
    else:
        return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        adr = request.POST.get('adr')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if(password == confirm_password):
            user = User(uid=uid,first_name=first_name, last_name=last_name, adr=adr,
                            mobile=mobile, age=age, gender=gender, email=email, password=password)
            # user.save()
            return redirect(profile)
        return render(request, 'signup.html')
    if request.method == 'GET':
        return render(request, 'signup.html')
        
def profile(request):
    return render(request, 'profile.html')

def online(request):
    return render(request, 'online-shoping.html')

def offline(request):
    return render(request, 'offline-shoping.html')