from selenium.webdriver.common.by import By

class PaymentPageLocator:
    TITLE_PAYMENT = (By.CLASS_NAME, 'pagoDataTitle')
    QUOTA_BTN = (By.ID, 'iSelectorId')
    AMOUNT_QUOTA_1 = (By.ID, 'dijit_MenuItem_1_text')
    CONTINUE_BTN = (By.ID, 'shippingBillingPageNext')

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitlePayment(self):
        return self.driver.find_element(*PaymentPageLocator.TITLE_PAYMENT)

    def getQuotaLabel(self):
        return self.driver.find_element(*PaymentPageLocator.QUOTA_BTN)

    def getAmountQuota1(self):
        return self.driver.find_element(*PaymentPageLocator.AMOUNT_QUOTA_1)

    def getContinueBtn(self):
        return self.driver.find_element(*PaymentPageLocator.CONTINUE_BTN)