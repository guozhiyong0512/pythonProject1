import time

from selenium.webdriver.common.by import By

from qiyeweixin.page.base_page import BasePage


class AddDepartment(BasePage):

    def add_department(self):
        from qiyeweixin.page.contact_page import ContactPage
        self.driver.find_element(By.XPATH, '//div//input[@name="name"]').send_keys("test")
        self.driver.find_element(By.XPATH,
                                 '//div//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        self.driver.find_element(By.XPATH,
                                 '//div[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]//a[@class="jstree-anchor"][1]').click()
        self.driver.find_element(By.XPATH, '//div//a[@class="qui_btn ww_btn ww_btn_Blue"]').click()

        return ContactPage(self.driver)
