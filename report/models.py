from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Report(models.Model):

    CATEGORY_LIST = (
        ("CONSTRUCTION", "CONSTRUCTION"),
        ("SPECIAL_EVENT", "SPECIAL_EVENT"),
        ("INCIDENT", "INCIDENT"),
        ("WEATHER_CONDITION", "WEATHER_CONDITION"),
        ("ROAD_CONDITION", "ROAD_CONDITION"),
    )

    STATUS_LIST = (
        ("Por validar", "Por validar"),
        ("Validado", "Validado"),
        ("Resolvido", "Resolvido"),
    )

    category = models.CharField(max_length=17, choices=CATEGORY_LIST);
    location = models.CharField(max_length=120);
    author = models.CharField(max_length=120);
    description = models.TextField();
    creation_date = models.DateTimeField(auto_now_add=True);
    update_date = models.DateTimeField(auto_now=True);
    #update_date = models.DateTimeField();
    # Default "Por validar", não editável na criação
    status = models.CharField(max_length=20,choices=STATUS_LIST, default="Por validar");   

    # Normal reverse will only give /api/report/<pk>
    def get_api_url(self, request=None):
        return api_reverse("api-report:report_rud",kwargs={'pk':self.pk}, request=request)
    
