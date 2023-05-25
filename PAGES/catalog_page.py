from selenium.webdriver.common.by import By
from selenium import webdriver
from BASE_PAGE.base_page import BasePage
from selenium.webdriver import ActionChains


class ProductCatalogLocators(BasePage):
    url_catalog = 'https://babydream.by/catalog'
    catalog_menu = (By.XPATH, "//li/a[@class='catalog']")
    selection1_of_toys_add_in_cart = (By.XPATH, "//div[@class='field-title']" 
        "/a[@href='/haggi_vaggi__huggy_wuggy/myagkaya_igrushka_sunrain_hagi_vagi_i_kisi_misi_25sm_korichneviy']")
    bay1_of_toys_button = (By.XPATH, "//div[@class='item']//a[@href='/addToCart?id=17822&color=']")
    selection2_of_toys_add_in_cart = (By.XPATH, "//div/a[@ href = '/igrushki/plyushevie_medvedi/myagkaya_plyushevaya_igrushka_medved_sunrain_martin_120_chaynaya_roza']")
    bay2_of_toys_button = (By.XPATH, "//div[@class='item']//a[@href='/addToCart?id=18050&color=']")
    cart_button = (By.XPATH, "//div[@class='cabinet-cart']/div[@class='cart']/a[@class='cart']")
    category_kachalki = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/igrushki/kachalki"]')
    category_kukli = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/igrushki/kukli_pupsi]')
    category_igrovaya_mebel = (By.XPATH, '//ul[@class="catalogue"]/li/a[@href="/mebel_dlya_detskoy/igrovaya_mebel"]')
    category = (By.XPATH, "//div[@class='block-catalog-category']//a[@href]")
    the_minimum_price_value = (By.XPATH, '//input[@id="amount1-1"]')
    the_maximum_price_value = (By.XPATH, '//input[@id="amount2-1"]')
    the_maximum_price_value_slider = (By.XPATH, '//a[@class="ui-slider-handle ui-state-default ui-corner-all"][2]')
    the_maximum_price_text_value = (By.XPATH, '//div[@id="amount2"]')
    button_filter = (By.XPATH, '//form[@class="default models"]//button')
    filter_product = (By.XPATH, "//div/div[@class='field-price']/div")

class ProductCatalogPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = ProductCatalogLocators.url_catalog
        self.webdriver.get(self.url)
    def go_to_cart(self):
        return self.find_element(ProductCatalogLocators.cart_button).click()

    def check_catalog_elements_is_clicable(self):
        categories_list = self.find_elements(ProductCatalogLocators.category)
        for category in categories_list:
            if not category.is_enabled() or not category.is_displayed():
                return False
        return True

    def add_to_cart_select_products(self):
        action = ActionChains(self.webdriver)
        action.move_to_element(self.find_element(ProductCatalogLocators.selection2_of_toys_add_in_cart)).perform()
        action.move_to_element(self.find_element(ProductCatalogLocators.bay2_of_toys_button)).perform()
        self.click_element(ProductCatalogLocators.bay2_of_toys_button)
        action.move_to_element(self.find_element(ProductCatalogLocators.selection1_of_toys_add_in_cart)).perform()
        action.move_to_element(self.find_element(ProductCatalogLocators.bay1_of_toys_button)).perform()
        self.click_element(ProductCatalogLocators.bay1_of_toys_button)

    def add_to_cart_select_product1(self):
        action = ActionChains(self.webdriver)
        action.move_to_element(self.find_element(ProductCatalogLocators.selection1_of_toys_add_in_cart)).perform()
        action.move_to_element(self.find_element(ProductCatalogLocators.bay1_of_toys_button)).perform()
        self.click_element(ProductCatalogLocators.bay1_of_toys_button)

    def setting_price_parameters(self):
        slider = self.find_element(ProductCatalogLocators.the_maximum_price_value_slider)
        max_slider_value = int(self.get_text_from_element(ProductCatalogLocators.the_maximum_price_text_value))
        action_chains = ActionChains(self.webdriver)
        while max_slider_value > 17:
            action_chains.drag_and_drop_by_offset(slider, -2, 0).perform()
            max_slider_value = int(self.get_text_from_element(ProductCatalogLocators.the_maximum_price_text_value))
        assert max_slider_value == 17


    def get_product_price(self, element):
        price = float(element.text.replace(' руб.', ''))
        return price

    def the_list_prise_after_filter(self):
        self.setting_price_parameters()
        products = self.find_elements(ProductCatalogLocators.filter_product)
        prices = []
        for product in products:
            price = self.get_product_price(product)
            prices.append(price)
        for price in prices:
            assert 0 <= price <= 17
    def click_button_filter(self):
        self.click_element(ProductCatalogLocators.button_filter)
