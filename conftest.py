import pytest
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

@pytest.fixture
def browser():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
