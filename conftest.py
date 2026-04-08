import os
from asyncio import wait_for

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, Playwright

#load .env when pytest  starts
load_dotenv()

@pytest.fixture(scope="session")
def app_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def user_credentials():
    return {
        "email": os.getenv("USER_EMAIL"),
        "password": os.getenv("USER_PASSWORD")
    }

AUTH_FILE = "auth.json"

@pytest.fixture(scope="session")
def auth_state(playwright: Playwright,app_url, user_credentials):
    if os.path.exists(AUTH_FILE): #remember this
        return AUTH_FILE

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(app_url)
    page.get_by_placeholder("email@example.com").fill(user_credentials["email"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["password"])

    # click login
    page.get_by_role("button", name="Login").click()

    # after login — dashboard loads with ORDERS button
    page.get_by_role("button", name="ORDERS").wait_for()
    context.storage_state(path=AUTH_FILE)
    context.close()
    return AUTH_FILE

@pytest.fixture(scope="session")
def auth_page(browser: Browser, auth_state, app_url):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto(app_url)

    yield page

    context.close()



