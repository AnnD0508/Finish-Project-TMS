from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage

class CheckoutLocators(BasePage):
    url_checkout = 'https://babydream.by/order'
    ordering_field_name = (By.XPATH, "//div/input[@name='Order[name]']")
    ordering_field_email = (By.XPATH, "//div/input[@name='Order[email]']")
    ordering_field_phone_number = (By.XPATH, "//div/input[@name='Order[phone]']")
    ordering_field_delivery_method = (By.XPATH, "//div/div[@class='jq-selectbox__select-text'][text()='Самовывоз']")
    ordering_field_adresse = (By.XPATH, "//div/input[@name='Order[city]']")
    ordering_field_payment_type= (By.XPATH, "//div/div[@class='jq-selectbox__select-text'][text()='Оплата наличными']")
    checkout_button = (By.XPATH, "//div/a[@class='btn'][@href='/order']")
    message_about_successful_ordering  = (By.XPATH, "//div/h3[@class='title'][text()='Ваш заказ успешно оформлен']")
    button_continue_shopping = (By.XPATH, "//div/a[@class='btn'][@href ='/catalog']")

class CheckoutPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = CheckoutLocators.url_checkout
        self.webdriver.get(self.url)
