# -*- coding: utf-8 -*-
import os

from tests.basic_test import Test


from page_object import *

__author__ = 'serg'

class AuthTest(Test):
    def test(self):
        USERNAME = u'Госпожа Губернаторша'
        feed_page = MainPage(self.driver)
        user_name = feed_page.top_menu.get_username()
        self.assertEqual(USERNAME, user_name)