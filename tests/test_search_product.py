import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page_objects.product_page import ProductPage

@pytest.mark.smoke
def test_add_product_to_cart(driver):
    product = ProductPage(driver)
    product.search_product("shoes")


