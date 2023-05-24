from django import forms
from django.contrib.auth.models import User
from website.models import Customer, Order

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your  last name',
        'class': 'w-100 py-2 px-2 rounded'
    }))

class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('avatar', 'phone_number', 'adress',)

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your address',
        'class': 'w-100 py-2 px-2 rounded'
    }))


class OrderCreateStep1Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'description', 'category', 'size', 'quantity', 'photo')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter item name',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    
class OrderCreateStep2Form(forms.ModelForm):
    pickup_adress = forms.CharField(required=True)
    pickup_name = forms.CharField(required=True)
    pickup_phone = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ('pickup_adress', 'pickup_name', 'pickup_phone',)

    pickup_adress = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter pick address',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    pickup_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter pickup name',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    pickup_phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter pickup phone',
        'class': 'w-100 py-2 px-2 rounded'
    }))

class OrderCreateStep3Form(forms.ModelForm):
    delivery_address = forms.CharField(required=True)
    delivery_name = forms.CharField(required=True)
    delivery_phone = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ('delivery_address', 'delivery_name', 'delivery_phone',)

    delivery_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter delivery address',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    delivery_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter delivery name',
        'class': 'w-100 py-2 px-2 rounded'
    }))
    delivery_phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter delivery phone',
        'class': 'w-100 py-2 px-2 rounded'
    }))    

class OrderCreateStep4Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('payment_methods', )
