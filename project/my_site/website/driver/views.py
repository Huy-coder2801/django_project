from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from website.driver import forms
import pandas as pd
import numpy as np
from website.models import Order

@login_required()
def driver_page(request):
    return render(request, 'driver/driver_page.html')

@login_required(login_url='/signup/?next=/driver/')
def available_jobs(request, id):
    job = Order.objects.get(id=id)
    
    if not job:
        return redirect(reverse('core:driver:jobs'))
    
    if request.method == 'POST' and job.status == Order.PROCESSING_STATUS:
        job.driver = request.user.driver
        job.status = Order.PICKING_STATUS
        job.save()
        return redirect(reverse('core:driver:myjob'))
    
    return render(request, 'driver/available_jobs.html', {
         'item' : job
    })

@login_required(login_url='/signup/?next=/driver/')
def jobs(request):
    job = Order.objects.filter(status=Order.PROCESSING_STATUS)

    return render(request, 'driver/jobs.html', {
        'job': job
    })

@login_required(login_url='/signup/?next=/driver/')
def myjob(request):
    job = Order.objects.filter(
        driver=request.user.driver,
        status__in = [
            Order.PICKING_STATUS,
            Order.DELIVERY_STATUS,
        ]
    )

    if request.method == 'POST':
        if request.POST.get('status') == 'delivery':
            for j in job:
                j.status = Order.DELIVERY_STATUS
                j.save()
                return redirect(reverse('core:driver:myjob'))
        elif request.POST.get('status') == 'cancel':
            for j in job:
                j.status = Order.PROCESSING_STATUS
                j.save()
                return redirect(reverse('core:driver:jobs'))
        elif request.POST.get('status') == 'complete':
            for j in job:
                j.status = Order.COMPLETED_STATUS
                j.save()
                return redirect(reverse('core:driver:home'))

    return render(request, 'driver/my_job.html', {
        'myjob' : job
    })

@login_required(login_url='/signup/?next=/driver/')
def dashboard(request):
    driver = request.user.driver
    
    order = Order.objects.filter(
        driver = driver,
        status__in = [
            Order.COMPLETED_STATUS
        ]
    )
    order_item = Order.objects.filter(
        driver = driver,
        status__in = [
            Order.COMPLETED_STATUS
        ]
    ).values()

    df = pd.DataFrame(order_item).sort_values('size', ascending=False)
    df_name = df['name'].tolist()
    df_price = df['price'].tolist()
    df_size = df['size'].value_counts().tolist()
    quantity = df.shape[0]

    for item in order:
        driver.earnings += item.price
         

    return render(request, 'driver/dashboard.html', {
        'order' : order,
        'df' : df,
        'df_name': df_name,
        'df_price': df_price,
        'df_size' : df_size,
        'earnings_month' : driver.earnings,
        'quantity' : quantity
    })