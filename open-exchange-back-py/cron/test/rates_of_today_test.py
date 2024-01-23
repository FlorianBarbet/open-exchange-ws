import os
import unittest
from datetime import datetime
from unittest import TestCase

import requests
import requests_mock

from core import open_exchange_singleton
from cron import rates_of_today

session = requests.Session()
adapter = requests_mock.Adapter()
session.mount('http://mocked', adapter)

open_exchange_singleton.base_url = 'http://mocked'
open_exchange_singleton.app_id = 'secret'


class JobTest(TestCase):
    def retrieve_rates_of_the_day(self):
        with requests_mock.Mocker() as m:
            today = datetime.today().strftime('%Y-%m-%d')

            url = 'http://mocked/api/historical/{date}.json'.format(date=today)
            m.get(url, json={'toto': 'ok'})

            self.assertEqual(rates_of_today.job(), {
                'toto': 'ok'
            })


if __name__ == '__main__':
    unittest.main()
