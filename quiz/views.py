from django.http import HttpResponse
from django.shortcuts import render
import random
import requests

# Create your views here.
def guess(request):
    
    resp = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
    country_list = resp.json()['data']
    random_country = random.choice(country_list)
    
    context = {
        'country': random_country['name'],
        'capital': random_country['capital'],
    }
    return render(request, 'quiz/guess.html', context)


def result(request):
    
    if not request.method == 'POST':
        return HttpResponse("Sorry I didn't get your answer!")
        
    answer = str(request.POST['capital'])
    guess = str(request.POST['your_guess'])
    
    resp = f"You were correct! {guess} was the right answer!"
    if not answer.lower() == guess.lower():
        resp = f"The correct answer was actually {answer}."
    
    context = {'resp': resp,}
    
    return render(request, 'quiz/result.html', context)
