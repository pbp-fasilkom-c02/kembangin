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
        user = User.objects.create_user(username="dummya", email="dummya@dummy.com", password="dummy12345")   
        client.login(username='dummya',password='dummy12345')
        response = client.get(reverse("forum:show_forum_detail",kwargs={"pk":user.pk}))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'forum_detail.html')

    def test_show_forum_detail_not_login(self):
        client = Client()
        user = User.objects.create_user(username="dummyb", email="dummyb@dummy.com", password="dummy12345")   
        response = client.get(reverse("forum:show_forum_detail",kwargs={"pk":user.pk}))
        self.assertEquals(response.status_code,302)

    def test_get_forum_by_pk_json(self):
        client = Client()
        user = User.objects.create_user(username="dummyc", email="dummyc@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:get_forum_by_pk",kwargs={'pk':forum.pk}))

        self.assertEquals(response.status_code,200)   

    def test_get_forum_json(self):
        client = Client()
        user = User.objects.create_user(username="dummyd", email="dummyd@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:get_forums_json"))
        self.assertEquals(response.status_code,200)   

    def test_add_forum(self):
        client = Client()
        user = User.objects.create_user(username="dummye", email="dummye@dummy.com", password="dummy12345")
        response = client.get(reverse("forum:add_forum"))
        self.assertEquals(response.status_code,200)   

    def test_add_comment(self):
        client = Client()
        user = User.objects.create_user(username="dummyf", email="dummyf@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:add_comment",kwargs={"pk":forum.pk}))
        self.assertEquals(response.status_code,302)   

    def test_delete_forum(self):
        client = Client()
        user = User.objects.create_user(username="dummyg", email="dummyg@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:delete_comment",kwargs={"id":forum.pk}))
        self.assertEquals(response.status_code,200)   

    def test_handle_upvote_comment(self):
        client = Client()
        user = User.objects.create_user(username="dummyh", email="dummyh@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:handle_vote",kwargs={"pk":forum.pk, "action":"up"}))
        self.assertEquals(response.status_code,302)   
    
    def test_handle_downvote_comment(self):
        client = Client()
        user = User.objects.create_user(username="dummyi", email="dummyi@dummy.com", password="dummy12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        response = client.get(reverse("forum:handle_vote",kwargs={"pk":forum.pk, "action":"down"}))
        self.assertEquals(response.status_code,302)  