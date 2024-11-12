from django.shortcuts import render

def user_homepage_view(request):
    return render(request, 'userhomepage.html')
