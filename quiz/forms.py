from django import forms

        
class QuizForm(forms.Form):
    country = forms.CharField(widget=forms.HiddenInput())
    guess = forms.CharField(label="Your Guess", max_length=50)