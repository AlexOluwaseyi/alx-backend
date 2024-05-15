import unittest

class LocaleTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_english_page(self):
        response = self.app.get('/', headers=[('Accept-Language', 'en')])
        self.assertIn('Hello, world!', response.data.decode())

    def test_french_page(self):
        response = self.app.get('/', headers=[('Accept-Language', 'fr')])
        self.assertIn('Bonjour le monde!', response.data.decode())

if __name__ == '__main__':
    unittest.main()
