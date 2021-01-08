from appium.webdriver.common.mobileby import MobileBy

from APPweixin.page.address_list_page import AddressListPage
from APPweixin.page.basepage import BasePage


class MainPage(BasePage):

    def goto_address(self):
        self.find_and_click(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")
        return AddressListPage(self.driver)
