
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from .models import Registration

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    name = 'John Doe'
    return render(request, 'index.html', {'name': name})

def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST, prefix='login')
        register_form = RegistrationForm(request.POST, prefix='register')
        
        if login_form.is_valid():
            # Handle login form submission
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = user_authenticate(username, password)
            
            if user is not None:
                # Authentication succeeded
                #login(request, user)
                return redirect('menu')  # Replace 'dashboard' with your desired page name or URL
            else:
                # Authentication failed
                error_message = 'Invalid username or password.'
        
        if register_form.is_valid():
            register_form.save()
            return redirect('registration_success')  # Create a success page or redirect to another view
    else:
        error_message=''
        login_form = LoginForm(prefix='login')
        register_form = RegistrationForm(prefix='register')
    return render(request, 'login.html', {'login_form': login_form, 'register_form': register_form, 'error_message': error_message})


def user_authenticate(username, password):
    try:
        user = Registration.objects.get(username=username)
        if user.password == password:
            return user
    except Registration.DoesNotExist:
        return None

def registration_success(request):
    return render(request, 'registration/registration_success.html')

def menu(request):
    return render(request, 'menu.html')



