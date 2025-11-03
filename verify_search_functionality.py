from playwright.sync_api import Page, expect

def test_search_functionality(page: Page):
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill("Python (programming language)")
    page.keyboard.press("Enter")
    expect(page).to_have_url(lambda url: "Python_(programming_language)" in url)
    expect(page.get_by_role("heading", name="Python programming language")).to_be_visible()
