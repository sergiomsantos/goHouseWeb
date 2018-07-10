from test_base import *

class TestRegister(TestBase):

    def setUp(self):
        TestBase.setUp(self)
        self.click_link('register-link')

    def test_register_location(self):
        endpoint = url_for('register')
        self.assertTrue(self.driver.current_url.endswith(endpoint))

    def test_go_index_on_click_gohouse(self):
        self.click_link('index-link')
        endpoint = url_for('index')
        self.assertTrue(self.driver.current_url.endswith(endpoint))

    

if __name__ == '__main__':
    unittest.main()