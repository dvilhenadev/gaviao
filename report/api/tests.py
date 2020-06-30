from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from report.models import Report
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

User= get_user_model()
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

class ReportAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="testuser",
            email="test@test.com"
        )
        user.set_password("randomirrelevantpassword")
        user.save();
        report = Report.objects.create(
            category="CONSTRUCTION",
            author=user,
            description="Testing description", 
            location="Test location", 
            )
    
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        
    def test_single_report(self):
        report_count = Report.objects.count()
        self.assertEqual(report_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-report:report_create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_post_item(self):
        data = {
            "description":"Oh my",
            "location":"deep space",
            "category":"SPECIAL_EVENT",
            "author":"api_url_tester"
        }
        url = api_reverse("api-report:report_create")
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        report = Report.objects.first()
        data = {}
        url = report.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        report = Report.objects.first()
        url = report.get_api_url()
        data = {
            "description":"changed description",
            "location":"oh no",
            "category":"INCIDENT",
            "author":"api_url_tester"
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_item_w_user(self):
        report = Report.objects.first()
        url = report.get_api_url()
        data = {
            "description":"changed description",
            "location":"oh no",
            "category":"INCIDENT",
            "author":"api_url_tester"
        }

        user_object = User.objects.first()
        payload = payload_handler(user_object)
        token_rsp = encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION="JWT "+token_rsp)

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_w_user(self):
        data = {
            "description":"Oh my",
            "location":"deep space",
            "category":"SPECIAL_EVENT",
            "author":"api_url_tester"
        }
        url = api_reverse("api-report:report_create")

        user_object = User.objects.first()
        payload = payload_handler(user_object)
        token_rsp = encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION="JWT "+token_rsp)

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)