from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *
from django.contrib.auth import logout

# Create your views here.
def myfunction(request):
    return render(request, "mainpage.html")
def myabout(request):
    return render(request, "about.html")
def myabout1(request):
    return render(request, "about1.html")
def mylogin(request):
    return render(request, "login.html")
def myregistration(request):
    return render(request, "registration.html")
def mycontact(request):
    return render(request, "contact.html")
def mycontact1(request):
    return render(request, "contact1.html")
def adminhome(request):
    return render(request, "adminhomepage.html")
def userhome(request):
    return render(request, "userhomepage.html")
def payment(request):
    return render(request,"payment.html")

def registration_view(request):
    user_exists = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'User with this email already exists. Please log in.')
            return render(request, 'login.html')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.info(request, 'Account created Successfully!')
        return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if user.check_password(password):
            # If username and password match, redirect to admin page
            if username == 'admin@gmail.com' and password == 'admin':
                return render(request, 'adminhomepage.html') # Assuming the URL name for the admin page is 'admin_page'
            else:
                return  render(request, 'userhomepage.html')  # Assuming the URL name for the user page is 'user_page'
        else:
            # If password does not match, display a message
            messages.info(request, 'Invalid password. Please try again')
            return render(request, 'login.html')


def show_topplaces(request):
    topplaces = Topplaces.objects.all()
    return render(request, 'show_topplaces.html', {'topplaces': topplaces})
def show_tophotels(request):
    tophotels = Tophotels.objects.all()
    return render(request, 'show_tophotels.html', {'tophotels': tophotels})

def show_tophotels1(request):
    tophotels1 = Tophotels.objects.all()
    query = request.GET.get('place')
    if query:
        tophotels1 = tophotels1.filter(place__icontains=query)
    return render(request, 'show_tophotels.html', {'tophotels1': tophotels1})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('main')