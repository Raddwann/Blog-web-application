"""
darkmode_test.py tests the functionallity for the darkmode option,
for both the desktop view and mobile view.
It first imports the needed libraries, Then defines the viewports for
desktop and mobile.
Then calls the function test_dark_mode, the function then initalizes a
Selenium WebDriver instance for Chrome and then sets the window size for the viewport parameter,
Then the 'driver' navigates to the local test URL/port and if the view port is mobile,
it first clicks the hamburger menu (the 3 dashes).
The test then locates the dark mode toggle and verifies its action using 'assert'.
Finally, the browser instance is closed
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def test_dark_mode(viewport):
    """
    Tests dark mode functionality for a given viewport (desktop or mobile).
    
    :param viewport: Dict with 'width', 'height', and 'type' keys to define the browser window size.
    """
    driver = webdriver.Chrome()  # Use appropriate driver (e.g., ChromeDriver)
    try:
        # Set the browser window size based on the viewport
        driver.set_window_size(viewport['width'], viewport['height'])
        driver.get("http://127.0.0.1:8000/")  # Your site's URL

        if viewport['type'] == "mobile":
            # Click the hamburger menu to open the navigation
            hamburger_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "menu-btn"))
            )
            hamburger_menu.click()
            time.sleep(1)  # Allow time for the menu to open

        # Determine the correct toggle button based on the viewport
        toggle_id = "theme-switch" if viewport['type'] == "desktop" else "theme-switch-mobile"

        # Wait for the dark mode toggle button to be interactable
        dark_mode_toggle = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, toggle_id))
        )
        dark_mode_toggle.click()
        time.sleep(1)  # Allow time for the transition

        # Verify dark mode by checking the body class
        body = driver.find_element(By.TAG_NAME, "body")
        assert "darkmode" in body.get_attribute("class"), f"Dark mode not applied for {viewport['type']}!"
        print(f"Test passed for {viewport['type']} viewport.")
    
    finally:
        # Quit the driver to ensure the browser closes
        driver.quit()


if __name__ == "__main__":
    # Define viewports for desktop and mobile
    viewports = [
        {"type": "desktop", "width": 1280, "height": 800},
        {"type": "mobile", "width": 375, "height": 812},
    ]

    # Run the test for each viewport
    for viewport in viewports:
        test_dark_mode(viewport)
