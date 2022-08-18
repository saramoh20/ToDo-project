
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from datetime import datetime
from django.contrib import messages
from task.forms import UserForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def logup(request):
    user = UserForm()
    if request.method == "POST":

        username = request.POST.get['username']
        password = request.POST.get['password']
        password2 = request.POST.get['confirm_password']
        myuser = User.objects.create_user(username, password, password2)
        myuser.save()
        message.success(request, "Already have account.")
    #     # return redirect('login')

    return render(request, 'logup.html', {'logup': logup})


def login(request):
    if request.method == "POST":
        username = request.POST.get['username']
        password = request.POST.get['pass1']
        password2 = request.POST.get['pass2']
        myuser = User.objects.create_user(username, password, password2)
        myuser.save()
        message.success(request, "hi.")

    return render(request, 'login.html', {'login': login})


def search(request):
    return render(request, 'search.html', {'search': search})


def taskes(request):
    return render(request, 'taskes.html', {'taskes': taskes})
