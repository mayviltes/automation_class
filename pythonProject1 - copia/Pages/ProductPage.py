from selenium.webdriver.common.by import By

class ProductPageLocator:

    PRODUCT_TITLE = (By.CLASS_NAME, 'main_header')
    ADD_PRODUCT_BTN = (By.ID, 'opener')

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def getProductTitle(self):
        return self.driver.find_element(*ProductPageLocator.PRODUCT_TITLE)

    def getAddProductBtn(self):
        return self.driver.find_element(*ProductPageLocator.ADD_PRODUCT_BTN)