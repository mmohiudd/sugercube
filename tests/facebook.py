import unittest
import json
import os
import sys

lib_path = os.path.abspath('..')
sys.path.append(lib_path)

from sugarcube.settings import SETTINGS
from sugarcube.facebook import Facebook


class TestFacebook(unittest.TestCase):
    def setUp(self):
        self.app_id = SETTINGS['facebook']['app_id']
        self.app_secret = SETTINGS['facebook']['app_secret']

        self.facebook = Facebook(SETTINGS['facebook'])

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

    def test_batch_call_with_fql(self):
        """
        test a batch call with fql
        """
        # 19292868552 is Facebook developers page
        batch = [
            {  # 0
                'method': "GET",
                'relative_url': """fql?q=SELECT name, fan_count,website
                FROM page WHERE page_id = 19292868552""",
            },
            {  # 1
                'method': "GET",
                'relative_url': """%s?fields=link""" % (self.app_id),
            }
        ]

        responses = self.facebook.api("", "POST", {
                'batch': batch
            })

        body = json.loads(responses[0]['body'])

        # graph call returns result data inside the 'data' variable
        self.assertEqual(
            body['data'][0]['website'],
            "http://developers.facebook.com")

    def test_batch_call_with_graph(self):
        """
        test batch call with graph
        """
        # 19292868552 is Facebook developers page
        batch = [
            {  # 0
                'method': "GET",
                'relative_url': """fql?q=SELECT name, fan_count,website
                FROM page WHERE page_id = 19292868552""",
            },
            {  # 1
                'method': "GET",
                'relative_url': """%s?fields=link""" % (self.app_id),
            }
        ]

        responses = self.facebook.api("", "POST", {
                'batch': batch
            })

        # graph call returns result data in the body
        body = json.loads(responses[1]['body'])

        link = ("http://www.facebook.com/apps/application.php?id=%s") \
        % (self.app_id)

        self.assertEqual(body['link'], link)
        self.assertEqual(body['id'], self.app_id)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFacebook)
unittest.TextTestRunner(verbosity=2).run(suite)
