import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import math


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.webdriver = driver
        self.url: str = ''

    def open_url(self, url):
        self.webdriver.get(url)

    def open(self):
        self.open_url(url=self.url)

    def page_is_loaded(self):
        assert self.webdriver.current_url == self.url

    def find_element(self, locator: tuple, timer=10) -> WebElement:
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(
            EC.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)
    def get_text_from_element(self, locator, timer=10):
        element = self.find_element(locator, timer)
        return element.text

    def click_on_drop_down_list(self, locator1: tuple, locator2: tuple):
        button = WebDriverWait(self.webdriver, 30).until(EC.presence_of_element_located(locator1))
        hover = ActionChains(self.webdriver).move_to_element(button)
        hover.perform()
        return WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located(locator2)).click()

    def switch_to_iframe(self, iframe_locator, timer=10):
        WebDriverWait(self, timer).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    def switch_to_default_context(self):
        self.webdriver.switch_to.default_content()

    def accept_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.accept()
        self.switch_to_default_context()

    def dismiss_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.dismiss()
        self.switch_to_default_context()

    def fill_and_accept_alert(self, content):
        alert_el = self.webdriver.switch_to.alert
        alert_el.send_keys(content)
        alert_el.accept()
        self.switch_to_default_context()

    def get_title(self):
        return self.webdriver.title

    def get_url(self):
        return self.webdriver.current_url

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
