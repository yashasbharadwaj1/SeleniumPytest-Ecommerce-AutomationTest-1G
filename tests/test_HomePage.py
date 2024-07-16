import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getFormData):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        message = homePage.SubmitForm(getFormData)
        log.info(f"Form Submission message :- {message}")
        assert "Success" in message

        # so that 1st data tuple of Rahul gets cleared and 2nd data tuple gets passed
        self.driver.refresh()

    @pytest.fixture(
        params=HomePageData.test_home_page_data
    )
    def getFormData(self,request):
        return request.param
