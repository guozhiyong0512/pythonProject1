import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_frame.black_handle import black_wrapper


class BasePage():
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    SEND = "send"
    CONTENT = "content"

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_send_keys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(3)
        res = self.driver.find_elements(by, locator)
        while len(res) == 0:
            self.driver.swipe(0, 600, 0, 200)
            res = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(3)
        return res[0]

    def swip_find_click(self, by, locator):
        self.swip_find(by, locator).click()

    def wait_for(self, by, loctor):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, loctor)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def load(self, yaml_path):
        with open(yaml_path, encoding="utf8") as f:
            data = yaml.load(f)
        for step in data:
            xpath = step.get(self.FIND)
            action = step.get(self.ACTION)
            content = step.get(self.CONTENT)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(By.XPATH, xpath)

            elif action == self.SEND:
                self.find_send_keys(By.XPATH, xpath, content)

    def sceenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)
