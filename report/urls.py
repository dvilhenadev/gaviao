from django.contrib import admin
from django.urls import path
from report.views import report_create_view, report_listview, report_updateview, report_detailview

urlpatterns = [
    path('',report_listview,name="report_list"),
    path('create/',report_create_view,name="report_create"),
    path('<int:id>/',report_detailview,name="report_update"),
    path('<int:id>/update',report_updateview,name="report_update")
]
