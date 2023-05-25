import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

@pytest.fixture
def browser(setup_chrome_options):
    options = setup_chrome_options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture
def setup_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-save-password-bubble')
    return options