from selenium.webdriver.common.by import By

class AccountPageLocator():
    NAME_TITLE = ((By.LINK_TEXT, 'Maria Lucinda Barboza'))
    SEARCH_INPUT = (By.ID, 'SimpleSearchForm_SearchTerm')
    LUPA_BTN = (By.ID, 'search-black')

class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    def getNameTitle(self):
        return self.driver.find_element(*AccountPageLocator.NAME_TITLE)

    def getSearchInput(self):
        return self.driver.find_element(AccountPageLocator.SEARCH_INPUT)

    def getLupaBtn(self):
        return self.driver.find_element(*AccountPageLocator.LUPA_BTN)