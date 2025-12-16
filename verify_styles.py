from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Desktop View
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Load local file
        filepath = os.path.abspath("diagrama.html")
        page.goto(f"file://{filepath}")

        # Screenshot full page to check overall rhythm
        page.screenshot(path="/home/jules/verification/desktop_full.png", full_page=True)

        # Screenshot Hero specifically to check top padding
        # Hero is the first section
        hero = page.locator("section").first
        hero.screenshot(path="/home/jules/verification/desktop_hero.png")

        # Screenshot a standard section (e.g. Criterios)
        criterios = page.locator("#criterios")
        criterios.screenshot(path="/home/jules/verification/desktop_criterios.png")

        # Mobile View
        page_mobile = browser.new_page(viewport={"width": 375, "height": 812})
        page_mobile.goto(f"file://{filepath}")

        # Screenshot full page mobile
        page_mobile.screenshot(path="/home/jules/verification/mobile_full.png", full_page=True)

        # Screenshot Hero Mobile
        hero_mobile = page_mobile.locator("section").first
        hero_mobile.screenshot(path="/home/jules/verification/mobile_hero.png")

        # Check Back to Top button (need to scroll down to make it appear)
        page_mobile.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        # Wait a bit for transition
        page_mobile.wait_for_timeout(1000)
        page_mobile.screenshot(path="/home/jules/verification/mobile_bottom.png")

        browser.close()

if __name__ == "__main__":
    run()
