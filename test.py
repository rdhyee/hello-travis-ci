# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import unittest
import requests

import selenium
from selenium import webdriver


class RquestTestCase(unittest.TestCase):
    def test_request(self):
        
        r = requests.get("https://github.com")
        self.assertEqual(r.status_code, 200)

    def test_selenium(self):

    	sel = webdriver.Firefox()
    	sel.get('https://en.wikipedia.org/wiki/Main_Page')

        commons_link = sel.find_element_by_xpath('//a[text()="Commons"]')
        self.assertEqual(commons_link.get_attribute('href'), 'https://commons.wikimedia.org/')

if __name__ == '__main__':
    unittest.main()
