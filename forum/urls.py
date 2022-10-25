from django.urls import path
from forum.views import add_forum, delete_forum, get_forums_json, show_forum_index


app_name = 'forum'

urlpatterns = [
    path('',show_forum_index, name="show_forum_index"),
    path('json',get_forums_json, name="get_forums_json"),
    path('add', add_forum, name='add_forum'),
    path('delete/<id>',delete_forum,name='delete_forum')
    # path('/<id>',forum, name="forum")
]