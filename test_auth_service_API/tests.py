from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from test_auth_service_API.models import Perm
from test_auth_service_API.models import Role
from rest_framework import status


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        self.test_user = User.objects.create(username='testuser', password='testpassword')

        # URL for creating an account.
        self.create_url = reverse('account-create')
        

    def test_create_user(self):
        """
        Ensure we can create a new user without any issue.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url , data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)


class PermissionOnlyAfterLoginTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        try:
            self.test_user = Perm.objects.create(owner='foobar', title='test_permissions')
        except ValueError:
            pass
        
        # URL for creating permission.
        self.create_url = reverse('permission-create')
        
    def test_create_permission(self):
        """
        We will create permission and test it
        """
        expected_response = 403
        data = {
            'username': 'foobar',
            'title': 'test_permissions',
        }

        response = self.client.post(self.create_url , data, format='json')
        self.assertEqual(expected_response, response.status_code)

class RoleOnlyAfterLoginTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        try:
            self.test_user = Role.objects.create(owner='foobar', perms='test_permissions')
        except ValueError:
            pass
        
        # URL for creating permission.
        self.create_url = reverse('permission-create')
        
    def test_create_role(self):
        """
        We will create permission and test it
        """
        expected_response = 403
        data = {
            'username': 'foobar',
            'title': 'test_permissions',
        }

        response = self.client.post(self.create_url , data, format='json')
        self.assertEqual(expected_response, response.status_code)        