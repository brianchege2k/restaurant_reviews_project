import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.conf import settings
from .models import Review  # Import the Review model

def landing_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if recaptcha_response:
                data = {
                    'secret': settings.RECAPTCHA_PRIVATE_KEY,
                    'response': recaptcha_response,
                }

                response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = response.json()

                if result['success']:
                    # Create an instance of the Review model and save the form data
                    review_instance = form.save(commit=False)  # Create an unsaved instance
                    # Additional processing or modifications to the instance if needed
                    review_instance.save()  # Save the instance to the database
                    messages.success(request, 'Your review has been submitted.')
                    return redirect('thank_you')
                else:
                    messages.error(request, 'reCAPTCHA validation failed. Please try again.')
            else:
                messages.error(request, 'reCAPTCHA validation failed. Please try again.')
        else:
            messages.error(request, 'Form validation failed. Please check your input.')
    else:
        form = ReviewForm()

    return render(request, 'landing_page.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
