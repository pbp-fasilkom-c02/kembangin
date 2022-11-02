from django.test import TestCase
from django.urls import reverse, resolve
from forum.views import show_forum_detail,show_forum_index, get_forums_json,get_forum_by_pk, add_forum, add_comment, delete_forum, delete_comment, handle_vote
from main.models import User
from forum.models import Forum
import datetime

class TestUrls(TestCase):
    
    def test_forum_url_is_resolved(self):
        
        url = reverse("forum:show_forum_index")
        self.assertEquals(resolve(url).func,show_forum_index)
    
    def test_forum_detail_url_is_resolved(self):
        user = User.objects.create_user(username="dummyaa", email="dummyaa@dummy.com", password="dummy12345") 
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:show_forum_detail",kwargs={"pk":forum.pk})
        self.assertEquals(resolve(url).func,show_forum_detail)

    def test_get_forum_by_pk_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:get_forum_by_pk",kwargs={"pk":forum.pk})
        self.assertEquals(resolve(url).func,get_forum_by_pk)
    

    def test_get_forums_url_is_resolved(self):
        url = reverse("forum:get_forums_json")
        self.assertEquals(resolve(url).func,get_forums_json)

    def test_add_forum_url_is_resolved(self):
        url = reverse("forum:add_forum")
        self.assertEquals(resolve(url).func,add_forum)
    
    def test_delete_forum_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:delete_forum",kwargs={"id":forum.pk})
        self.assertEquals(resolve(url).func,delete_forum)


    def test_add_comment_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:add_comment",kwargs={"pk":forum.pk})
        self.assertEquals(resolve(url).func,add_comment)

    def test_delete_comment_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:delete_comment", kwargs={"pk":forum.pk})
        self.assertEquals(resolve(url).func,delete_comment)

    def test_upvote_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:handle_vote", kwargs={"pk":forum.pk, "action":"up"})
        self.assertEquals(resolve(url).func,handle_vote)

    def test_downvote_url_is_resolved(self):
        user = User.objects.create_user(username="dummyjj", email="dummyjj@dummy.com", password="dummys12345")
        forum = Forum.objects.create(question="This is test question",description="Lorem ipsum",created_at=datetime.datetime.now(),author=user)
        url = reverse("forum:handle_vote", kwargs={"pk":forum.pk, "action":"down"})
        self.assertEquals(resolve(url).func,handle_vote)
