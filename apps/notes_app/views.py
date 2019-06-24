from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import User
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    return render(request, "login_app/index.html")