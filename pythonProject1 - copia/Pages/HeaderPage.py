from selenium.webdriver.common.by import By

class HeaderPageLocators:
    SEARCH_INPUT = (By.ID, 'SimpleSearchForm_SearchTerm')
    LUPA_BTN = (By.CSS_SELECTOR, 'i#search-black')

class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_INPUT)

    def getLupaBtn(self):
        return self.driver.find_element(*HeaderPageLocators.LUPA_BTN)
