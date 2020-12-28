import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestApp():

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "unicodeKeyboard":True,
            "resetKeyboard":True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_app_click(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='工作台']").click()
        time.sleep(5)
        action = TouchAction(self.driver)
        win_size = self.driver.get_window_rect()
        width = win_size["width"]
        height = win_size["height"]
        x1 = width / 2
        height_start = height * 4 / 5
        height_end = height * 1 / 5
        action.press(x=x1, y=height_start).wait(800).move_to(x=x1, y=height_end).release().perform()
        time.sleep(10)
        #获取打卡对象信息
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='打卡']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath('//*[contains(@text,"次外出")]').click()
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source