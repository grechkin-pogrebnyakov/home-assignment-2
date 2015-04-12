# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

__author__ = 'serg'


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def wait_for_redirect(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.title_is(u"Технопарк@Mail.ru")
        )


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'
    CREATE_BUTTON = '//a[@id="modal_write_show"]'
    CREATE_TOPIC_BUTTON = '//a[@href="/blog/topic/create/"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )

    def open_topic_creation(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()
        WebDriverWait(self.driver, 30, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.CREATE_TOPIC_BUTTON)))
        self.driver.find_element_by_xpath(self.CREATE_TOPIC_BUTTON).click()



class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'
    ERROR_MSG = '//ul[@class="system-message-error"]'
    H4_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[1]/a'
    H5_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[2]/a'
    H6_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[3]/a'
    BOLD_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[5]/a'
    ITALIC_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[6]/a'
    STROKE_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[7]/a'
    UNDERLINE_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[8]/a'
    QUOTE_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[9]/a'
    CODE_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[10]/a'
    UL_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[12]/a'
    OL_MARK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[13]/a'
    ADD_LINK = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[16]/a'
    ADD_USER = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[17]/a'
    USER_INPUT = '//input[@id="search-user-login-popup"]'
    USER_CHOOSE = '//*[@id="list-body"]/tr[1]/td/div/p[2]/a'
    ADD_PICTURE = '//*[@id="markItUpId_text"]/div/div[1]/ul/li[15]/a'
    PICTURE_PATH_SELECTOR = '//input[@id="img_file"]'
    PICTURE_URL_SELECTOR = '//input[@id="img_url"]'
    PICTURE_SUBMIT = '//button[@id="submit-image-upload"]'
    OVERLAY = '//div[@class="jqmOverlay"]'
    IMG_ALIGN = '//select[@id="form-image-align"]'
    IMG_OPTION = '//option[@value=""]'
    IMG_TITLE = '//input[@id="form-image-title"]'
    PICTURE_BY_URL = '//a[contains(text(),"Из интернета")]'
    PICTURE_SUBMIT_LINK = '//button[@id="submit-image-upload-link"]'
    PICTURE_SUBMIT_UPLOAD = '//button[@id="submit-image-upload-link-upload"]'
    PUBLISH = '//input[@id="id_publish"]'
    DISABLE_COMMENTS = '//input[@id="id_forbid_comment"]'
    ADD_POLL = '//input[@name="add_poll"]'
    POLL_QUESTION = '//input[@id="id_question"]'
    POLL_ANSWER = '//input[@id="id_form-{}-answer"]'
    ADD_POLL_ANSWER = '//a[@class="add-poll-answer link-dotted"]'

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_title(self,title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_main_text(self,main_text):
        self.driver.find_element_by_xpath(self.TEXT).send_keys(main_text)

    def submit(self):
        WebDriverWait(self.driver, 30, 0.1).until(EC.invisibility_of_element_located((By.XPATH, self.OVERLAY)))
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()

    def get_error_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ERROR_MSG).text
        )
    def select_all_text(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    def mark_h4(self):
        self.driver.find_element_by_xpath(self.H4_MARK).click()

    def mark_h5(self):
        self.driver.find_element_by_xpath(self.H5_MARK).click()

    def mark_h6(self):
        self.driver.find_element_by_xpath(self.H6_MARK).click()

    def mark_bold(self):
        self.driver.find_element_by_xpath(self.BOLD_MARK).click()

    def mark_italic(self):
        self.driver.find_element_by_xpath(self.ITALIC_MARK).click()

    def mark_stroke(self):
        self.driver.find_element_by_xpath(self.STROKE_MARK).click()

    def mark_underline(self):
        self.driver.find_element_by_xpath(self.UNDERLINE_MARK).click()

    def mark_quote(self):
        self.driver.find_element_by_xpath(self.QUOTE_MARK).click()

    def mark_code(self):
        self.driver.find_element_by_xpath(self.CODE_MARK).click()

    def mark_ul(self):
        self.driver.find_element_by_xpath(self.UL_MARK).click()

    def mark_ol(self):
        self.driver.find_element_by_xpath(self.OL_MARK).click()

    def add_link(self, addr, text):
        self.driver.find_element_by_xpath(self.ADD_LINK).click()
        WebDriverWait(self.driver, 30, 0.1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(addr)
        alert.accept()
        ActionChains(self.driver).send_keys(text).perform()

    def add_user(self, user_name):
        self.driver.find_element_by_xpath(self.ADD_USER).click()
        self.driver.find_element_by_xpath(self.USER_INPUT).send_keys(user_name)
        WebDriverWait(self.driver, 30, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.USER_CHOOSE)))
        self.driver.find_element_by_xpath(self.USER_CHOOSE).click()

    def img_align_select_open(self):
        self.driver.find_element_by_xpath(self.IMG_ALIGN).click()

    def img_align_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def add_picture_from_pc(self, path, align=None, text=None):
        self.driver.find_element_by_xpath(self.ADD_PICTURE).click()
        self.driver.find_element_by_xpath(self.PICTURE_PATH_SELECTOR).send_keys(path)
        if align:
            Select(self.driver.find_element_by_xpath(self.IMG_ALIGN)).select_by_value(align)
        if text:
            self.driver.find_element_by_xpath(self.IMG_TITLE).send_keys(text)
        self.driver.find_element_by_xpath(self.PICTURE_SUBMIT).click()

    def add_picture_from_web(self, url, align=None, text=None, upload=False):
        self.driver.find_element_by_xpath(self.ADD_PICTURE).click()
        self.driver.find_element_by_xpath(self.PICTURE_BY_URL).click()
        self.driver.find_element_by_xpath(self.PICTURE_URL_SELECTOR).send_keys(url)
        if align:
            Select(self.driver.find_element_by_xpath(self.IMG_ALIGN)).select_by_value(align)
        if text:
            self.driver.find_element_by_xpath(self.IMG_TITLE).send_keys(text)
        if upload:
            self.driver.find_element_by_xpath(self.PICTURE_SUBMIT_UPLOAD).click()
        else:
            self.driver.find_element_by_xpath(self.PICTURE_SUBMIT_LINK).click()

    def set_draft(self):
        self.driver.find_element_by_xpath(self.PUBLISH).click()

    def disable_comments(self):
        self.driver.find_element_by_xpath(self.DISABLE_COMMENTS).click()

    def add_poll(self, question, answers):
        self.driver.find_element_by_xpath(self.ADD_POLL).click()
        self.driver.find_element_by_xpath(self.POLL_QUESTION).send_keys(question)
        for i in range(0, len(answers), 1):
            if i > 1:
                self.driver.find_element_by_xpath(self.ADD_POLL_ANSWER).click()
            self.driver.find_element_by_xpath(self.POLL_ANSWER.format(i.__str__())).send_keys(answers[i])


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//div[@class="topic-content text"]'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'
    UL_LOCATION = '//div[@class="topic-content text"]/ul/li'
    OL_LOCATION = '//div[@class="topic-content text"]/ol/li'
    IMAGE_TAG = '//div[@class="topic-content text"]/img'
    DRAFT = '//i[@class="icon-synio-topic-draft"]'
    COMMENTS = '//h4[@class="reply-header"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_ul_text(self):
        try:
            return self.driver.find_element_by_xpath(self.UL_LOCATION).text
        except NoSuchElementException:
            return None

    def get_ol_text(self):
        try:
            return self.driver.find_element_by_xpath(self.OL_LOCATION).text
        except NoSuchElementException:
            return None

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT).get_attribute("innerHTML")
        )

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        try:
            self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
            self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()
        except NoSuchElementException:
            pass

    def has_picture(self, align=None, text=None):
        try:
            image = self.driver.find_element_by_xpath(self.IMAGE_TAG)
            if image.is_enabled():
                result = True
                if align:
                    result = (align == image.get_attribute('align'))
                if result and text:
                    result = (text == image.get_attribute('title'))
                return result
            return False
        except NoSuchElementException:
            return False

    def is_draft(self):
        try:
            return self.driver.find_element_by_xpath(self.DRAFT).is_enabled()
        except NoSuchElementException:
            return False

    def are_comments_disabled(self):
        try:
            return not self.driver.find_element_by_xpath(self.COMMENTS).is_enabled()
        except NoSuchElementException:
            return True

    def is_poll_exist(self):
        return True