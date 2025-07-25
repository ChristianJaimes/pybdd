from pytest_bdd import given, when, then, parsers
from tests.page_objects.project_search_page import ProjectSearchPage

@given("the user enters to Globant POC application")
def navigate_to_app(browser):
    page = ProjectSearchPage(browser)
    page.navigate_to_application()

@when(parsers.parse("the user searches for '{project_name}'"))
def search_project(browser, project_name):
    page = ProjectSearchPage(browser)
    page.search_for_project(project_name)

@when("the user clicks on the project result")
def click_project_result(browser):
    page = ProjectSearchPage(browser)
    page.click_project_result()

@then("the project information should be displayed")
def verify_project_displayed(browser):
    page = ProjectSearchPage(browser)
    assert page.is_project_displayed(), "Project information is not displayed"

@then("the project details should be accessible")
def verify_project_accessible(browser):
    page = ProjectSearchPage(browser)
    assert page.are_project_details_visible(), "Project details are not accessible"

@then("the complete project details page should load")
def verify_details_page_loaded(browser):
    page = ProjectSearchPage(browser)
    assert page.are_project_details_visible(), "Project details page did not load"

@then("all project information should be visible")
def verify_all_info_visible(browser):
    page = ProjectSearchPage(browser)
    assert page.are_project_details_visible(), "Not all project information is visible"

@then(parsers.parse('an appropriate "{message}" message should be displayed'))
def verify_no_results_message(browser, message):
    page = ProjectSearchPage(browser)
    actual_message = page.get_no_results_message()
    assert actual_message == message, f"Expected message '{message}' but got '{actual_message}'"