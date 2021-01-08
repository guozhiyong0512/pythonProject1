from appium.webdriver.common.mobileby import MobileBy

from APPweixin.page.basepage import BasePage


class ContactAddPage(BasePage):

    def add_contact(self):
        self.find_send_keys(MobileBy.XPATH,
                            "//android.widget.EditText[@resource-id='com.tencent.wework:id/au0' and @text='必填']",
                            "eeee")
        self.find_and_click(MobileBy.XPATH,
                            "//android.widget.RelativeLayout[@resource-id='com.tencent.wework:id/dux']/android.widget.RelativeLayout[1]")
        self.wait_for(MobileBy.XPATH,
                      "//android.widget.TextView[@resource-id='com.tencent.wework:id/dqn' and @text='女']")
        self.find_and_click(MobileBy.XPATH,
                            "//android.widget.TextView[@resource-id='com.tencent.wework:id/dqn' and @text='女']")
        self.find_send_keys(MobileBy.XPATH,
                            "//android.widget.EditText[@resource-id='com.tencent.wework:id/eq7']", 18811112255)
        self.find_and_click(MobileBy.XPATH,
                            "//android.widget.TextView[@resource-id='com.tencent.wework:id/gur']")

        return True
