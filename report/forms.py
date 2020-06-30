from django import forms
from .models import Report
from django.contrib.auth.models import User

class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report;
        fields = [
            'category',
            'location',
            'author',
            'description',
        ]
    
    # def clean_author(self, *args, **kwargs):
    #     author = self.cleaned_data.get("author");
    #     if not author in User.objects.all():
    #         print(User.objects.values().get(username__exact=author));
    #         raise forms.ValidationError("User is not registered")

class ReportUpdateForm(forms.ModelForm):
    class Meta:
        model = Report;
        fields = [
            'category',
            'location',
            'author',
            'description',
            'status',
        ]