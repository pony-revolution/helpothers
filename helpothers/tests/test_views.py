from django.test import TestCase


class TestViews(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)
