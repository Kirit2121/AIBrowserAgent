def check_broken_links(page):
    """Detects broken links on the page."""
    all_links = page.locator("a").all()
    broken_links = []

    for link in all_links:
        href = link.get_attribute("href")
        if href and "http" in href:
            try:
                response = page.request.get(href)
                if response.status >= 400:
                    broken_links.append(href)
            except:
                broken_links.append(href)

    if broken_links:
        print(f"⚠️ Broken Links Found: {broken_links}")

def check_missing_elements(page):
    """Checks if expected elements are missing from the page."""
    missing_elements = []
    required_elements = ["input", "button", "a"]

    for element in required_elements:
        if not page.locator(element).count():
            missing_elements.append(element)

    if missing_elements:
        print(f"⚠️ Missing Elements: {missing_elements}")
