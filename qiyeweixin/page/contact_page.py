import time

from selenium.webdriver.common.by import By

from qiyeweixin.page.adddepartment_page import AddDepartment
from qiyeweixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_get_members = (By.XPATH, '//table//td[@class="member_colRight_memberTable_td"][1]')
    _location_goto_members = (By.XPATH, '//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]')
    _location_goto_department = (
    By.XPATH, '//main//div[@class="member_colLeft_top member_colLeft_top_BorderBottom"]//i')
    _location_go_department = (By.XPATH, '//ul//a[@class="js_create_party"]')

    def goto_add_menber(self):
        from qiyeweixin.page.addmember_page import AddMemberPage
        self.wait_click(self._location_goto_members)
        self.find(self._location_goto_members).click()
        return AddMemberPage(self.driver)

    def get_member(self):
        self.wait_click(self._location_get_members)
        get_member_list = self.finds(self._location_get_members)
        member_list = []
        for i in get_member_list:
            member_list.append(i.text)
        return member_list

    def goto_add_department(self):
        self.find(self._location_goto_department).click()
        self.find(self._location_go_department).click()
        return AddDepartment(self.driver)

    def get_department(self):
        self.driver.refresh()
        time.sleep(2)
        get_department = self.driver.find_elements_by_xpath('//div//a[@class="jstree-anchor"]')
        department_list = []
        for i in get_department:
            department_list.append(i.text)

        return department_list
