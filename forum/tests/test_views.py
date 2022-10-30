from django.test import TestCase, Client
from django.urls import reverse
from main.models import User
from forum.models import Forum,ForumReply
import datetime

class TestViews(TestCase):


    def test_show_forum_resolved(self):
        client = Client()
        response = client.get(reverse("forum:show_forum_index"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'forum_index.html')

    def test_show_forum_detail_resolved(self):
        client = Client()
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="dummy12345")   
        client.login(username='dummy',password='dummy12345')
        response = client.get(reverse("forum:show_forum_detail",kwargs={"pk":user.pk}))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'forum_detail.html')

    def test_show_forum_detail_not_login(self):
        client = Client()
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="dummy12345")   
        response = client.get(reverse("forum:show_forum_detail",kwargs={"pk":user.pk}))
        self.assertEquals(response.status_code,302)

    def test_get_forum_by_pk_json(self):
        client = Client()
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:get_forum_by_pk",kwargs={'pk':forum.pk}))

        self.assertEquals(response.status_code,200)   

    def test_get_forum_json(self):
        client = Client()
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:get_forums_json"))
        self.assertEquals(response.status_code,200)   

