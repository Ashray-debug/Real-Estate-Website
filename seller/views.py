from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from ..accounts/models import Realtor
from accounts.models import Realtor

def login(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']

	    realtor = auth.authenticate(username=username, password=password)

	    if realtor is not None:
	      auth.login(request, realtor)
	      messages.success(request, 'You are now logged in')
	      return redirect('sdashboard')
	    else:
	      messages.error(request, 'Invalid credentials')
	      return redirect('slogin')
	else:
	    return render(request, 'loginseller.html')

def dashboard(request):
	return render(request,'dashboard.html')


def logout(request):
	if request.method=='POST':
		auth.logout(request)
		messages.success(request,"Now you are successfully logout")
		return redirect('index')