from appium.options.android import UiAutomator2Options
import pytest
from appium import webdriver
import time
import os
import pytest_html

# --- DRIVER SETUP ---
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("appPackage", "com.amazon.mShop.android.shopping")
    options.set_capability("appActivity", "com.amazon.mShop.navigation.MainActivity")
    options.set_capability("noReset", True)
    options.set_capability("autoGrantPermissions", True)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    time.sleep(5)
    yield driver
    driver.quit()

# --- SCREENSHOT ON FAILURE HOOK ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to report
            if hasattr(item, 'extra'):
                item.extra.append(pytest_html.extras.png(screenshot_path))
            else:
                item.extra = [pytest_html.extras.png(screenshot_path)]

# --- REPORT METADATA ---
def pytest_html_report_title(report):
    report.title = "Amazon Android App Automation Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([pytest_html.extras.html("<p><strong>Tester:</strong> Gokul</p>")])
    prefix.extend([pytest_html.extras.html("<p><strong>Project:</strong> Amazon Mobile Automation</p>")])

