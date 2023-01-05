from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random
from quiz.models import Quiz
from quiz.forms import QuizForm

# Create your views here.
def guess(request):
    
    if request.method == "POST":
        form = QuizForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect(
                reverse("result", kwargs=form.cleaned_data)
            )
    
    country_list = Quiz.objects.all()
    random_country = random.choice(country_list)
    
    context = {
        "country": random_country.country,
        "form": QuizForm({
            "country": random_country.country,
            "guess": "E.g. London"
        })
    }
    return render(request, "quiz/guess.html", context)


def result(request, country, guess):
    
    query = Quiz.objects.filter(country=country)
    if len(query) > 1:
        return HttpResponse('More than 1 country with that name')
    
    answer = query[0].capital
    
    resp = f"{guess} was wrong! The correct answer was actually {answer}."
    if answer == guess:
        resp = f"You were correct! {guess} was the right answer!"
    
    return render(request, 'quiz/result.html', {'resp': resp})
