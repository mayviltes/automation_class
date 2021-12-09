from selenium.webdriver.common.by import By

class SummaryPageLocator:
    TITLE_SUMMARY = (By.CLASS_NAME, 'resumenDataTitle')
    CONFIRM_BTN = (By.ID, 'singleOrderSummary')

class SummaryPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitleSummary(self):
        return self.driver.find_element(*SummaryPageLocator.TITLE_SUMMARY)

    def getConfirmBtn(self):
        return self.driver.find_element(*SummaryPageLocator.CONFIRM_BTN)