from django.test import TestCase
from quiz.models import Quiz


class QuizTestCase(TestCase):
    def setUp(self):
        Quiz.objects.create(country="Wakanda", capital="Birnin Zana")
    
    def test_correct_answer(self):
        wakanda = Quiz.objects.get(country="Wakanda")
        expected_resp = "You were correct! Birnin Zana was the right answer!"
        self.assertEqual(wakanda.check_answer("Birnin Zana"), expected_resp)
    
    def test_incorrect_answer(self):
        wakanda = Quiz.objects.get(country="Wakanda")
        expected_resp = "Forever was wrong! The correct answer was actually Birnin Zana."
        self.assertEqual(wakanda.check_answer("Forever"), expected_resp)
