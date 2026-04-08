from playwright.sync_api import Page, expect


def test_hard_assertion_example(auth_page):
    # hard assertion — stops at first failure
    # useful to run this to SEE the difference
    expect(auth_page.get_by_role("button", name="ORDERS")).to_be_visible()  # passes
    expect(auth_page.get_by_role("button", name="WRONG")).to_be_visible()   # fails here
    expect(auth_page.get_by_role("button", name="Cart")).to_be_visible()    # never reached


def test_soft_assertion_example(auth_page):
    # soft assertion — keeps running after failure
    expect.soft(auth_page.get_by_role("button", name="ORDERS")).to_be_visible()  # passes
    expect.soft(auth_page.get_by_role("button", name="WRONG")).to_be_visible()   # fails BUT continues
    expect.soft(auth_page.get_by_role("button", name="Cart")).to_be_visible()    # still runs
    # all failures reported together at end


def test_real_world_mix(auth_page):
    # real pattern used in companies:
    # soft for non-critical UI checks
    # hard for the critical thing that must pass

    # non-critical — check these but don't stop if wrong
    expect.soft(auth_page.get_by_role("button", name="ORDERS")).to_be_visible()
    expect.soft(auth_page.get_by_role("button", name="Cart")).to_be_visible()
    expect.soft(auth_page.locator(".navbar")).to_be_visible()

    # critical — this must pass
    # if homepage didn't load at all, nothing else matters
    expect(auth_page.locator("app-root")).to_be_visible()