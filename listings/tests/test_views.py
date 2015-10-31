from django.core.urlresolvers import reverse
from django.test import TestCase

from django_fakery import factory

from listings import models


class ListingViewsTestCase(TestCase):
    def setUp(self):
        self.regularuser = factory.make(
            'auth.User',
            fields={
                'username': 'regularuser',
                'password': 'regularuser',
                'is_staff': False,
            }
        )
        self.city = factory.make(
            'listings.City',
            fields={
                'name': 'Revolution City'
            }
        )

    def test_resource_add(self):
        url = reverse('resource-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.login(username='regularuser', password='regularuser')

        payload = {
            'name': 'resource name',
            'description': 'lorem ipsum',
            'url': 'http://example.com'
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)

        resource = models.Resource.objects.get(name='resource name')
        self.assertEqual(resource.author, self.regularuser)
        self.assertTrue(self.regularuser.has_perm('listings.change_resource', resource))


    def test_gathering_center_add(self):
        url = reverse('gathering-center-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.login(username='regularuser', password='regularuser')

        payload = {
            'location_name': 'Center name',
            'description': 'lorem ipsum',
            'address': 'Pony Rd',
            'city': self.city.id

        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 302)

        center = models.GatheringCenter.objects.get(location_name='Center name')
