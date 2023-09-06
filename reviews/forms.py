from django import forms
from captcha.fields import ReCaptchaField
from .models import Review

class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    review_text = forms.CharField(widget=forms.Textarea)
    rating = forms.FloatField(min_value=1, max_value=10)
    captcha = ReCaptchaField()

    class Meta:
        model = Review
        fields = ('name', 'email', 'review_text', 'rating')
