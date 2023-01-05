from django.http import HttpResponseRedirect, HttpResponseServerError
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.urls import reverse
import random
from quiz.models import Quiz
from quiz.forms import QuizForm


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
    
    try:
        quiz = Quiz.objects.get(country=country)
    except MultipleObjectsReturned:
        raise HttpResponseServerError("Mutiple countries with same name")
    
    resp = quiz.check_answer(guess)
    
    return render(request, 'quiz/result.html', {'resp': resp})
