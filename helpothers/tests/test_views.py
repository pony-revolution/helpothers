from django.core.urlresolvers import reverse
from django.test import TestCase


class TestViews(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(url, {'next': 'some_url'})
        self.assertEqual(response.status_code, 200)
