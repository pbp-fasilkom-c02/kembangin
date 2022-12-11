from django.urls import path
from report.views import *

app_name = 'report'

urlpatterns = [
    path('', show_reports, name='show_reports'),
    path('json/', show_json, name='show_json'),
    path('json/<str:username>/',show_json_by_username, name="show_json_by_username"),
    path('add-report/', add_report, name='add_report'),
    path('add-report-flutter/<str:username>', add_report_flutter, name='add_report_flutter'),
    path('delete-report/<int:id>/', delete_report, name='delete_report'),
]