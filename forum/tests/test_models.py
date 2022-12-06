from django.test import TestCase
from forum.models import Forum, ForumReply
import datetime
from main.models import User

class TestModels(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="dummyeee", email="dummyeee@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        ForumReply.objects.create(comment="This is test comment",forum=forum, created_at=datetime.datetime.now(), author=user)


    def test_forum_models(self):
        forum = Forum.objects.get(question="This is test question")
        self.assertEqual(forum.question, "This is test question")

    def test_forum_reply_models(self):
        forumReply = ForumReply.objects.get(comment="This is test comment")
        self.assertEqual(forumReply.comment, "This is test comment")
    