from django.test import TestCase, Client
from django.urls import reverse
from forum.models import User


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