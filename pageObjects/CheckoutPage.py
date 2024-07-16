from selenium.webdriver.common.by import By

from utilities.Common import BaseClass


class CheckoutPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    productWebElements = (By.XPATH, "//div[@class='card h-100']")
    productTitle = (By.XPATH, "div/h4/a")
    addToCart = (By.XPATH, "div/button")
    viewCart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    performCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def AddToCartAndCheckout(self):
        ProductWebElements = self.driver.find_elements(*CheckoutPage.productWebElements)
        for productElement in ProductWebElements:
            title = productElement.find_element(*CheckoutPage.productTitle).text
            if title == "Blackberry":
                # Add to cart
                productElement.find_element(*CheckoutPage.addToCart).click()

        # View Cart
        self.driver.find_element(*CheckoutPage.viewCart).click()

        # Perform Checkout
        self.driver.find_element(*CheckoutPage.performCheckout).click()



