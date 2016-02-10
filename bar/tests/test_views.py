import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.transaction import TransactionManagementError

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APITransactionTestCase

from ..models import Bar


ASSETS_DIR = os.path.join(settings.BASE_DIR, 'bar', 'tests', 'assets')


class BarUpdateViewTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user('foo')
        cls.bar = Bar.objects.create(name='changeme')
        cls.url = reverse('bar-detail', kwargs={'pk': cls.bar.pk})

    def test_anonymous_denied(self):
        """
        Show how to logout
        """
        self.client.force_authenticate(self.user)
        self.client.force_authenticate()  # Logout if previously logged in
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authenticated_allowed(self):
        """
        Force authenticate apply until you stop it
        """
        self.client.force_authenticate(self.user)
        # We can do it as long as we want...
        for i in range(0, 3):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 200)

    def test_update_default_format(self):
        """
        Assert that client send request with proper default content-type.
        """

        # See TEST_REQUEST_DEFAULT_FORMAT in settings.
        self.assertEqual(self.client.default_format, 'json')

        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, {'name': 'toto'})
        self.assertEqual(
            response.request['CONTENT_TYPE'],
            'application/json; charset=None',
        )
        # Same check, but more verbose
        self.assertEqual(
            response.wsgi_request.META.get('CONTENT_TYPE'),
            'application/json; charset=None',
        )

    def test_update_parser_format_json(self):
        """
        Using format parameter allow us to send proper Content-Type header and
        encode data. How could we live without?
        """
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, {'name': 'foo'}, format='json')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/json; charset=None')
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.content, '{"id":1,"name":"foo","doc":null}')  # for raw check, don't do this pleaaaase

    def test_update_parser_json_raw(self):
        """
        Yeah, you can still do it manually if you want!
        """
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, '{"name": "bar"}', content_type='application/json')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/json')
        self.assertEqual(response.data['name'], 'bar')

    def test_update_parser_xml(self):
        """
        Same as test_update_parser_format_json() but for XML lovers...
        """
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, {'name': 'baz'}, format='xml')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/xml; charset=utf-8')
        self.assertEqual(response.data['name'], 'baz')

    def test_update_parser_xml_raw(self):
        """
        Same as test_update_parser_format_json_raw() but for XML lovers...
        """
        self.client.force_authenticate(self.user)
        data = '<?xml version="1.0" encoding="utf-8"?><root><name>choco</name></root>'
        response = self.client.patch(self.url, data, content_type='application/xml')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/xml')
        self.assertEqual(response.data['name'], 'choco')

    def test_update_parser_multipart(self):
        """
        Test multipart format without sending file data...
        """
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, {'name': 'titi'}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'multipart/form-data; boundary=BoUnDaRyStRiNg; charset=utf-8',
            response.request['CONTENT_TYPE'],
        )
        self.assertEqual(response.data['name'], 'titi')

    def test_update_renderer_json(self):
        """
        Test response header in json
        """
        response = self.client.patch(self.url, HTTP_ACCEPT='application/json')
        self.assertEqual(response['content-type'], 'application/json')

    def test_update_renderer_xml(self):
        """
        Test response header in xml.
        """
        response = self.client.patch(self.url, HTTP_ACCEPT='application/xml')
        self.assertEqual(response['content-type'], 'application/xml; charset=utf-8')

    def test_update_parser_xml_renderer_json(self):
        """
        Test request with data send in xml and but response in json
        """
        self.client.force_authenticate(self.user)
        data = '<?xml version="1.0" encoding="utf-8"?><root><name>baz</name></root>'
        response = self.client.patch(
            self.url, data, format='xml', HTTP_ACCEPT='application/json')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/xml; charset=utf-8')
        self.assertEqual(response['content-type'], 'application/json')

    def test_update_parser_json_renderer_xml(self):
        """
        Test request with data send in json but response in xml
        """
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            self.url, {'name': 'foo'}, format='json', HTTP_ACCEPT='application/xml')
        self.assertEqual(response.request['CONTENT_TYPE'], 'application/json; charset=None')
        self.assertEqual(response['content-type'], 'application/xml; charset=utf-8')

    def test_update_file(self):
        """
        Test *multipart* format is not the default one anymore. Now, we need
        to set it explicitly.
        Also check that we display absolute file uri because this is good.
        Very good practice.
        """
        bar = Bar.objects.create()
        url = reverse('bar-detail', kwargs={'pk': bar.pk})

        self.client.force_authenticate(self.user)
        filepath = os.path.join(ASSETS_DIR, 'test.pdf')

        # Without format, it fallback to default (JSON)
        with open(filepath) as fp:
            response = self.client.patch(url, data={'doc': fp})  # BAAAAAD
            self.assertEqual(response.status_code, 400)

        with open(filepath) as fp:
            response = self.client.patch(
                url,
                data={'doc': fp},
                format='multipart',  # DON'T FORGOT IT
            )

        bar.refresh_from_db()
        self.assertIn(bar.doc.url, response.data['doc'])
        self.assertIn('http://testserver', response.data['doc'])

        # In fact, we could just do :
        self.assertEqual(
            response.data['doc'],
            'http://testserver{file.url}'.format(file=bar.doc),  # i.e : http://testserver is hardcoded in Django core
        )


class BarNameViewMixinTestCase(object):

    def test_rollback(self):
        """
        For purpose, try to execute a view which execute a DB transaction
        rollback.
        """
        Bar.objects.create(name='sethguekobar')

        bar = Bar.objects.create(name='changeme')
        url = reverse('bar-name', kwargs={'pk': bar.pk})

        return self.client.patch(url, {'name': 'sethguekobar'})


class BarNameViewTestCase(BarNameViewMixinTestCase, APITestCase):

    def test_rollback(self):
        """
        Assert that we cannot execute a DB transaction rollback with classes :

        * TestCase
        * APITestCase

        because they are already run into a DB transaction and we can't
        rollback remaining active transaction. (If you want to rollback some
        transaction inside other, you should use savepoint instead).

        As a result, we would got a ::

          TransactionManagementError: This is forbidden when an 'atomic' block is active.
        """
        with self.assertRaises(TransactionManagementError):
            super(BarNameViewTestCase, self).test_rollback()


class BarNameViewTransactionTestCase(BarNameViewMixinTestCase,
                                     APITransactionTestCase):

    def test_rollback(self):
        """
        Because test is not executed into a DB transaction, we could rollback
        it because there is no other active transaction...
        """
        response = super(BarNameViewTransactionTestCase, self).test_rollback()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "I will survive!")
