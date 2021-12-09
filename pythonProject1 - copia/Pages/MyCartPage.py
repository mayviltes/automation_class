from selenium.webdriver.common.by import By

class MyCartPageLocator:
    TITLE_MYCART = (By.ID, 'order_details_cart_title')
    CONTINUE_BTN = (By.ID, 'WC_CheckoutLogonf_div_10')


class MyCartPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitleMyCart(self):
        return self.driver.find_element(*MyCartPageLocator.TITLE_MYCART)

    def getContinueBtn(self):
        return self.driver.find_element(*MyCartPageLocator.CONTINUE_BTN)