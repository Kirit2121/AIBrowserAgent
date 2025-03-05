import time
from playwright.sync_api import sync_playwright
from app.automation.bug_detection import check_broken_links, check_missing_elements
from app.automation.reports import save_test_report

def perform_browser_actions(instruction):
    """Executes AI-generated steps in Chrome."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=5000)
        page = browser.new_page()

        try:
            if "go to" in instruction:
                url = instruction.split("go to")[-1].split()[0].strip()
                if not url.startswith("http"):
                    url = f"https://google.com"
                page.goto(url,timeout=60000)
                print(f"Opened: {url}")
                time.sleep(10)

          
            # Bug detection & reporting
            check_broken_links(page)
            # check_missing_elements(page)
            save_test_report(page)

        finally:
           print("Browser closed")
