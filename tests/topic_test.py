# -*- coding: utf-8 -*-

from page_object import *

from basic_test import TestWithAuth, BasicTest

class TopicDeleteTestCase(TestWithAuth):

    def testDeletion(self):

        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        blog_page.topic.delete()

        topic_title = blog_page.topic.get_title()
        self.assertNotEqual(self.TITLE,topic_title)


class TopicMainTestCase(BasicTest):

    def testSimpleCreation(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

    def testNoBlogSelected(self):
        ERROR_MSG = u'Блог'
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        error_text = create_form.get_error_text()

        self.assertIn(ERROR_MSG, error_text)

    def testNoTitle(self):
        ERROR_MSG = u'Заголовок'
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        error_text = create_form.get_error_text()

        self.assertIn(ERROR_MSG, error_text)

    def testNoText(self):
        ERROR_MSG = u'Текст'
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.submit()

        error_text = create_form.get_error_text()

        self.assertIn(ERROR_MSG, error_text)

    def testMarkH4(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_h4()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<h4>'+self.MAIN_TEXT+'</h4>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkH5(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_h5()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<h5>'+self.MAIN_TEXT+'</h5>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkH6(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_h6()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<h6>'+self.MAIN_TEXT+'</h6>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkBold(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_bold()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<strong>'+self.MAIN_TEXT+'</strong>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkItalic(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_italic()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<em>'+self.MAIN_TEXT+'</em>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkStroke(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_stroke()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<s>'+self.MAIN_TEXT+'</s>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkUnderline(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_underline()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<u>'+self.MAIN_TEXT+'</u>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkQuote(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.select_all_text()
        create_form.mark_quote()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<blockquote>'+self.MAIN_TEXT+'</blockquote>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkCode(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_code()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<code>'+self.MAIN_TEXT+'</code>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testMarkUl(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_ul()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_ul_text()
        self.assertIsNotNone(topic_text)
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_ul_text()
        self.assertIsNotNone(topic_text)
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

    def testMarkOl(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.mark_ol()
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_ol_text()
        self.assertIsNotNone(topic_text)
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_ol_text()
        self.assertIsNotNone(topic_text)
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)

    def testAddLink(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_link(self.LINK_ADDR, self.LINK_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = '<a href="'+self.LINK_ADDR+'">'+self.LINK_TEXT+'</a>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testAddUser(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_user(self.USER_ADD)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        expected_text = u'<a href="/profile/dm.kotegov/">Дмитрий Котегов</a>'
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(expected_text, topic_text)

    def testAddPicture(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_pc(self.PATH_TO_PIC)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture())

    def testAddPictureLeft(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_pc(self.PATH_TO_PIC, align='left')
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture(align='left'))

    def testAddPictureRight(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_pc(self.PATH_TO_PIC, align='right')
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture(align='right'))

    def testAddPictureCenter(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_pc(self.PATH_TO_PIC, align='center')
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture(align='center'))

    def testAddPictureWithText(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        img_title = self.createRandomText('Img title')
        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_pc(self.PATH_TO_PIC, text=img_title)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture(text=img_title))

    def testAddPictureByUrl_Upload(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_web(self.PIC_URL, upload=True)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture())

    def testAddPictureByUrl_Link(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.add_picture_from_web(self.PIC_URL, upload=False)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.has_picture())

    def testDraft(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.set_draft()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.is_draft())

    def testDisableComments(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.disable_comments()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.are_comments_disabled())

# this test checks nothing: polls are broken at the forum
    def testAddPoll(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.add_poll('dsgg',['gfsdgdf','sdgsdg'])
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertTrue(topic_page.topic.is_poll_exist())

    def testAddTopicByClicks(self):
        main_page = MainPage(self.driver)
        main_page.top_menu.open_topic_creation()

        create_form = main_page.create_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertIn(self.MAIN_TEXT, topic_text)