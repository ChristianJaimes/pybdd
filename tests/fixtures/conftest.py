import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.utils.config import IMPLICIT_WAIT

@pytest.fixture
def browser():
    """Create a Chrome WebDriver instance."""
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    # Set implicit wait
    driver.implicitly_wait(IMPLICIT_WAIT)
    
    # Maximize window
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.quit()