from django.urls import path
from .views import ReportRudView,ReportAPIView

urlpatterns = [
    path('',ReportAPIView.as_view(),name="report_create"),
    path('<int:pk>/',ReportRudView.as_view(),name="report_rud"),
    
]
