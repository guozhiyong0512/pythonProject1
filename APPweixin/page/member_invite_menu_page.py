from appium.webdriver.common.mobileby import MobileBy

from APPweixin.page.basepage import BasePage
from APPweixin.page.contcat_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def add_member_menual(self):
        self.find_and_click(MobileBy.XPATH, "//android.widget.TextView[@text='手动输入添加']")
        return ContactAddPage(self.driver)
