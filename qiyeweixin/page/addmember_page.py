from selenium import webdriver
from selenium.webdriver.common.by import By

from qiyeweixin.page.base_page import BasePage
from qiyeweixin.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _location_username = (By.ID, "username")
    _location_memberAdd_english_name = (By.ID, "memberAdd_english_name")
    _location_memberAdd_acctid = (By.ID, "memberAdd_acctid")
    _location_select = (By.XPATH, '//div//span[text()="女"]')
    _location_memberAdd_phone = (By.ID, "memberAdd_phone")
    _location_memberAdd_telephone = (By.ID, "memberAdd_telephone")
    _location_memberAdd_mail = (By.ID, "memberAdd_mail")
    _location_memberEdit_address = (By.ID, "memberEdit_address")
    _location_memberAdd_title = (By.ID, "memberAdd_title")
    _location_sub = (By.XPATH, '//div//a[text()="保存"]')

    def add_member(self):
        self.driver.find_element(*self._location_username).send_keys("老白")
        self.driver.find_element(*self._location_memberAdd_english_name).send_keys("白总")
        self.driver.find_element(*self._location_memberAdd_acctid).send_keys("123")
        self.driver.find_element(*self._location_select).click()
        self.driver.find_element(*self._location_memberAdd_phone).send_keys("15510719667")
        self.driver.find_element(*self._location_memberAdd_telephone).send_keys("15510719667")
        self.driver.find_element(*self._location_memberAdd_mail).send_keys("1327581900@qq.com")
        self.driver.find_element(*self._location_memberEdit_address).send_keys("北京东城")
        self.driver.find_element(*self._location_memberAdd_title).send_keys("测试工程师")
        self.driver.find_element(*self._location_sub).click()
        return ContactPage(self.driver)

    def add_member_fail(self):
        self.driver.find_element(*self._location_username).send_keys("老白")
        self.driver.find_element(*self._location_memberAdd_english_name).send_keys("白总")
        self.driver.find_element(*self._location_memberAdd_acctid).send_keys("123")
        self.driver.find_element(*self._location_select).click()
        self.driver.find_element(*self._location_memberAdd_phone).send_keys("15510719667")
        self.driver.find_element(*self._location_memberAdd_telephone).send_keys("15510719667")
        self.driver.find_element(*self._location_memberAdd_mail).send_keys("1327581900@qq.com")
        self.driver.find_element(*self._location_memberEdit_address).send_keys("北京东城")
        self.driver.find_element(*self._location_memberAdd_title).send_keys("测试工程师")
        error_messsage = self.find(By.XPATH,
                                   '//form//div[@class="member_edit_item member_edit_item_Account"]//div[@class="ww_inputWithTips_tips"]').text
        return error_messsage
