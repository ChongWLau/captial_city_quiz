from django.test import TestCase, RequestFactory
from quiz.models import Quiz

from .views import guess, result


class QuizTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Quiz.objects.create(country="Wakanda", capital="Birnin Zana")
    
    def test_correct_answer(self):
        wakanda = Quiz.objects.get(country="Wakanda")
        expected_resp = "You were correct! Birnin Zana was the right answer!"
        self.assertEqual(wakanda.check_answer("Birnin Zana"), expected_resp)
    
    def test_incorrect_answer(self):
        wakanda = Quiz.objects.get(country="Wakanda")
        expected_resp = "Forever was wrong! The correct answer was actually Birnin Zana."
        self.assertEqual(wakanda.check_answer("Forever"), expected_resp)
    
    def test_quiz_view(self):
        request = self.factory.get('quiz')
        response = guess(request)
        self.assertEqual(response.status_code, 200)
    
    def test_quiz_view_post_redirect(self):
        request = self.factory.post('quiz', {'country': 'Wakanda', 'guess': 'Birnin Zana'})
        response = guess(request)
        self.assertEqual(response.status_code, 302)
    
    def test_incorrect_result_view(self):
        request = self.factory.get('quiz/result/Wakanda/Forever')
        response = result(request, 'Wakanda', 'Forever')
        self.assertEqual(response.status_code, 200)
    
    def test_correct_result_view(self):
        request = self.factory.get('quiz/result/Wakanda/Birnin Zana')
        response = result(request, 'Wakanda', 'Birnin Zana')
        self.assertEqual(response.status_code, 200)
    
    def test_result_view_bad_request(self):
        request = self.factory.get('quiz/result/Utopia/Birnin Zana')
        response = result(request, 'Utopia', 'Birnin Zana')
        self.assertEqual(response.status_code, 400)
    
    def test_result_view_duplicate_country(self):
        Quiz.objects.create(country="Wakanda", capital="Forever")
        request = self.factory.get('quiz/result/Wakanda/Birnin Zana')
        response = result(request, 'Wakanda', 'Birnin Zana')
        self.assertEqual(response.status_code, 500)
    
    def test_quiz_view_no_data(self):
        Quiz.objects.all().delete()
        request = self.factory.get('quiz')
        response = guess(request)
        self.assertEqual(response.status_code, 500)
