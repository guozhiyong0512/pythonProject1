from appium import webdriver

from test_frame.basepage import BasePage
from test_frame.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)

        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(10)

    def goto_main(self):

        return MainPage(self.driver)