from django.contrib import admin
from django.urls import path, include
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
    path('submit_passport/', views.submit_passport, name='submit_passport'),
    path('submit_second_passport/', views.submit_second_passport, name='submit_second_passport'),
    path('submit_visa/', views.submit_visa, name='submit_visa'),
    path('submit_extended_visa/', views.submit_extended_visa, name='submit_extended_visa'),
    path('submit_family_details/', views.submit_family_details, name='submit_family_details'),
    path('submit-application/', views.submit_application, name='submit_application'),
    path('userhomepage/', views.user_homepage_view, name='user_homepage'),
]
