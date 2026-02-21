from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='q']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-form__button")
    HELP_LINK = (By.CSS_SELECTOR, "a[href='/help/']")

    def open_home(self) -> None:
        self.open("/")

    def wait_until_loaded(self) -> None:
        self.wait.until(ec.visibility_of_element_located(self.SEARCH_INPUT))
        self.wait.until(ec.visibility_of_element_located(self.SEARCH_BUTTON))

    def has_help_link(self) -> bool:
        return bool(self.driver.find_elements(*self.HELP_LINK))

    def search_for(self, package_name: str) -> None:
        search_input = self.wait.until(ec.element_to_be_clickable(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(package_name)
        self.wait.until(ec.element_to_be_clickable(self.SEARCH_BUTTON)).click()
