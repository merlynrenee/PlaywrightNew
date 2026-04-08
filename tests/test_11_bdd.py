from signal import pause

import pytest
from playwright.sync_api import expect, Page
from pytest_bdd import scenario, scenarios, given, when, then

from pageObject.apiUtils import ApiUtils

scenarios("../features/orders.feature")

@pytest.fixture
def shared_data():
    return {}

@given("a new order is created via API")
def create_order(playwright,user_credentials,shared_data):
    api = ApiUtils()
    order_id=api.create_order(playwright,user_credentials)
    shared_data["order_id"]=order_id

@given("user is on the login page")
def user_on_login_page(auth_page,shared_data,):
    shared_data["page"]=auth_page

@when("the user logins in with valid credentials")
def user_logins(shared_data):
    page = shared_data["page"]
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()

@when("the user navigates to the orders page")
def user_navigates(shared_data):
    page = shared_data["page"]
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

@then("the order should be visible in the list")
def order_is_visible(shared_data):
    page = shared_data["page"]
    order_id = shared_data["order_id"]
    print(f"Looking for order ID: {order_id}")
    print(f"Table content: {page.locator('tr').all_text_contents()}")

    order_row = page.locator("tr").filter(has_text=order_id)
    #expect(order_row).to_be_visible(timeout=10000)
    #order_row.get_by_role("button", name="View").click()
    print(f"Order id:{order_id} found in list")
    pause()
    order_row.get_by_role("button", name="Delete").click()
    print(f"Order {order_id} deleted — test data cleaned up")

