from playwright.sync_api import Page, expect


def test_login_recorded(page: Page, app_url, user_credentials):
    # navigate to the site
    page.goto(app_url)

    # fill in credentials from .env
    page.get_by_placeholder("email@example.com").fill(user_credentials["email"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["password"])

    # click login
    page.get_by_role("button", name="Login").click()

    # after login — dashboard loads with ORDERS button
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()


