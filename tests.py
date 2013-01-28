import unittest
from settings import SETTINGS
from facebook import Facebook


class TestSugercube(unittest.TestCase):
    def setUp(self):
        self.app_id = SETTINGS['app_id']
        self.app_secret = SETTINGS['app_secret']

        self.facebook = Facebook(SETTINGS)
        self.test_user = {
            'id': "100005126973855"
        }

    def test_app_access_token(self):
        """
        as no access_token is set, the access token should be
        <app_id>|<app_secret>
        """
        access_token = ("%s|%s") % (self.app_id, self.app_secret)

        self.assertEqual(
            self.facebook.get_access_token(),
            access_token
        )

    def test_access_token(self):
        """
        as no access_token is set, the access token should
        be same as app_access_token
        """

        self.assertEqual(
            self.facebook.get_access_token(),
            self.facebook.get_app_access_token()
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestSugercube)
unittest.TextTestRunner(verbosity=2).run(suite)
