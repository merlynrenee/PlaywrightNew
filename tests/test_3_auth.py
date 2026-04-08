from playwright.sync_api import Page, expect


def test_already_logged_in(auth_page):
    #go to straight to order
    auth_page.get_by_role("button", name="ORDERS").click()

    expect(auth_page.get_by_text("Your Orders")).to_be_visible()

def test_dashboard_logged_in(auth_page):
    # another test — still logged in, no login steps
    # verify the dashboard loaded
    expect(auth_page.get_by_role("button", name="ORDERS")).to_be_visible()
    expect(auth_page.get_by_role("button", name = "Go Back to Cart")).to_be_visible()