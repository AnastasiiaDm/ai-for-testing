from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_login(self) -> None:
        self.open("/account/login/")

    def wait_until_loaded(self) -> None:
        self.wait.until(ec.visibility_of_element_located(self.USERNAME_INPUT))
        self.wait.until(ec.visibility_of_element_located(self.PASSWORD_INPUT))
        self.wait.until(ec.visibility_of_element_located(self.SUBMIT_BUTTON))
