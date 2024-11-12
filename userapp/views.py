from django.shortcuts import render, redirect
from django.http import HttpResponse
import random  # Import the random module

def apply(request):
    if request.method == 'POST':
        # Retrieve data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        passport_number = request.POST.get('passport_number')
        nationality = request.POST.get('nationality')
        date_of_birth = request.POST.get('date_of_birth')
        purpose_of_visit = request.POST.get('purpose_of_visit')

        # Handle the data (e.g., save it to the database or send an email)

        # Redirect to a success page after handling the data
        return redirect('success')

    return render(request, 'apply.html')

def submit_passport(request):
    if request.method == 'POST':
        # Handle the form submission logic here
        return HttpResponse("Passport application submitted successfully!")
    else:
        return HttpResponse("Invalid request.")

def submit_second_passport(request):
    if request.method == 'POST':
        # Handle form submission logic here
        return HttpResponse('Second passport application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')  # Or appropriate template

def submit_visa(request):
    if request.method == 'POST':
        # Handle the visa form submission
        return HttpResponse('Visa application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')  # Or the relevant template

def submit_extended_visa(request):
    if request.method == 'POST':
        # Process the extended visa form data here
        return HttpResponse('Extended visa application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')

def submit_family_details(request):
    if request.method == 'POST':
        # Handle the submitted family details here
        return HttpResponse("Family details submitted successfully.")
    return render(request, 'userhomepage.html')

def submit_application(request):
    if request.method == 'POST':
        # handle form submission
        return redirect('some_redirect_url')  # Ensure 'some_redirect_url' is defined in urls.py
    return render(request, 'userhomepage.html')

def generate_random_confirmation_number():
    return f"D160-{random.randint(100000, 999999)}"

def contact_view(request):
    confirmation_number = generate_random_confirmation_number()
    return render(request, 'contact.html', {'confirmation_number': confirmation_number})

def submit_passport_view(request):
    if request.method == 'POST':
        form = PassportApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # saves data to the MongoDB collection
            return redirect('thank_you')  # redirect after successful submission
    # Handle GET request or invalid form cases
    return render(request, 'submit_passport.html')  # Provide a relevant template for GET case

def user_homepage_view(request):
    return render(request, 'userhomepage.html')
