# -*- coding: utf-8 -*-

from page_object import *

from basic_test import Test

class SimpleTest(Test):

    def test(self):
        BLOG = 'Флудилка'
        TITLE = u'MyTopic'
        MAIN_TEXT = u'Мой текст'

        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        self.assertEqual(TITLE,topic_title)
        self.assertEqual(MAIN_TEXT,topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(TITLE,topic_title)
        self.assertEqual(MAIN_TEXT,topic_text)

        blog_page.topic.delete()
        topic_title = blog_page.topic.get_title()
        # topic_text = blog_page.topic.get_text()
        self.assertNotEqual(TITLE,topic_title)
        # self.assertNotEqual(MAIN_TEXT,topic_text)
