from django.urls import path
from forum.views import add_forum, delete_comment, delete_forum, get_forums_json, handle_vote, show_forum_index, show_forum_detail,get_forum_by_pk, add_comment, delete_forum_flutter


app_name = 'forum'

urlpatterns = [
    path('',show_forum_index, name="show_forum_index"),
    path('json',get_forums_json, name="get_forums_json"),
    path('json/<int:pk>',get_forum_by_pk, name="get_forum_by_pk"),
    path('add', add_forum, name='add_forum'),
    path('delete/<int:id>',delete_forum,name='delete_forum'),
    path('delete-forum/<int:id>/<str:current_username>',delete_forum_flutter,name='delete_forum_flutter'),
    path('<int:pk>',show_forum_detail, name="show_forum_detail"),
    path('<int:pk>/add-comment',add_comment, name="add_comment"),
    path('<int:pk>/delete-comment/',delete_comment, name="delete_comment"),
    path('<int:pk>/vote/<str:action>',handle_vote,name="handle_vote")
]