# -*- coding: utf-8 -*-
import random
import os

import unittest

__author__ = 'serg'


from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from page_object import *


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        USEREMAIL = 'ftest12@tech-mail.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
     #   try:
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
        auth_form.wait_for_redirect()
        # except(Exception):
        #     self.driver.quit()


    def tearDown(self):
        self.driver.quit()

    def createRandomText(self, basic_text):
        random.seed()
        magic_num = random.randint(0, 1000)
        return basic_text.append(magic_num)
