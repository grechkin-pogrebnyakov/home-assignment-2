#!/usr/bin/env python2

import sys
import unittest
from tests.topic_test import SimpleTest
from tests.auth_test import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SimpleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
