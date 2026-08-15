from playwright.sync_api import sync_playwright
import webbrowser

def open_website(url):

    try:

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        webbrowser.open(url)

        return {
            "success": True,
            "message": f"Opened {url}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
def search_web(query):

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(
                "https://www.google.com"
            )

            page.locator(
                "textarea[name='q']"
            ).fill(query)

            page.keyboard.press("Enter")

            page.wait_for_load_state(
                "domcontentloaded"
            )

            return {
                "success": True,
                "message": f"Searched Google for: {query}"
            }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }