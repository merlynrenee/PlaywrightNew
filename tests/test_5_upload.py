from pathlib import Path

from playwright.sync_api import Page,expect
BASE_DIR = Path(__file__).parent.parent   # goes up from tests/ to project root
FILE_PATH = BASE_DIR / "data" / "test_upload.txt"

def test_file_upload(page:Page):
    page.goto("https://practice.expandtesting.com/upload")

    # set the file on the input
    page.get_by_test_id("file-input").set_input_files(FILE_PATH)

    # click upload
    page.get_by_test_id("file-submit").click()
    page.pause()

    # verify success heading appears
    expect(page.get_by_role("heading", name="File Uploaded!")).to_be_visible()

def test_file_upload_shows_filename(page: Page):
    page.goto("https://practice.expandtesting.com/upload")

    page.get_by_test_id("file-input").set_input_files(FILE_PATH)
    page.get_by_test_id("file-submit").click()

    # verify the actual filename appears on the page after upload
    expect(page.get_by_text("test_upload.txt")).to_be_visible()