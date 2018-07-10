import unittest
import urllib2
import time

from flask_testing import LiveServerTestCase
from selenium import webdriver
from flask import url_for

from webapp import app

RAND_EMAIL = 'rdnaodhkw82878e@mail.com'
RAND_PASSWORD = 'rdnaodhkw82878e'

TEST_EMAIL = 'tqs@mail.com'
TEST_PASSWORD = 'tqs'
TEST_USERNAME = 'tqs'

class TestBase(LiveServerTestCase):
    def create_app(self):
        return app
    
    def setUp(self):
        '''Setup the test driver and create test users'''

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    # def test_server_is_up_and_running(self):
    #     response = urllib2.urlopen(self.get_server_url())
    #     self.assertEqual(response.code, 200)
     


class TestLogin(TestBase):

    def head_to_login_page(self):
        self.driver.find_element_by_id('login-link').click()
        time.sleep(1)

    def do_login(self, login, password):
        self.head_to_login_page()

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()
        time.sleep(1)

    def test_login_location(self):
        self.head_to_login_page()
        endpoint = url_for('login')
        self.assertTrue(self.driver.current_url.endswith(endpoint))

    # def test_successfull_login(self):
    #     self.do_login(TEST_EMAIL, TEST_PASSWORD)
    #     header = self.driver.find_element_by_id('username-header').text
    #     self.assertIn(TEST_USERNAME, header)
    
    # def test_wrong_email(self):
    #     self.do_login(RAND_EMAIL, TEST_PASSWORD)
    #     alert_text = webdriver.common.alert.Alert(self.driver).text
    #     self.assertEqual('Wrong email/password', alert_text)
    
    # def test_wrong_password(self):
    #     self.do_login(TEST_EMAIL, RAND_PASSWORD)
    #     alert_text = webdriver.common.alert.Alert(self.driver).text
    #     self.assertEqual('Wrong email/password', alert_text)
    
    def test_go_index_on_click_gohouse(self):
        self.head_to_login_page()
        self.driver.find_element_by_id('index-link').click()
        time.sleep(1)
        endpoint = url_for('index')
        self.assertTrue(self.driver.current_url.endswith(endpoint))

    

if __name__ == '__main__':
    unittest.main()