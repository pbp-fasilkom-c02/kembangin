from django.urls import path
from forum.views import get_forums_json, show_forum_index


app_name = 'forum'

urlpatterns = [
    path('',show_forum_index, name="show_forum_index"),
    path('json',get_forums_json, name="get_forums_json")
    # path('', show_profile, name='show_profile'),
    # path('/<id>',forum, name="forum")
]