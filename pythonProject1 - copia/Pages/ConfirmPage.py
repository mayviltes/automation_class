from selenium.webdriver.common.by import By

class ConfirmPageLocator:
    TITLE_CONFIRM = (By.ID, 'WC_confirmatiosuccess_message_box')
    DOWNLOAD_BTN = (By.ID, 'WC_OrderShippingBillingConfirmationPage_Print_Link')

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitleConfirm(self):
        return self.driver.find_element(*ConfirmPageLocator.TITLE_CONFIRM)

    def getDownloandBtn(self):
        return self.driver.find_element(*ConfirmPageLocator.DOWNLOAD_BTN)