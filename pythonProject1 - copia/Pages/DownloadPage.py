from selenium.webdriver.common.by import By

class DownloadPageLocator():
    SELECT_DESTINY = (By.CLASS_NAME, 'md-select')
    OPTION_LIST = (By.)
    DOWNLOAD_BTN = (By.CLASS_NAME, 'action-button')

class DownloadPage:

    def __init__(self, driver):
        self.driver = driver

    def getDownloadBtn(self):
        return self.driver.find_element(*DownloadPageLocator.DOWNLOAD_BTN)
