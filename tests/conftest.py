from __future__ import annotations

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("PYPI_BASE_URL", "https://pypi.org").rstrip("/")


@pytest.fixture(scope="session")
def wait_timeout() -> int:
    return int(os.getenv("UI_WAIT_TIMEOUT", "3"))


@pytest.fixture
def driver() -> webdriver.Chrome:
    options = ChromeOptions()
    if os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path:
        service = ChromeService(executable_path=chromedriver_path)
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(0)
    yield browser
    browser.quit()


@pytest.fixture
def wait(driver: webdriver.Chrome, wait_timeout: int) -> WebDriverWait:
    return WebDriverWait(driver, wait_timeout)
