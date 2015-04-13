# -*- coding: utf-8 -*-
import random
import os

import unittest

__author__ = 'serg'


from selenium.webdriver import DesiredCapabilities, Remote
from page_object import *


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )


    def tearDown(self):
        self.driver.quit()

    def createRandomText(self, basic_text):
        random.seed()
        magic_num = random.randint(0, 1000)
        return basic_text + magic_num.__str__()


class TestWithAuth(Test):
    def setUp(self):
        self.BLOG = 'Флудилка'
        self.TITLE = self.createRandomText('MyTopic')
        self.MAIN_TEXT = self.createRandomText(u'Мой текст')
        self.LINK_ADDR = self.createRandomText('bla_bla_bla.com')
        self.LINK_TEXT = self.createRandomText('great web cite ')
        self.USER_ADD = u'Котегов'
        self.PATH_TO_PIC = '1-7515585-5807031.jpg'
        self.PIC_URL = 'fc07.deviantart.net/fs70/f/2013/209/7/a/have_a_nice_day_by_slawa-d6elhdw.jpg'

        USEREMAIL = 'ftest12@tech-mail.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        super(TestWithAuth, self).setUp()
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
        auth_form.wait_for_redirect()


class BasicTest(TestWithAuth):
    def tearDown(self):
        blog_page = BlogPage(self.driver)
        blog_page.topic.delete()
        super(BasicTest, self).tearDown()