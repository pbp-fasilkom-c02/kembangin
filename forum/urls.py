from django.urls import path
from forum.views import add_forum, delete_comment, delete_forum, get_forums_json, show_forum_index, show_forum_detail,get_forum_by_pk, add_comment


app_name = 'forum'

urlpatterns = [
    path('',show_forum_index, name="show_forum_index"),
    path('json',get_forums_json, name="get_forums_json"),
    path('json/<int:pk>',get_forum_by_pk, name="get_forum_by_pk"),
    path('add', add_forum, name='add_forum'),
    path('delete/<id>',delete_forum,name='delete_forum'),
    path('<int:pk>',show_forum_detail, name="show_forum_detail"),
    path('<int:pk>/add-comment',add_comment, name="add_comment"),
    path('<int:pk>/delete-comment/',delete_comment, name="delete_comment"),
   

]