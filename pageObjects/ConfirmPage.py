from selenium.webdriver.common.by import By

from utilities.Common import BaseClass


class ConfirmPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    india = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[value='Purchase']")
    alertMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def EnterCountryAndConfirmOrder(self):
        self.driver.find_element(*ConfirmPage.country).send_keys("ind")

        self.verifyLinkPresence("India")

        self.driver.find_element(*ConfirmPage.india).click()

        self.driver.find_element(*ConfirmPage.checkbox).click()

        self.driver.find_element(*ConfirmPage.purchaseButton).click()

        successText = self.driver.find_element(*ConfirmPage.alertMsg).text

        return successText
