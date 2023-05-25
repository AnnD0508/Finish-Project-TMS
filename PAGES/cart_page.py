from selenium.webdriver.common.by import By
from selenium import webdriver
from BASE_PAGE.base_page import BasePage
import time


class CartLocators(BasePage):
    url_cart = 'https://babydream.by/cart'
    cart_is_empty = (By.XPATH, '//div[@class="cabinet-cart"]//span[@class="items cartCountGoods"]')
    return_to_catalog_button = (By.XPATH, "//div[@class='col-left']//a[@href='/catalog']")
    button_remove = (
        By.XPATH, "//div/a[@class='remove-product deleteFromCartLink'][@href='/deleteCartGood?id=17822%3A0']")
    button_plus_product = (By.XPATH, "//div[@class='jq-number__spin plus']")
    button_minus_product = (By.XPATH, "//div[@class='jq-number__spin minus']")
    checkout_buton = (By.XPATH, "//div[@class='box-btn']/a[@href='/order']")
    product1_in_cart = (By.XPATH,
                        "//div/a[@href='/igrushki/plyushevie_medvedi/myagkaya_plyushevaya_igrushka_medved_sunrain_martin_120_chaynaya_roza']")
    product2_in_cart = (By.XPATH,
                        "//div/a[@href='/haggi_vaggi__huggy_wuggy/myagkaya_igrushka_sunrain_hagi_vagi_i_kisi_misi_25sm_korichneviy']")
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

    def get_cart_product_params(self, locator):
        name = self.get_text_from_element(locator)
        price = self.get_text_from_element((locator[0], locator[1] + '/../../../../../div[2]/div/span'))
        quantity = self.find_element(
            (locator[0], locator[1] + '/../../../../../div[3]//input[@class="updateQtyInput"]')).get_attribute('value')
        total = self.get_text_from_element((locator[0], locator[1] + '/../../../../../div[4]/div/span'))
        return {"name": name, "price": price, "quantity": quantity, "total": total}

    def contains_cart_product_after_add(self):
        cart_products = [
            self.get_cart_product_params(CartLocators.product1_in_cart),
            self.get_cart_product_params(CartLocators.product2_in_cart)
        ]
        expected_products = [
            {"name": 'Мягкая плюшевая игрушка Медведь SunRain Мартин 120 Чайная роза', "price": '82', "quantity": '1'},
            {"name": 'Мягкая игрушка SunRain Хаги Ваги и Киси Миси 25см Коричневый', "price": '11', "quantity": '1'}
        ]
        i = 0
        for cart_product in cart_products:
            assert cart_product['name'] == expected_products[i]['name']
            assert cart_product['price'] == expected_products[i]['price']
            assert cart_product['quantity'] == expected_products[i]['quantity']
            i = i + 1

    def the_total_amount_corresponds(self):
        cart_products = [
            self.get_cart_product_params(CartLocators.product1_in_cart),
            self.get_cart_product_params(CartLocators.product2_in_cart)
        ]
        test_products = [
            {"price": '82', "quantity": '1'},
            {"price": '11', "quantity": '1'}
        ]
        expected_total_price = 0
        i = 0
        for cart_product in cart_products:
            assert cart_product['price'] == test_products[i]['price']
            assert cart_product['quantity'] == test_products[i]['quantity']
            expected_total_price += float(cart_product['price']) * int(cart_product['quantity'])
            i += 1
        actual_total_price = float(self.get_text_from_element(CartLocators.total_price))
        assert expected_total_price == actual_total_price, f"Expected total price {expected_total_price}, but got {actual_total_price}."

    def add_quantity(self):
        self.click_element(CartLocators.button_plus_product, 2)
        time.sleep(2)
        return

    def change_quantity_add_product_in_cart(self):
        before_quantity = self.get_cart_product_params(CartLocators.product2_in_cart)['quantity']
        self.click_element(CartLocators.button_plus_product)
        after_add_quantity = self.get_cart_product_params(CartLocators.product2_in_cart)['quantity']
        assert after_add_quantity == str(
            int(before_quantity) + 1), f"Expected quantity to be {int(before_quantity) + 1}, but got {after_add_quantity}."

    def reduce_the_amount_of(self):
        before_quantity = self.get_cart_product_params(CartLocators.product2_in_cart)['quantity']
        self.click_element(CartLocators.button_minus_product)
        after_reduce_quantity = self.get_cart_product_params(CartLocators.product2_in_cart)['quantity']
        assert after_reduce_quantity == str(
            int(before_quantity) -1 ), f"Expected quantity to be {int(before_quantity) + 1}, but got {after_reduce_quantity}."

    def remove_product_from_cart(self):
        return self.find_element(CartLocators.button_remove)

    def go_from_cart_to_home(self):
        self.click_element(CartLocators.return_to_home)

    def go_from_cart_to_catalog(self):
        self.click_element(CartLocators.return_to_catalog_button)

    def go_to_order_form_page(self):
        self.click_element(CartLocators.checkout_buton)
