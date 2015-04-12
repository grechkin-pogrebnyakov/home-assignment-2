#!/usr/bin/env python2

import sys
import unittest
from tests.topic_test import TopicDeleteTestCase, TopicMainTestCase
from tests.auth_test import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(TopicDeleteTestCase),
        unittest.makeSuite(TopicMainTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
