# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import unittest
import requests

class RquestTestCase(unittest.TestCase):
    def test_request(self):
        
        r = requests.get("https://github.com")
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()