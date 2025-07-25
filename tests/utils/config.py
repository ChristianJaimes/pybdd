from selenium.webdriver.common.by import By

# Application Configuration
BASE_URL = "https://globantpoc.azurewebsites.net"

# Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# Locators for Project Search
class ProjectSearchLocators:
    SEARCH_INPUT = (By.ID, "project-search-input")
    SEARCH_BUTTON = (By.ID, "search-button")
    PROJECT_RESULT = (By.CLASS_NAME, "project-result-item")
    PROJECT_DETAILS = (By.CLASS_NAME, "project-details")
    NO_RESULTS_MESSAGE = (By.CLASS_NAME, "no-results-message")