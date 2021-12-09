from selenium.webdriver.common.by import By

class InfoPersonalPageLocator:
    TITLE_INFO_PERSONAL = (By.CLASS_NAME, 'personalDataTitle')
    MAIL_INPUT = (By.ID, 'WC__ShoppingCartAddressEntryForm_billingAddressCreateEditFormDiv_1_email1_1')
    TERM_COND_CHECK = (By.ID, 'term_cond')
    CONTINUE_BTN = (By.ID, 'WC_UnregisteredCheckout_links_4')


class InfoPersonalPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitleInfoPersonal(self):
        return self.driver.find_element(*InfoPersonalPageLocator.TITLE_INFO_PERSONAL)

    def getMailInput(self):
        return self.driver.find_element(*InfoPersonalPageLocator.MAIL_INPUT)

    def getTermAndCondCheck(self):
        return self.driver.find_element(*InfoPersonalPageLocator.TERM_COND_CHECK)

    def getContinueBtn(self):
        return self.driver.find_element(*InfoPersonalPageLocator.CONTINUE_BTN)


