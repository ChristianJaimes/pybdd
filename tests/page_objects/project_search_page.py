from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.config import ProjectSearchLocators, BASE_URL, EXPLICIT_WAIT

class ProjectSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def navigate_to_application(self):
        """Navigate to the Globant POC application."""
        self.driver.get(BASE_URL)

    def search_for_project(self, project_name):
        """Search for a specific project."""
        search_input = self.wait.until(
            EC.presence_of_element_located(ProjectSearchLocators.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(project_name)
        
        search_button = self.driver.find_element(*ProjectSearchLocators.SEARCH_BUTTON)
        search_button.click()

    def is_project_displayed(self):
        """Check if project information is displayed."""
        try:
            self.wait.until(
                EC.presence_of_element_located(ProjectSearchLocators.PROJECT_RESULT)
            )
            return True
        except:
            return False

    def click_project_result(self):
        """Click on the project result."""
        project_result = self.wait.until(
            EC.element_to_be_clickable(ProjectSearchLocators.PROJECT_RESULT)
        )
        project_result.click()

    def are_project_details_visible(self):
        """Check if project details are visible."""
        try:
            self.wait.until(
                EC.visibility_of_element_located(ProjectSearchLocators.PROJECT_DETAILS)
            )
            return True
        except:
            return False

    def get_no_results_message(self):
        """Get the no results message."""
        try:
            message_element = self.wait.until(
                EC.presence_of_element_located(ProjectSearchLocators.NO_RESULTS_MESSAGE)
            )
            return message_element.text
        except:
            return None