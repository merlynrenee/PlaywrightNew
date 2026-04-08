from playwright.sync_api import expect


def test_read_page_title(auth_page):
    title = auth_page.evaluate("document.title")

    print(f"Page title:{title}")
    assert "Let's Shop" in title

def test_read_local_storage_token(auth_page):
    token= auth_page.evaluate("localStorage.getItem('token')")

    print(f"Token form local storage token:{token}")

    assert token is not None
    assert len(token) > 0

def scroll_to_bottom(auth_page):
    auth_page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
    #goes to top of the page
    auth_page.evaluate("window.scrollTo(0,0)")

    expect(auth_page.get_by_role("button", name = "ORDERS")).to_be_visible()

def test_highlight_element(auth_page):
    auth_page.get_by_role("button", name = "ORDERS").evaluate("function(el) {el.style.border= '3px solid red';}")

    expect(auth_page.get_by_role("button", name="ORDERS")).to_be_visible()