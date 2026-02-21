from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.pages.base_page import BasePage


class ProjectPage(BasePage):
    PROJECT_TITLE = (By.CSS_SELECTOR, "h1.package-header__name")
    RELEASE_HISTORY_LINK = (By.CSS_SELECTOR, "a[href$='/#history'], a[href$='/history/']")
    RELEASE_ENTRIES = (By.CSS_SELECTOR, "div.release, .release.release--latest")

    def wait_until_loaded(self) -> None:
        self.wait.until(ec.visibility_of_element_located(self.PROJECT_TITLE))

    def title_text(self) -> str:
        return self.wait.until(ec.visibility_of_element_located(self.PROJECT_TITLE)).text

    def install_command_contains(self, package_name: str) -> bool:
        command_locator = (By.XPATH, f"//*[contains(normalize-space(.), 'pip install {package_name}')]")
        return bool(self.driver.find_elements(*command_locator))

    def go_to_release_history(self) -> None:
        self.wait.until(ec.element_to_be_clickable(self.RELEASE_HISTORY_LINK)).click()

    def has_release_entries(self) -> bool:
        self.wait.until(ec.visibility_of_any_elements_located(self.RELEASE_ENTRIES))
        return len(self.driver.find_elements(*self.RELEASE_ENTRIES)) > 0
