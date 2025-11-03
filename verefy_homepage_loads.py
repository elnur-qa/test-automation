from playwright.sync_api import Page, expect

""" def test_wikipedia_homepage_loads(page: Page):
    page.goto("https://www.wikipedia.org/")
    expect(page.locator("text=The Free Encyclopedia")).to_be_visible() """


#Verify Language navigation works
def test_language_selection_to_english(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("link", name="English").click()
    expect(page).to_have_url("https://en.wikipedia.org/wiki/Main_Page")
    expect(page.get_by_text("Welcome to Wikipedia")).to_be_visible()
