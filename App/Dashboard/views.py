from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('dashboard')

@login_required(login_url="admin:login")
def dashboard(request):
    return HttpResponse("dashboard")
