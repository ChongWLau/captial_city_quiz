from django.db import models


class Quiz(models.Model):
    
    country = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)

    def check_answer(self, guess: str):
            
        if self.capital.lower() == guess.lower():
            return f"You were correct! {guess} was the right answer!"
        return f"{guess} was wrong! The correct answer was actually {self.capital}."
