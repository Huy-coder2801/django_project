from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from website.customer import forms

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from website.models import Order
# Create your views here.
@login_required()
def home(request):
    return render(request, 'customer/customer_page.html')

@login_required(login_url='login/?next=/customer/')
def profile(request):
    user_form = forms.BasicUserForm(instance=request.user)
    customer_form = forms.BasicCustomerForm(instance=request.user.customer)
    password_form = PasswordChangeForm(request.user)

    if request.POST.get('action') == 'update_profile':
        if request.method == 'POST':
            user_form = forms.BasicUserForm(request.POST, instance=request.user)
            customer_form = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user.customer)

            if user_form.is_valid() and customer_form.is_valid():
                user_form.save()
                customer_form.save()
                return redirect(reverse('core:customer:home'))
            
    elif request.POST.get('action') == 'update_password':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect(reverse('core:customer:home'))
        
    return render(request, 'customer/profile.html', {
        'user_form' : user_form,
        'customer_form': customer_form,
        'password_form': password_form,
    })

@login_required(login_url='login/?next=/customer/')
def create_order(request):
    current_customer = request.user.customer
    medium_price = 25000.0
    large_price = 35000.0
    creating_order = Order.objects.filter(customer=current_customer, status=Order.CREATING_STATUS).last()
    step1_form = forms.OrderCreateStep1Form(instance=creating_order)
    step2_form = forms.OrderCreateStep2Form(instance=creating_order)
    step3_form = forms.OrderCreateStep3Form(instance=creating_order)
    step4_form = forms.OrderCreateStep4Form(instance=creating_order)
    
    if request.method == 'POST':
        if request.POST.get('step') == '1':
            step1_form = forms.OrderCreateStep1Form(request.POST, request.FILES, instance=creating_order)
            if step1_form.is_valid():
                creating_order = step1_form.save(commit=False)
                creating_order.customer = current_customer
                if creating_order.size == 'medium':
                    creating_order.price = medium_price 
                elif creating_order.size == 'large':
                     creating_order.price = large_price
                creating_order.save()
                return redirect(reverse('core:customer:create_order'))
            
        elif request.POST.get('step') == '2':
            step2_form = forms.OrderCreateStep2Form(request.POST, instance=creating_order)
            if step2_form.is_valid():    
                creating_order = step2_form.save()
                return redirect(reverse('core:customer:create_order'))
            
        elif request.POST.get('step') == '3':
            step3_form = forms.OrderCreateStep3Form(request.POST, instance=creating_order)
            if step3_form.is_valid():    
                creating_order = step3_form.save()
                return redirect(reverse('core:customer:create_order'))

        elif request.POST.get('step') == '4':
            step4_form = forms.OrderCreateStep4Form(request.POST, instance=creating_order)
            if step4_form.is_valid(): 
                creating_order.status = Order.PROCESSING_STATUS
                
                creating_order = step4_form.save()
                return redirect(reverse('core:customer:orders'))

    if not creating_order:
        current_step = 1
    elif creating_order.delivery_name:
        current_step = 4
    elif creating_order.pickup_name:
        current_step = 3
    else:
        current_step = 2

    return render(request, 'customer/create_order.html', {   
        'order' : creating_order,
        'current_step': current_step,
        'step1_form' : step1_form,
        'step2_form' : step2_form,
        'step3_form' : step3_form,
        'step4_form' : step4_form,
    })
    
@login_required(login_url='login/?next=/customer/')
def orders(request):
    order = Order.objects.filter(
        customer=request.user.customer,
        status__in = [
            Order.PROCESSING_STATUS,
            Order.PICKING_STATUS,
            Order.DELIVERY_STATUS,
        ]
    )

    return render(request, 'customer/orders.html', {
        'order': order
    })

@login_required(login_url='login/?next=/customer/')
def archived_orders(request):
    order = Order.objects.filter(
        customer=request.user.customer,
        status__in = [
            Order.COMPLETED_STATUS,
            Order.CANCELED_STATUS,
        ]
    )

    return render(request, 'customer/orders.html', {
        'order': order
    })

@login_required(login_url='login/?next=/customer/')
def details(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST' and order.status == Order.PROCESSING_STATUS:
        order.status = Order.CANCELED_STATUS
        order.save()
        return redirect(reverse('core:customer:archived'))

    return render(request, 'customer/details.html', {
        'order': order
    })