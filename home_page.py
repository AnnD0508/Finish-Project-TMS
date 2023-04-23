from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage
from selenium.webdriver import ActionChains


class HomeLocators(BasePage):
    url_home = 'https://babydream.by/'
    logo = (By.XPATH, "//a[@class='logo']")
    search_field = (By.XPATH, "//input[@class='siteSearch sb-search-input ui-autocomplete-input']")
    search_submit = (By.XPATH, "//input[@class='sb-search-submit']")
    search_button = (By.XPATH, "//span[@class='icon-search']")
    search_results = (By.XPATH, '//div[@class="items"]/div[@class="item"]//a[@class="title"]')
    catalog_menu = (By.XPATH, "//li/a[@class='catalog']")
    category_kachalki = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/igrushki/kachalki"]')
    category_kukli = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/igrushki/kukli_pupsi]')
    category_igrovaya_mebel = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/mebel_dlya_detskoy/igrovaya_mebel"]')
    cart_button = (By.XPATH, "//div[@class='cabinet-cart']/div[@class='cart']/a[@class='cart']")
    items_to_compare = (By.XPATH, "//div[@class='box-compare']/a[@class]")
    account_button = (By.XPATH, "//a[@class='login']")
    link_to_ask_a_question = (By.XPATH, "//div[@class='block block-help']/div/div/a[@data-target='#modalFeedback']")
    feedback_form = (By.XPATH, "//div[@class='modal-content']/div/form[@id='feedback-form']")


class HomePage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = HomeLocators.url_home
        self.webdriver.get(self.url)
    def is_catalog_menu_displayed(self):
        return self.find_element(HomeLocators.catalog_menu)
    def is_logo_displayed(self):
        return self.find_element(HomeLocators.logo)
    def is_search_button_displayed(self):
        return self.find_element(HomeLocators.search_button)
        self.click_element(HomeLocators.search_button)
    def is_search_field_displayed(self):
        return self.find_element(HomeLocators.search_field)
    def is_cart_button_displayed(self):
        return self.find_element(HomeLocators.cart_button)
    def is_link_account_displayed(self):
        return self.find_element(HomeLocators.account_button)
    def is_link_to_ask_a_question_displayed(self, url):
        return self.find_element(HomeLocators.link_to_ask_a_question)

