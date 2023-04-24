from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage


class LoginLocators(BasePage):
    url_login = 'https://babydream.by/login'
    url_user_cabinet = 'https://babydream.by/cabinet'
    button_register = (By.XPATH, "//div/a[@href='/registration']")
    field_register_name = (By.XPATH, "//div/input[@name='User[name]']")
    field_register_last_name = (By.XPATH, "//div/input[@name='User[surname]']")
    field_register_phone = (By.XPATH, "//div/input[@name='User[phone]']")
    field_register_email = (By.XPATH, "//div/input[@name='User[email]']")
    field_register_password_confirmation = (By.XPATH, "//div/input[@name='User[repeat_password]']")
    checkbox_not_robot = (By.XPATH, "//div/span/div[@class='recaptcha-checkbox-border']")
    button_clic_register = (By.XPATH, "//div/button[@type='submit']/span[text()='Зарегистрироваться']")
    message_field_register_empti = (By.XPATH, "//div[@id='User_email_em_']")
    autorisation_email = (By.XPATH, "//div/input[@id='LoginForm_username']")
    autorisation_password = (By.XPATH, "//input[@id='LoginForm_password']")
    autorisation_checkbox_not_robot = (By.XPATH, '//form[@id="login-form"]//iframe[@title="reCAPTCHA"]')
    email_is_incomplete_message = (By.XPATH, "//div[@class='errorMessage'][text()='Необходимо заполнить поле E-mail.']")
    password_is_incomlete_message = (By.XPATH, "//div[@class='errorMessage'][text()='Не верный логин или пароль']")
    button_to_came_in = (By.XPATH, "//div/button[@type='submit']/span[text()='Войти']")
    button_cabinet_user = (By.XPATH, "//div[@class='user-menu dropdown']/a[@href='#']")
    button_my_account = (By.XPATH, '//ul[@class="dropdown-menu"]/li[1]/a')


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = LoginLocators.url_login
        self.webdriver.get(self.url)

    def input_password(self):
        password = '123456789'
        self.send_keys(LoginLocators.autorisation_password, password)

    def click_element_robot(self, timer=10):
        self.click_element(LoginLocators.autorisation_checkbox_not_robot)

    def click_button_came_in(self, timer=10):
        self.click_element(LoginLocators.button_to_came_in)

    def email_is_empty(self):
        assert self.get_text_from_element(
            LoginLocators.email_is_incomplete_message) == 'Необходимо заполнить поле E-mail'

    def input_email_password_unregistered_user(self):
        email = '3826347@mail.ru'
        password = '123456789'
        self.send_keys(LoginLocators.autorisation_email, email)
        self.send_keys(LoginLocators.autorisation_password, password)

    def message_about_invalid_input(self):
        assert self.get_text_from_element(LoginLocators.password_is_incomlete_message) == 'Не верный логин или пароль'

    def entering_data_of_a_registered_user(self):
        email = '5555555@gmail.com'
        password = '123456789'
        self.send_keys(LoginLocators.autorisation_email, email)
        self.send_keys(LoginLocators.autorisation_password, password)

    def click_button_cabinet_user(self):
        self.click_element(LoginLocators.button_cabinet_user)
        self.click_element(LoginLocators.button_my_account)

    def user_cabinet_is_excepted(self):
        assert self.webdriver.current_url == LoginLocators.url_user_cabinet

    def entering_an_incorrect_registered_user_password(self):
        email = '5555555@gmail.com'
        password = '12345678'
        self.send_keys(LoginLocators.autorisation_email, email)
        self.send_keys(LoginLocators.autorisation_password, password)
