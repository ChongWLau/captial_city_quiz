import requests
from quiz.models import Quiz


def run():
    
    old_data = Quiz.objects.all()
    old_data.delete()
    
    resp = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
    resp.raise_for_status()
    country_list = resp.json()['data']
    
    for country in country_list:
        c = Quiz(country=country['name'], capital=country['capital'])
        c.save()