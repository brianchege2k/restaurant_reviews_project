from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

def landing_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Create an instance of the Review model and save the form data
            review_instance = form.save()
            messages.success(request, 'Your review has been submitted.')
            return redirect('thank_you')
        else:
            messages.error(request, 'Form validation failed. Please check your input.')
    else:
        form = ReviewForm()

    return render(request, 'landing_page.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
