# page_objects/product_page.py (Extend this class)

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        logging.info(f"🔍 Searching for: {product_name}")
        try:
            search_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/chrome_action_bar_search_icon")
                )
            )
            search_icon.click()

            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/rs_search_src_text")
                )
            )

            search_input.send_keys(product_name + "\n")
            logging.info("✅ Search submitted successfully")
        except Exception as e:
            logging.error(f"❌ Search failed: {e}")
            raise

