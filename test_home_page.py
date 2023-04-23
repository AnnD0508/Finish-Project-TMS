from home_page import HomePage
from cart_page import CartPage
from catalog_page import ProductCatalogPage


class Test_Web_Site:
    def test_displaying_links_and_buttons_on_the_home_page(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        assert home_page.is_catalog_menu_displayed()
        assert home_page.is_logo_displayed()
        assert home_page.is_search_button_displayed()
        assert home_page.is_search_field_displayed()
        assert home_page.is_cart_button_displayed()
        assert home_page.is_link_account_displayed()
        assert home_page.is_link_to_ask_a_question_displayed

    def test_all_elements_products_catalog_is_clickable(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.is_catalog_menu_displayed()
        home_page.go_to_categories_menu()
        catalog_page = ProductCatalogPage(browser)
        catalog_page.open()
        catalog_page.page_is_loaded()
        catalog_page.check_catalog_elements_is_clicable()

    def test_cart_page_is_empty(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        home_page.go_to_cart()
        cart_page = CartPage(browser)
        cart_page.open()
        cart_page.page_is_loaded()
        assert cart_page.cart_is_empty() is True
