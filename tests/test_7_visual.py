from playwright.sync_api import expect


def test_homeoage_visual(auth_page):

    expect(auth_page).to_have_screenshot("homepage.png")

def test_navbar_visual(auth_page):
    expect(auth_page.locator("app-nav")).to_have_screenshot("navbar.png")

def test_homepage_with_tolerance(auth_page):
    expect(auth_page).to_have_screenshot("homepage_tolerant.png",max_diff_pixels=55 )