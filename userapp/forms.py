# userapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Adjust to your actual template
