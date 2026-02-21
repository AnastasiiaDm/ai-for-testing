from __future__ import annotations

from pytest_bdd import given, parsers, scenarios, then, when

from tests.pages.home_page import HomePage
from tests.pages.login_page import LoginPage
from tests.pages.project_page import ProjectPage
from tests.pages.search_results_page import SearchResultsPage


scenarios("../features/pypi_ui.feature")


@given("I open the PyPI home page")
def open_home_page(driver, wait, base_url) -> None:
    home_page = HomePage(driver, wait, base_url)
    home_page.open_home()
    home_page.wait_until_loaded()


@then("the home page core controls are visible")
def verify_home_core_controls(driver, wait, base_url) -> None:
    home_page = HomePage(driver, wait, base_url)
    assert home_page.has_help_link(), "Expected Help link to be visible on home page."


@when(parsers.parse('I search for package "{package_name}"'))
def search_for_package(driver, wait, base_url, package_name: str) -> None:
    home_page = HomePage(driver, wait, base_url)
    home_page.search_for(package_name)


@then(parsers.parse('results are shown for package "{package_name}"'))
def verify_search_results(driver, wait, base_url, package_name: str) -> None:
    results_page = SearchResultsPage(driver, wait, base_url)
    results_page.wait_until_loaded()
    assert results_page.has_package(package_name), (
        f"Expected search results to include package '{package_name}'."
    )


@given(parsers.parse('I search and open package "{package_name}"'))
def search_and_open_package(driver, wait, base_url, package_name: str) -> None:
    home_page = HomePage(driver, wait, base_url)
    home_page.open_home()
    home_page.wait_until_loaded()
    home_page.search_for(package_name)

    results_page = SearchResultsPage(driver, wait, base_url)
    results_page.wait_until_loaded()
    results_page.open_package(package_name)


@then(parsers.parse('package details are displayed for "{package_name}"'))
def verify_package_details(driver, wait, base_url, package_name: str) -> None:
    project_page = ProjectPage(driver, wait, base_url)
    project_page.wait_until_loaded()
    assert package_name.lower() in project_page.title_text().lower(), (
        f"Expected package page title to contain '{package_name}'."
    )


@then(parsers.parse('install command is visible for "{package_name}"'))
def verify_install_command(driver, wait, base_url, package_name: str) -> None:
    project_page = ProjectPage(driver, wait, base_url)
    assert project_page.install_command_contains(package_name), (
        f"Expected pip install command for package '{package_name}'."
    )


@when("I open release history")
def open_release_history(driver, wait, base_url) -> None:
    project_page = ProjectPage(driver, wait, base_url)
    project_page.go_to_release_history()


@then("release history entries are visible")
def verify_release_history(driver, wait, base_url) -> None:
    project_page = ProjectPage(driver, wait, base_url)
    assert project_page.has_release_entries(), "Expected at least one release history entry."


@given("I open the login page")
def open_login_page(driver, wait, base_url) -> None:
    login_page = LoginPage(driver, wait, base_url)
    login_page.open_login()


@then("login form controls are visible")
def verify_login_form_controls(driver, wait, base_url) -> None:
    login_page = LoginPage(driver, wait, base_url)
    login_page.wait_until_loaded()
