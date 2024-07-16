
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        homePage.ShopItems().click()

        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.AddToCartAndCheckout()

        log.info(f"Checkout Successfull")

        confirmPage = ConfirmPage(self.driver)
        successText = confirmPage.EnterCountryAndConfirmOrder()

        log.info(f"SuccessText :- {successText}")

        assert "Success! Thank you!" in successText
        # To check screenshot feature on filure in report.html
        #assert "Fail" in successText
