from flask_testing import LiveServerTestCase
from selenium import webdriver
from flask import url_for

from webapp import app

import unittest
import urllib2
import time

# non-registered user credentials
RAND_EMAIL = 'rdnaodhkw82878e@mail.com'
RAND_PASSWORD = 'rdnaodhkw82878e'

# registered user credentials
TEST_EMAIL = 'tqs@mail.com'
TEST_PASSWORD = 'tqs'
TEST_USERNAME = 'tqs'

# browser config options
# -> instruct to use a headless browser
HEADLESS = True

class TestBase(LiveServerTestCase):
    
    def create_app(self):
        return app
    
    def setUp(self):
        
        if HEADLESS:
            # HEADLESS BROWSER
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            chrome_options.add_argument('window-size=1920x1080')
            self.driver = webdriver.Chrome(options=chrome_options, port=7007)
        else:
            # HEADFULL BROWSER
            self.driver = webdriver.Chrome()
        
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
    
    def click_link(self, linkID):
        self.driver.find_element_by_id(linkID).click()
        time.sleep(1)


# # class TestLogin(TestBase):

# #     def setUp(self):
# #         TestBase.setUp(self)
# #         self.click_link('login-link')

# #     def do_login(self, login, password):
# #         self.driver.find_element_by_id('email').send_keys(login)
# #         self.driver.find_element_by_id('password').send_keys(password)
# #         self.click_link('submit')

# #     def test_login_location(self):
# #         endpoint = url_for('login')
# #         self.assertTrue(self.driver.current_url.endswith(endpoint))

# #     def test_successfull_login(self):
# #         self.do_login(TEST_EMAIL, TEST_PASSWORD)
# #         header = self.driver.find_element_by_id('username-header').text
# #         self.assertIn(TEST_USERNAME, header)
    
# #     def test_wrong_email(self):
# #         self.do_login(RAND_EMAIL, TEST_PASSWORD)
# #         alert_text = webdriver.common.alert.Alert(self.driver).text
# #         self.assertEqual('Wrong email/password', alert_text)
    
# #     def test_wrong_password(self):
# #         self.do_login(TEST_EMAIL, RAND_PASSWORD)
# #         alert_text = webdriver.common.alert.Alert(self.driver).text
# #         self.assertEqual('Wrong email/password', alert_text)
    
# #     def test_go_index_on_click_gohouse(self):
# #         self.click_link('index-link')
# #         endpoint = url_for('index')
# #         self.assertTrue(self.driver.current_url.endswith(endpoint))

    

if __name__ == '__main__':
    unittest.main()