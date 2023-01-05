from django.db import models


class Quiz(models.Model):
    
    country = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)

    def check_answer(self, guess):
        if self.capital == guess:
            return f"You were correct! {guess} was the right answer!"
        return f"{guess} was wrong! The correct answer was actually {self.capital}."