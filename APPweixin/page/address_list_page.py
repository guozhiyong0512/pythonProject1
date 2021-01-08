import time

from appium.webdriver.common.mobileby import MobileBy

from APPweixin.page.basepage import BasePage
from APPweixin.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):

    def click_addmember(self):
        time.sleep(3)
        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH, "//*[@text='添加成员']")

        return MemberInviteMenuPage(self.driver)
