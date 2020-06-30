from rest_framework import serializers
from report.models import Report

class ReportSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Report
        fields = [
            'uri',
            'pk',
            'category',
            'location',
            'author',
            'description',
            'status',
            'creation_date',
            'update_date',
        ]

        read_only_fields=['author','creation_date']

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)