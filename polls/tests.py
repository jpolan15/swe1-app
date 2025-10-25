from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_recent_question(self):
        """Recent questions should return True"""
        recent_time = timezone.now() - timedelta(hours=12)
        recent_question = Question(pub_date=recent_time)
        self.assertTrue(recent_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """Old questions should return False"""
        old_time = timezone.now() - timedelta(days=2)
        old_question = Question(pub_date=old_time)
        self.assertFalse(old_question.was_published_recently())
