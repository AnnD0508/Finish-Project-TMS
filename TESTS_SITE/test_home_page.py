import allure
import pytest
from PAGES.home_page import HomePage
from PAGES.cart_page import CartPage
from PAGES.catalog_page import ProductCatalogPage
from PAGES.checkout_page import CheckoutPage
from PAGES.login_page import LoginPage


class Test_Web_Site:
    @allure.feature("Home Page")
    @allure.story("Displaying links and buttons")
    def test_displaying_links_and_buttons_on_the_home_page(self, browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Check if catalog menu is displayed"):
            assert home_page.is_catalog_menu_displayed()
        with allure.step("Check if logo is displayed"):
            assert home_page.is_logo_displayed()
        with allure.step("Check if search button is displayed"):
            assert home_page.is_search_button_displayed()
        with allure.step("Check if search field is displayed"):
            assert home_page.is_search_field_displayed()
        with allure.step("Check if cart button is displayed"):
            assert home_page.is_cart_button_displayed()
        with allure.step("Check if link account is displayed"):
            assert home_page.is_link_account_displayed()
        with allure.step("Check if link to ask a question is displayed"):
            assert home_page.is_link_to_ask_a_question_displayed()

    @allure.feature("Catalog Page")
    @allure.story("Catalog elements")
    def test_all_elements_products_catalog_is_clicable(self, browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open product catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Check if all elements in the product catalog are clickable"):
            catalog_page.check_catalog_elements_is_clicable()

    @allure.feature("Cart Page")
    @allure.story("Cart is empty")
    def test_cart_page_is_empty(self, browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to cart page"):
            home_page.go_to_cart()
        with allure.step("Open cart page"):
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Check if cart is empty"):
            assert cart_page.cart_is_empty() is True

    @allure.feature("Cart Page")
    @allure.story("Cart is not empty")
    def test_cart_page_is_not_empty(self, browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open product catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add product to cart"):
            catalog_page.add_to_cart_select_product1()
        with allure.step("Go to cart page"):
            catalog_page.go_to_cart()
        with allure.step("Open cart page"):
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Check if cart is not empty"):
            assert cart_page.cart_is_empty() is False

    @pytest.mark.xfail(reason="This test is expected to fail - bug found")
    @allure.feature('Product search')
    @allure.story('Search results')
    def test_search_result_matches_the_given_search_product(self,browser):
        with allure.step('Open the home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Verify search results'):
            home_page.search_and_match_products()

    @allure.feature("Cart Page")
    @allure.story("Add products to cart")
    def test_add_to_cart_select_products(self,browser):
        with allure.step("Open Home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to Categories menu"):
            home_page.is_catalog_menu_displayed()
            home_page.go_to_categories_menu()
        with allure.step("Open Product Catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Open Cart page"):
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Check that cart is empty"):
            assert cart_page.cart_is_empty() is True
        with allure.step("Go from cart to catalog"):
         cart_page.go_from_cart_to_catalog()
        with allure.step("Add products to cart"):
         catalog_page.add_to_cart_select_products()
        with allure.step("Go to cart"):
         catalog_page.go_to_cart()
        with allure.step("Check that cart is not empty"):
            assert cart_page.cart_is_empty() is False

    @allure.feature("Cart Page")
    @allure.story("Checking_items_params_in_the_cart")
    def test_checking_items_params_in_the_cart(self,browser):
        with allure.step("Open Home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to catalog"):
            home_page.is_catalog_menu_displayed()
            home_page.go_to_categories_menu()
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add_to_cart_select_products"):
            catalog_page.add_to_cart_select_products()
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Contains_cart_product_after_add"):
            cart_page.contains_cart_product_after_add()

    @allure.feature("Cart Functionality")
    @allure.story("Total Amount Verification")
    def test_total_amount_corresponds(self, browser):
        with allure.step("Open the home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
            home_page.go_to_categories_menu()
        with allure.step("Add products to cart"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_products()
        with allure.step("Verify cart functionality"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
            cart_page.contains_cart_product_after_add()
            cart_page.the_total_amount_corresponds()


    @allure.feature("Cart Functionality")
    @allure.story("Add Quantity in Cart Verification")
    def test_checking_add_quantity_in_the_cart(self, browser):
        with allure.step("Open the home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
            home_page.go_to_categories_menu()
        with allure.step("Add a product to the cart"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_product1()
        with allure.step("Go to cart"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Add quantity"):
            cart_page.add_quantity()
        with allure.step("Verify the quantity of the product in the cart"):
            cart_page.change_quantity_add_product_in_cart()


    @allure.feature("Cart Functionality")
    @allure.story("Checking minus quantity in the cart")
    def test_checking_minus_quantity_in_the_cart(self,browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add product to cart"):
            catalog_page.add_to_cart_select_product1()
        with allure.step("Go to cart page"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Add quantity of product"):
            cart_page.add_quantity()
        with allure.step("Reduce the amount of product in cart"):
            cart_page.reduce_the_amount_of()

    @allure.feature("Cart Functionality")
    @allure.story("Removing a product from the cart")
    def test_remove_product_from_the_cart(self,browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add product to cart"):
            catalog_page.add_to_cart_select_product1()
        with allure.step("Go to cart page"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Remove product from cart"):
            cart_page.remove_product_from_cart()
        with allure.step("Check if the cart is empty"):
            cart_page.cart_is_empty()

    @allure.feature("Cart Functionality")
    @allure.story("Going from cart to home page")
    def test_go_from_cart_to_home_page(self,browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add products to cart"):
            catalog_page.add_to_cart_select_products()
        with allure.step("Go to cart page"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Go from cart to home"):
            cart_page.go_from_cart_to_home()
        with allure.step("Open home page again"):
            home_page.open()
            home_page.page_is_loaded()

    @allure.feature("Cart Functionality")
    @allure.story("Going from cart to catalog page")
    def test_go_from_cart_to_catalog_page(self,browser):
        with allure.step("Open home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Go to categories menu"):
            home_page.go_to_categories_menu()
        with allure.step("Open catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Add products to cart"):
            catalog_page.add_to_cart_select_products()
        with allure.step("Go to cart page"):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step("Go from cart to catalog page"):
            cart_page.go_from_cart_to_catalog()
            catalog_page.page_is_loaded()

    @allure.feature("Cart")
    @allure.story("Checkout process")
    def test_go_from_cart_to_order_form_page(self, browser):
            with allure.step("Open the home page"):
                home_page = HomePage(browser)
                home_page.open()
                home_page.page_is_loaded()
                home_page.is_catalog_menu_displayed()
            with allure.step("Go to the categories menu"):
                home_page.go_to_categories_menu()
            with allure.step("Open the product catalog page"):
                catalog_page = ProductCatalogPage(browser)
                catalog_page.open()
                catalog_page.page_is_loaded()
            with allure.step("Select products and add them to the cart"):
                catalog_page.add_to_cart_select_products()
            with allure.step("Go to the cart page"):
                catalog_page.go_to_cart()
                cart_page = CartPage(browser)
                cart_page.open()
                cart_page.page_is_loaded()
            with allure.step("Proceed to the checkout page"):
                cart_page.go_to_order_form_page()
                checkout_page = CheckoutPage(browser)
                checkout_page.page_is_loaded()

    @allure.feature("Catalog")
    @allure.story("Price filter")
    def test_max_price_slider(self, browser):
        with allure.step("Open the home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Open the product catalog page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Set the maximum price slider"):
            catalog_page.setting_price_parameters()

    @pytest.mark.xfail(reason="This test is expected to fail need breakpoint to fill captcha")
    @allure.feature("Authorization")
    @allure.story("Unregistered user")
    def test_attempt_to_authorize_an_unregistered_user(self, browser):
        with allure.step("Open the home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to the account page"):
            home_page.go_to_account()
        with allure.step("Enter login details"):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
        with allure.step("Enter password"):
            login_page.input_password()
        with allure.step("Click element robot"):
            login_page.click_element_robot()
        with allure.step("Click the button came in"):
            login_page.click_button_came_in()  # TODO: need breakpoint to fill captcha
        with allure.step("Verify that an error message appears"):
            assert login_page.email_is_empty(), 'Необходимо заполнить поле E-mail'

    @pytest.mark.xfail(reason="This test is expected to fail need breakpoint to fill captcha")
    @allure.feature("Authorization")
    @allure.story("Unregistered user")
    def test_date_entry_no_unregistered_user(self, browser):
        with allure.step("Open the home page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to the account page"):
            home_page.go_to_account()
        with allure.step("Enter login details"):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
        with allure.step("Enter email and password for an unregistered user"):
            login_page.input_email_password_unregistered_user()
        with allure.step("Click_element_robot"):
            login_page.click_element_robot()
        with allure.step("Click_button_came_in"):
            login_page.click_button_came_in()  # TODO: need breakpoint to fill captcha
        with allure.step("Verify that an error message appears"):
            assert login_page.message_about_invalid_input(), 'Не верный логин или пароль'

    @pytest.mark.xfail(reason="This test is expected to fail need breakpoint to fill captcha")
    @allure.feature('Authorization')
    @allure.story('Registered User')
    def test_registered_user_authorization(self, browser):
        with allure.step('Open Home Page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account'):
            home_page.go_to_account()
        with allure.step('Enter Registered User Data'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.entering_data_of_a_registered_user()
        with allure.step('Click Robot Checkbox'):
            login_page.click_element_robot()
        with allure.step('Click "Came In" Button'): # TODO: need breakpoint to fill captcha
            login_page.click_button_came_in()
        with allure.step('Click User Cabinet Button'):
            login_page.click_button_cabinet_user()
        with allure.step('User Cabinet is Expected'):
            login_page.user_cabinet_is_excepted()

    @pytest.mark.xfail(reason="This test is expected to fail need breakpoint to fill captcha")
    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_an_incorrect_registered_user_password(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Enter incorrect user password'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.entering_an_incorrect_registered_user_password()
        with allure.step('Click robot checkbox'):
            login_page.click_element_robot()
        with allure.step('Click login button'):
            login_page.click_button_came_in() # TODO: need breakpoint to fill captcha
        with allure.step('Verify error message'):
            login_page.message_about_invalid_input()

    @pytest.mark.xfail(reason="This test is expected to fail - bug found")
    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_password_entry_less_than_three_characters(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter password with less than three characters'):
            login_page.user_registration_password_entry_less_than_three_characters()

    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_registered_user_if_field_name_empty(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter registration details without name'):
            login_page.user_registration_without_filling_name()

    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_registered_user_if_field_email_empty(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter registration details without email'):
            login_page.user_registration_without_filling_email()

    @pytest.mark.xfail(reason="This test is expected to fail - bug found")
    @allure.feature("User Registration")
    @allure.story("Entering registered user with incorrect email")
    def test_entering_registered_user_if_field_email_not_correct(self, browser):
        with allure.step("Open Home Page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step("Go to Account page"):
            home_page.go_to_account()
        with allure.step("Open Login page"):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
        with allure.step("Click Register button"):
            login_page.click_button_register()
        with allure.step("Fill in incorrect email for user registration"):
            login_page.user_registration_filling_email_is_not_correct()

    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_registered_user_if_field_phone_empty(self, browser):
        with allure.step('Open Home Page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account'):
            home_page.go_to_account()
        with allure.step('Click Register Button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
        with allure.step("Click Register button"):
            login_page.click_button_register()
        with allure.step('Fill in User Data Without Phone'):
            login_page.user_registration_without_filling_phone()

    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_entering_registered_user_password_confirmation_is_not_correct(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter registration details with password confirmation not matching'):
            login_page.user_registration_password_confirmation_is_not_correct()

    @pytest.mark.xfail(reason="This test is expected to fail - bug found")
    @allure.feature('Registration')
    @allure.story('Registered User')
    def test_attempt_to_register_a_user_with_an_already_registered_email(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter registration details with already registered email'):
            login_page.user_registration_is_email_already_busy()

    @pytest.mark.xfail(reason="This test is expected to fail need breakpoint to fill captcha")
    @allure.feature('Registration')
    @allure.story('New User')
    def test_registration_new_user(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
        with allure.step('Go to Account page'):
            home_page.go_to_account()
        with allure.step('Click Register button'):
            login_page = LoginPage(browser)
            login_page.page_is_loaded()
            login_page.click_button_register()
        with allure.step('Enter registration details'):
            login_page.date_input_user_registration()
        with allure.step('Click_register'):
            login_page.click_element_robot_registration()
            login_page.click_register()  # TODO: need breakpoint to fill captcha
        with allure.step('Go to User Cabinet page'):
            login_page.click_button_cabinet_user()
        with allure.step('Verify user cabinet page is opened'):
            login_page.user_cabinet_is_excepted()

    @allure.feature('Checkout')
    @allure.story('Checkout unregistered user')
    def test_checkout_unregistered_user(self,browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step('Go to Categories menu'):
            home_page.go_to_categories_menu()
        with allure.step('Add product 1 to cart'):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_product1()
        with allure.step('Go to cart'):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step('Go to order form page'):
            cart_page.go_to_order_form_page()
            checkout_page = CheckoutPage(browser)
            checkout_page.page_is_loaded()
        with allure.step('Enter date as unregistered user'):
            checkout_page.date_input_user_unregistrated()


    @allure.feature('Checkout')
    @allure.story('Placing an order without filling in the name')
    def test_attempt_to_place_an_order_without_filling_in_the_name(self,browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step('Go to Categories menu'):
            home_page.go_to_categories_menu()
        with allure.step('Add product 1 to cart'):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_product1()
        with allure.step('Go to cart'):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step('Go to order form page'):
            cart_page.go_to_order_form_page()
            checkout_page = CheckoutPage(browser)
            checkout_page.page_is_loaded()
        with allure.step('Attempt to place an order without filling in the name'):
            checkout_page.attempt_to_place_an_order_without_filling_in_the_name()

    @allure.feature('Checkout')
    @allure.story('Placing an order without filling in the email')
    def test_attempt_to_place_an_order_without_filling_in_the_email(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step('Go to Categories menu'):
            home_page.go_to_categories_menu()
        with allure.step('Add product 1 to cart'):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_product1()
        with allure.step('Go to cart'):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step('Go to order form page'):
            cart_page.go_to_order_form_page()
            checkout_page = CheckoutPage(browser)
            checkout_page.page_is_loaded()
        with allure.step('Attempt to place an order without filling in the email'):
            checkout_page.attempt_to_place_an_order_without_filling_in_the_email()

    @allure.feature('Checkout')
    @allure.story('Placing an order without filling in the phone')
    def test_attempt_to_place_an_order_without_filling_in_the_phone(self, browser):
        with allure.step('Open Home page'):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step('Go to Categories menu'):
            home_page.go_to_categories_menu()
        with allure.step('Add product 1 to cart'):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
            catalog_page.add_to_cart_select_product1()
        with allure.step('Go to cart'):
            catalog_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.open()
            cart_page.page_is_loaded()
        with allure.step('Go to order form page'):
            cart_page.go_to_order_form_page()
            checkout_page = CheckoutPage(browser)
            checkout_page.page_is_loaded()
        with allure.step('Attempt to place an order without filling in the phone'):
            checkout_page.attempt_to_place_an_order_without_filling_in_the_phone()

    @allure.feature("Product Catalog")
    @allure.story("Price Filter")
    def test_products_price_filter(self, browser):
        with allure.step("Open Home Page"):
            home_page = HomePage(browser)
            home_page.open()
            home_page.page_is_loaded()
            home_page.is_catalog_menu_displayed()
        with allure.step("Open Catalog Page"):
            catalog_page = ProductCatalogPage(browser)
            catalog_page.open()
            catalog_page.page_is_loaded()
        with allure.step("Set price parameters"):
            catalog_page.setting_price_parameters()
        with allure.step("Click filter button"):
            catalog_page.click_button_filter()
        with allure.step("Verify price list after filter"):
            catalog_page.the_list_prise_after_filter()
