from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import BasePage

class CartLocators(BasePage):
    url_cart = 'https://babydream.by/cart'
    cart_is_empty = (By.XPATH, '//div[@class="cabinet-cart"]//span[@class="items cartCountGoods"]')
    return_to_catalog_button = (By.XPATH, "//div[@class='col-left']//a[@href='/catalog']")
    button_remove = (By.XPATH, "//div/a[@class='remove-product deleteFromCartLink'][@href='/deleteCartGood?id=17822%3A0']")
    button_plus_product = (By.XPATH, "//div[@class='jq-number__spin plus']")
    button_minus_product = (By.XPATH, "//div[@class='jq-number__spin minus']")
    checkout_buton = (By.XPATH, "//div[@class='box-btn']/a[@href='/order']")
    product1_in_cart = (By.XPATH, "//div/a[@href='/igrushki/plyushevie_medvedi/myagkaya_plyushevaya_igrushka_medved_sunrain_martin_120_chaynaya_roza']")
    product2_in_cart = (By.XPATH, "//div/a[@href='/haggi_vaggi__huggy_wuggy/myagkaya_igrushka_sunrain_hagi_vagi_i_kisi_misi_25sm_korichneviy']")
    total_price = (By.XPATH, "//div[@class='cart-total-price']//span[@class='total']")
    price1 = (By.XPATH, "//div[@class='td'][2]/div/span[@class='price'][text()=82]")
    price2 = (By.XPATH, "//div[@class='td'][4]/div/span[@class='price'][text()=82]")
    quantity1 = (By.XPATH, "//div/div[@class='jq-number__field'][1]")
    return_to_home = (By.XPATH, "//div/ol[@class='breadcrumb']//a[@href='/']")

class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = CartLocators.url_cart
        self.webdriver.get(self.url)
    def cart_is_empty(self) -> bool:
        return self.find_element(CartLocators.cart_is_empty).text == '0'
