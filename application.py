from selenium import webdriver

__author__ = 'Max'


class Application:

    def __init__(self):
        self.app = webdriver.Chrome()

    def make_screenshot(self, path):
        wd = self.app
        wd.save_screenshot(path)

    def go_to_main_page(self):
        wd = self.app
        wd.get('http://the-internet.herokuapp.com/')

    def find_form_autotification(self):
        wd = self.app
        wd.find_element_by_link_text('Form Authentication').click()

    def find_submit_button(self):
        wd = self.app
        wd.find_element_by_css_selector('button.radius').click()

    def check_error_for_novalid_fill_form(self):
        wd = self.app
        assert wd.find_element_by_css_selector('a.close').is_displayed()

    def fill_login_form(self, login, password):
        wd = self.app
        wd.find_element_by_id('username').click()
        wd.find_element_by_id('username').clear()
        wd.find_element_by_id("username").send_keys(login)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id('password').clear()
        wd.find_element_by_id('password').send_keys(password)

    def destroy(self):
        wd = self.app
        wd.quit()