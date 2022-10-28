from django.test import TestCase
from django.urls import reverse, resolve
from forum.views import show_forum_detail,show_forum_index
from main.models import User

class TestUrls(TestCase):

    def test_forum_url_is_resolved(self):
        url = reverse("forum:show_forum_index")
        self.assertEquals(resolve(url).func,show_forum_index)
    
    def test_forum_detail_url_is_resolved(self):
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="dummy12345") 
        url = reverse("forum:show_forum_detail",kwargs={"pk":user.pk})
        self.assertEquals(resolve(url).func,show_forum_detail)