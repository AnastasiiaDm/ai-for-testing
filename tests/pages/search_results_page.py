from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

from tests.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    RESULTS = (By.CSS_SELECTOR, "a.package-snippet")

    def wait_until_loaded(self) -> None:
        self.wait.until(ec.visibility_of_any_elements_located(self.RESULTS))

    def results(self) -> list[WebElement]:
        return self.driver.find_elements(*self.RESULTS)

    def has_package(self, package_name: str) -> bool:
        normalized = package_name.lower()
        return any(normalized in result.text.lower() for result in self.results())

    def open_package(self, package_name: str) -> None:
        normalized = package_name.lower()
        for result in self.results():
            if normalized in result.text.lower():
                result.click()
                return
        raise AssertionError(f"Package '{package_name}' not found in search results.")
