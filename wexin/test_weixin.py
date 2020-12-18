import time

import selenium
import yaml
from selenium import webdriver


class TestWeiXin():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def test_getcookie(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookie = driver.get_cookies()
        with open("wxcookie.yml", "w", encoding="utf8") as f:
            yaml.dump(cookie, f)

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("wxcookie.yml", encoding="utf8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath('//div//a[@id="menu_contacts"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//div[@class="ww_operationBar"]//a[@class="qui_btn ww_btn js_add_member"]').click()
        self.driver.find_element_by_id("username").send_keys("老白")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("白总")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123")
        self.driver.find_element_by_xpath('//div//span[text()="女"]').click()
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15510719668")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("15510719668")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("1327581900@qq.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("北京东城")
        self.driver.find_element_by_id("memberAdd_title").send_keys("测试工程师")
        self.driver.find_element_by_xpath('//div//a[text()="保存"]').click()
        assert self.driver.find_element_by_id("js_tips").text == "保存成功"
        time.sleep(20)
