from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string


class LoginLocators(BasePage):
    url_login = 'https://babydream.by/login'
    url_user_cabinet = 'https://babydream.by/cabinet'
    button_register = (By.XPATH, "//div/a[@href='/registration']")
    field_register_name = (By.XPATH, "//div/input[@name='User[name]']")
    field_register_last_name = (By.XPATH, "//div/input[@name='User[surname]']")
    field_register_phone = (By.XPATH, "//div/input[@name='User[phone]']")
    field_register_email = (By.XPATH, "//div/input[@name='User[email]']")
    field_register_password = (By.XPATH, "//div/input[@name='User[password]']")
    field_register_password_confirmation = (By.XPATH, "//div/input[@name='User[repeat_password]']")
    checkbox_not_robot = (By.XPATH, '//form[@id="registration-form"]//iframe[@title="reCAPTCHA"]')
    button_clic_register = (By.XPATH, "//div/button[@class='btn orange']")
    message_password_less_than_three_characters = (By.XPATH, "//div[text()='Пароль слишком короткий (Минимум: 6 симв.).']")
    message_field_name_is_empty = (By.XPATH, "//div[text()='Необходимо заполнить поле Имя, Фамилия.']")
    message_field_phone_is_empty = (By.XPATH, "//div[text()='Необходимо заполнить поле Телефон.']")
    message_field_register_is_email_empty = (By.XPATH, "//div[text()='Необходимо заполнить поле E-mail.']")
    message_field_filling_is_not_correct = (By.XPATH, "//div[text()='E-mail не является правильным E-Mail адресом.']")
    message_password_confirmation_is_not_correct = (By.XPATH, "//div[text() = 'Подтвердите пароль должен быть повторен в точности.']")
    message_email_is_already_busy = (By.XPATH, '//div[text()=\'E-mail "3333333@mail.ru" уже занят.\']')
    autorisation_email = (By.XPATH, "//div/input[@id='LoginForm_username']")
    autorisation_password = (By.XPATH, "//input[@id='LoginForm_password']")
    autorisation_checkbox_not_robot = (By.XPATH, '//form[@id="login-form"]//iframe[@title="reCAPTCHA"]')
    email_is_incomplete_message = (By.XPATH, "//div[@class='errorMessage'][text()='Необходимо заполнить поле E-mail.']")
    password_is_incomplete_message = (By.XPATH, "//div[@class='errorMessage'][text()='Не верный логин или пароль']")
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
        assert self.get_text_from_element(LoginLocators.password_is_incomplete_message) == 'Не верный логин или пароль'

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

    def click_button_register(self, timer=10):
        self.click_element(LoginLocators.button_register)

    def generate_email(self, length=10):
        username = ''.join(random.choices(string.ascii_lowercase, k=length))
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com"]
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        return email

    def user_registration_password_entry_less_than_three_characters(self):
        name = 'Ilon'
        last_name = 'Mask'
        phone = '+375297777777'
        email = self.generate_email()
        password = '123'
        self.send_keys(LoginLocators.field_register_name, name)
        self.send_keys(LoginLocators.field_register_last_name, last_name)
        self.send_keys(LoginLocators.field_register_phone, phone)
        self.send_keys(LoginLocators.field_register_email, email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.click_element(LoginLocators.field_register_password_confirmation)
        assert self.get_text_from_element(
            LoginLocators.message_password_less_than_three_characters) == 'Пароль слишком короткий (Минимум: 6 симв.).'

    def user_registration_without_filling_name(self):
        last_name = 'Mask'
        phone = '+375257777777'
        email = self.generate_email()
        password = '12345678'
        self.click_element(LoginLocators.field_register_name)
        self.send_keys(LoginLocators. field_register_last_name, last_name)
        self.send_keys(LoginLocators.field_register_phone, phone)
        self.send_keys(LoginLocators.field_register_email, email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.send_keys(LoginLocators.field_register_password_confirmation, password)
        assert self.get_text_from_element(LoginLocators.message_field_name_is_empty) == 'Необходимо заполнить поле Имя, Фамилия.'

    def user_registration_without_filling_email(self):
        name = 'Ilon'
        last_name = 'Mask'
        phone = '+375257777777'
        password = '12345678'
        self.send_keys(LoginLocators.field_register_name, name)
        self.send_keys(LoginLocators.field_register_last_name, last_name)
        self.send_keys(LoginLocators.field_register_phone, phone)
        self.click_element(LoginLocators.field_register_email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.send_keys(LoginLocators.field_register_password_confirmation, password)
        assert self.get_text_from_element(LoginLocators. message_field_register_is_email_empty) == 'Необходимо заполнить поле E-mail.'

    def user_registration_filling_email_is_not_correct(self):
        name = 'Ilon'
        last_name = 'Mask'
        phone = '+375257777777'
        email = '12345678mail.ru'
        password = '12345678'
        self.send_keys(LoginLocators.field_register_name, name)
        self.send_keys(LoginLocators.field_register_last_name, last_name)
        self.send_keys(LoginLocators.field_register_phone, phone)
        self.send_keys(LoginLocators.field_register_email, email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.send_keys(LoginLocators.field_register_password_confirmation, password)
        assert self.get_text_from_element(LoginLocators.message_field_filling_is_not_correct) == 'E-mail не является правильным E-Mail адресом.'

    def user_registration_without_filling_phone(self):
        name = 'Ilon'
        last_name = 'Mask'
        email = self.generate_email()
        password = '12345678'
        self.send_keys(LoginLocators.field_register_name, name)
        self.send_keys(LoginLocators. field_register_last_name, last_name)
        self.click_element(LoginLocators.field_register_phone)
        self.send_keys(LoginLocators.field_register_email, email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.send_keys(LoginLocators.field_register_password_confirmation, password)
        assert self.get_text_from_element(LoginLocators.message_field_phone_is_empty) == 'Необходимо заполнить поле Телефон.'

    def user_registration_password_confirmation_is_not_correct(self):
        name = 'Ilon'
        last_name = 'Mask'
        phone = '+375257777777'
        email = self.generate_email()
        password = '12345678'
        password_confirmation = '123456789'
        self.send_keys(LoginLocators.field_register_name, name)
        self.send_keys(LoginLocators.field_register_last_name, last_name)
        self.send_keys(LoginLocators.field_register_phone, phone)
        self.send_keys(LoginLocators.field_register_email, email)
        self.send_keys(LoginLocators.field_register_password, password)
        self.send_keys(LoginLocators.field_register_password_confirmation, password_confirmation)
        self.click_element(LoginLocators.field_register_password)
        assert self.get_text_from_element(
            LoginLocators.message_password_confirmation_is_not_correct) == 'Подтвердите пароль должен быть повторен в точности.'
