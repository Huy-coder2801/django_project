from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, EditProfile
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()    
    
    context = {
            'form' : form
    }
    
    return render(request, 'core/signup.html', context)




