from django.shortcuts import render, redirect
from .forms import SignupForm
from items.models import Product

# Create your views here.
def index(request):
    item = Product.objects.all()

    context = {
        'item': item
    }

    return render(request, 'core/index.html', context)

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

