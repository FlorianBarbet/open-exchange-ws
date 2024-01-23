import os

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class OpenExchange:
    def __init__(self):
        self.base_url = os.getenv('OPEN_EXCHANGE_BASE_URL', default=None)
        self.app_id = os.getenv('OPEN_EXCHANGE_APP_ID', default=None)
        self.session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def get_rates_of_day(self, date: str) -> object:
        self.validate()
        url = '{base}/api/historical/{date}.json'.format(
            base=self.base_url, date=date)
        with self.session.get(url,
                              params={
                                  'app_id': self.app_id
                              },
                              headers={
                                  'Content-Type': 'application/json'
                              },
                              verify=False
                              ) as response:
            return response.json()

    def validate(self):
        if self.base_url is None:
            raise '[open_exchange.py] [env:OPEN_EXCHANGE_BASE_URL] No base url provided'
