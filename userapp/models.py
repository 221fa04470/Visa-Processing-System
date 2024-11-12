# mainapp/models.py
from django.db import models

class PassportApplication(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='passport_photos/')
    contact_number = models.CharField(max_length=20)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class VisaApplication(models.Model):
    full_name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=100)
    country_of_residence = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=50)
    entry_type = models.CharField(max_length=50)
    travel_dates = models.DateField()
    photo = models.ImageField(upload_to='visa_photos/')
    purpose_of_visit = models.TextField()

    def __str__(self):
        return self.full_name

class ExtendedVisaApplication(models.Model):
    full_name = models.CharField(max_length=255)
    visa_number = models.CharField(max_length=100)
    reason_for_extension = models.TextField()
    requested_extension_dates = models.DateField()
    photo = models.ImageField(upload_to='extended_visa_photos/')

    def __str__(self):
        return self.full_name
# userapp/views.py

def submit_passport_application(request):
    if request.method == 'POST':
        # Create a new PassportApplication instance with form data
        application = PassportApplication(
            full_name=request.POST.get('passport-fullname'),  # Updated to match 'full_name' field in the model
            dob=request.POST.get('passport-dob'),
            address=request.POST.get('passport-address'),
            gender=request.POST.get('passport-gender'),
            nationality=request.POST.get('passport-nationality'),
            contact_number=request.POST.get('passport-contact'),
            father_name=request.POST.get('passport-father-name'),
            mother_name=request.POST.get('passport-mother-name')
            # Exclude 'application_type' and 'application_token' as they aren't in the model
        )
        application.save()  # Save to MongoDB
        return HttpResponse("Application submitted successfully.")
    else:
        return render(request, 'userhomepage.html')