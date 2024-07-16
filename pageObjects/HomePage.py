import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.Common import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # a[href='/angularpractice/shop'] --> by using regular expression (*) is written as a[href*='shop']
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.CSS_SELECTOR, "#inlineRadio1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alertMsg = (By.CLASS_NAME, "alert-success")

    def ShopItems(self):
        # * helps selenium understand  *HomePage.shop as a locator and to replicate below line behaviour
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        return self.driver.find_element(*HomePage.shop)

    def SubmitForm(self,getFormData):
        self.driver.find_element(*HomePage.name).send_keys(getFormData["name"])

        self.driver.find_element(*HomePage.email).send_keys(getFormData["email"])

        self.driver.find_element(*HomePage.password).send_keys(getFormData["password"])

        self.driver.find_element(*HomePage.checkbox).click()

        # Static DropDown
        dropdown = Select(self.driver.find_element(*HomePage.gender))
        dropdown.select_by_visible_text(getFormData["gender"])
        dropdown.select_by_index(getFormData["genderindex"])

        self.driver.find_element(*HomePage.employmentStatus)

        self.driver.find_element(*HomePage.submitButton).click()

        message = self.driver.find_element(*HomePage.alertMsg).text

        return message


