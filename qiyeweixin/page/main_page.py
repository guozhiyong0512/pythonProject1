from selenium.webdriver.common.by import By
from qiyeweixin.page.addmember_page import AddMemberPage
from qiyeweixin.page.base_page import BasePage
from qiyeweixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    _location_goto_contact = (By.XPATH, '//div//a[@id="menu_contacts"]')

    def goto_add_member(self):
        self.find(self._location_goto_member).click()

        return AddMemberPage(self.driver)

    def goto_contact(self):
        self.find(self._location_goto_contact).click()

        return ContactPage(self.driver)
