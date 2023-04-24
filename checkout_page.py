from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage
import random
import string

class CheckoutLocators(BasePage):
    url_checkout = 'https://babydream.by/order'
    ordering_field_name = (By.XPATH, "//div/input[@name='Order[name]']")
    ordering_field_email = (By.XPATH, "//div/input[@name='Order[email]']")
    ordering_field_phone_number = (By.XPATH, "//div/input[@name='Order[phone]']")
    ordering_field_delivery_method = (By.XPATH, "//div/div[@class='jq-selectbox__select-text'][text()='Самовывоз']")
    ordering_field_adresse = (By.XPATH, "//div/input[@name='Order[city]']")
    ordering_field_payment_type = (By.XPATH, "//div/div[@class='jq-selectbox__select-text'][text()='Оплата наличными']")
    checkout_button = (By.XPATH, "//div/button[@class='btn buttonMakeOrder']")
    message_about_successful_ordering = (By.XPATH, "//div/h3[@class='title'][text()='Ваш заказ успешно оформлен']")
    button_continue_shopping = (By.XPATH, "//div/a[@class='btn'][@href ='/catalog']")
    message_ordering_field_name = (By.XPATH, "//div[@class='errorMessage'][text()='Необходимо заполнить поле Имя.']")
    message_ordering_field_email = (By.XPATH, "//div[@class='errorMessage'][text()='Необходимо заполнить поле E-mail.']")
    message_ordering_field_phone_number = (By.XPATH, "//div[@class='errorMessage'][text()='Необходимо заполнить поле Телефон.']")

class CheckoutPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = CheckoutLocators.url_checkout
        self.webdriver.get(self.url)

    def generate_email(self, length=10):
        username = ''.join(random.choices(string.ascii_lowercase, k=length))
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com"]
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        return email

    def date_input_user_unregistrated(self):
        name = 'Marfa'
        email = self.generate_email()
        phone = '+375257777777'
        self.send_keys(CheckoutLocators.ordering_field_name, name)
        self.send_keys(CheckoutLocators.ordering_field_email, email)
        self.send_keys(CheckoutLocators.ordering_field_phone_number, phone)
        self.click_element(CheckoutLocators.ordering_field_delivery_method)
        self.click_element(CheckoutLocators.ordering_field_adresse)
        self.click_element(CheckoutLocators.checkout_button)
        assert self.get_text_from_element(CheckoutLocators.message_about_successful_ordering) == 'Ваш заказ успешно оформлен'

    def date_input_user_unregistrated(self):
        name = 'Marfa'
        email = self.generate_email()
        phone = '+375257777777'
        self.send_keys(CheckoutLocators.ordering_field_name, name)
        self.send_keys(CheckoutLocators.ordering_field_email, email)
        self.send_keys(CheckoutLocators.ordering_field_phone_number, phone)
        self.click_element(CheckoutLocators.ordering_field_delivery_method)
        self.click_element(CheckoutLocators.ordering_field_adresse)
        self.click_element(CheckoutLocators.checkout_button)
        assert self.get_text_from_element(CheckoutLocators.message_about_successful_ordering) == 'Ваш заказ успешно оформлен'

    def attempt_to_place_an_order_without_filling_in_the_name(self):
        email = self.generate_email()
        phone = '+375257777777'
        self.send_keys(CheckoutLocators.ordering_field_email, email)
        self.send_keys(CheckoutLocators.ordering_field_phone_number, phone)
        self.click_element(CheckoutLocators.checkout_button)
        assert self.get_text_from_element(
            CheckoutLocators.message_ordering_field_name) == 'Необходимо заполнить поле Имя.'

        def attempt_to_place_an_order_without_filling_in_the_name(self):
            name = 'Marfa'
            phone = '+375257777777'
            self.send_keys(CheckoutLocators.ordering_field_name, name)
            self.send_keys(CheckoutLocators.ordering_field_phone_number, phone)
            self.click_element(CheckoutLocators.checkout_button)
            assert self.get_text_from_element(
                CheckoutLocators.message_ordering_field_name) == 'Необходимо заполнить поле E-mail.'
