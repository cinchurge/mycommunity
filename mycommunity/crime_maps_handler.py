from __future__ import absolute_import

import requests


class CrimeMapsAPIError(Exception):
    pass


class CrimeMapsHandler(object):
    url = "https://jgentes-Crime-Data-v1.p.mashape.com"

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def _query(self, endpoint, **params):
        headers = {
            "X-Mashape-Authorization": self.auth_token,
            "Accept": "application/json"
        }
        ret = requests.get(self.url + endpoint, headers=headers, params=params)
        if ret.status_code == 200:
            return ret.json()
        else:
            raise CrimeMapsAPIError("Error accessing Crime Maps API (%d): %s" %
                                    (ret.status_code, ret.text))
