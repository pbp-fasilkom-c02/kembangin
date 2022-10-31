from django.urls import path
from artikel.views import artikel_by_id_json, show_artikel
from artikel.views import create_new_artikel
from artikel.views import artikel_json
from artikel.views import delete_artikel
from artikel.views import comment_json
from artikel.views import handle_vote, share_exp

app_name = 'artikel'

urlpatterns = [
    path('', show_artikel, name="show_artikel"),
    path('create-new-artikel/', create_new_artikel, name="create_new_artikel"),
    path('json/', artikel_json, name='artikel_json'),
    path('comment/json/', comment_json, name='comment_json'),
    path('delete-artikel/<int:id>/', delete_artikel, name="delete-artikel"),
    path('json/<int:id>', artikel_by_id_json, name='artikel_by_id_json'),
    path('<int:id>/vote/<str:action>',handle_vote,name="handle_vote"),
    path('share-exp/', share_exp, name="share-exp"),
]
