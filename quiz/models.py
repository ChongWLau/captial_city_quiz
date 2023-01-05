from django.db import models

# Create your models here.
class Guess(models.Model):
    
    capital = models.CharField(max_length=50)
    guess = models.CharField(max_length=50, default="E.g. London")
    
    def check_answer(self):
        if not self.guess_text == self.capital_text:
            return False
        return True
