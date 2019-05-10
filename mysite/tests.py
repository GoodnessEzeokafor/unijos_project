from django.test import (
    SimpleTestCase,
    Client,
    TestCase
)


class HomeViewTest(SimpleTestCase):


    def test_home(self):
        c = Client()
        resp = c.get('')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/accounts/login')
        self.assertTemplateUsed('home.html')
        print(resp)
