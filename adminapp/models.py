from django.db import models  # Add this line

class PassportApplication(models.Model):
    # Your model fields here
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
