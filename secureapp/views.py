from django.shortcuts import render, redirect

from . forms import CreateUserForm

from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required

from django.contrib import messages


def home(request):
    
    return render(request, 'index.html')


def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
        
    context = {'RegisterForm': form}
    
    return render(request, 'register.html', context)
    

@login_required(login_url= 'two_factor:login')
def Dashboard(request):
    
    return render(request, 'dashboard.html')



def user_logout(request):
    
    auth.logout(request)
    
    messages.success(request, "Logout successful!")
    
    return redirect ("")


def account_locked(request):
    
    
    return render (request, "account-locked.html")



