from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def landing_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ReviewForm()

    return render(request, 'landing_page.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')



