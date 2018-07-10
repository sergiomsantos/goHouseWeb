from test_base import *

class TestLogin(TestBase):

    def setUp(self):
        TestBase.setUp(self)
        self.click_link('login-link')

    def test_login_location(self):
        endpoint = url_for('login')
        self.assertTrue(self.driver.current_url.endswith(endpoint))
    
    # def do_login(self, login, password):
    #     self.driver.find_element_by_id('email').send_keys(login)
    #     self.driver.find_element_by_id('password').send_keys(password)
    #     self.click_link('submit')

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
        self.click_link('index-link')
        endpoint = url_for('index')
        self.assertTrue(self.driver.current_url.endswith(endpoint))

    

if __name__ == '__main__':
    unittest.main()