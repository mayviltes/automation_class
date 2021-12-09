from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_1_BTN = (By.ID, 'Header_GlobalLogin_signInQuickLink')
    USER_INPUT = (By.ID, 'Header_GlobalLogin_WC_AccountDisplay_FormInput_logonId_In_Logon_1')
    PASSWORD_INPUT = (By.ID, 'Header_GlobalLogin_WC_AccountDisplay_FormInput_logonPassword_In_Logon_1')
    LOGIN_2_BTN = (By.ID, 'Header_GlobalLogin_WC_AccountDisplay_links_2')

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def getLogin_1(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_1_BTN)

    def getUserInput(self):
        return self.driver.find_element(*LoginPageLocators.USER_INPUT)

    def getPasswordBtn(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    def getLogin_2(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_2_BTN)