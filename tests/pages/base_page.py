from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, base_url: str) -> None:
        self.driver = driver
        self.wait = wait
        self.base_url = base_url

    def open(self, path: str = "/") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def wait_for_url_contains(self, text: str) -> None:
        self.wait.until(ec.url_contains(text))
