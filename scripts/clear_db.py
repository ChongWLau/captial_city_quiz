from quiz.models import Quiz


def run():
    
    old_data = Quiz.objects.all()
    old_data.delete()