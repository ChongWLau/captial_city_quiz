from django import forms
# from models import Quiz


# class QuizModelForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         exclude = ('capital',)
        
class QuizForm(forms.Form):
    country = forms.CharField(widget=forms.HiddenInput())
    guess = forms.CharField(label="Your Guess", max_length=50)