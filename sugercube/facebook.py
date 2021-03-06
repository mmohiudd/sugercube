import urllib
import requests

import logging
logger = logging.getLogger(__name__)


class Facebook(object):
    domain_map = {
        'api': 'https://api.facebook.com/',
        'api_video': 'https://api-video.facebook.com/',
        'api_read': 'https://api-read.facebook.com/',
        'graph': 'https://graph.facebook.com/',
        'graph_video': 'https://graph-video.facebook.com/',
        'www': 'https://www.facebook.com/',
    }

    config = {
        'app_id': None,
        'app_secret': None
    }

    def __init__(self, config, access_token=None):
        self.config = config

        if access_token is None:
            self.access_token = ("%s|%s") % (config['app_id'], config['app_secret'])  # generic app access token
        else:
            self.access_token = access_token

    def get_app_id(self):
        return self.app_id

    def get_app_secret(self):
        return self.app_secret

    def get_domain_map(self):
        self.domain_map

    def get_access_token(self):
        return self.access_token

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_app_access_token(self):
        return ("%s|%s") % (self.config['app_id'], self.config['app_secret'])  # generic app access token

    def api(self, relative_url="", method="GET", call_data={}):
        url = self.domain_map['graph'] + relative_url

        # if a batch call and missing access_token
        if 'batch' in call_data:
            if 'access_token' in call_data:
                pass
            else:  # no access_token passed - set to app access_token
                call_data['access_token'] = self.get_app_access_token()

        data = urllib.urlencode(call_data)  # url encode request arguments

        try:
            if method is "GET":
                r = requests.get(url, data=data)
            elif method is "POST":
                r = requests.post(url, data=data)
            elif method is "PUT":
                r = requests.put(url, data=data)
            elif method is "DELETE":
                r = requests.delete(url, data=data)

            return r.json()
        except Exception as e:
            return {'error': e}
