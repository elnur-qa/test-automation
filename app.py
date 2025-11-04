from playwright.sync_api import sync_playwright, expect
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to Playwright docs
        page.goto("https://playwright.dev/python/")
        time.sleep(3)

        # Click on Docs link
        page.get_by_role("link", name="Docs").click()
        time.sleep(3)

        # Click "How to install Playwright Pytest"
        page.get_by_role("link", name = "How to install Playwright Pytest").click()
        time.sleep(3)
        #Click on Learn Videos link
        page.get_by_role("link", name= "Learn Videos").click()
        page.wait_for_load_state("domcontentloaded")

        #Clcik on  "Playwright Assertions: Avoid Race Conditions with This Simple Fix!
        page.get_by_role("button", name = "Playwright Assertions: Avoid Race Conditions with This Simple Fix!").click()
        time.sleep(5)


        context.close()
        browser.close()

if __name__ == "__main__":
    run()
