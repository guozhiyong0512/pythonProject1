import yaml
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage


class SearchPage(BasePage):

    def search(self):
        # self.find_send_keys(By.XPATH,"//android.widget.EditText[@resource-id='com.xueqiu.android:id/search_input_text']","XXXX")
        # self.find(By.XPATH,"//android.widget.EditText[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("XXXX")
        # with open("../page/search.yml", encoding="utf8") as f:
        #     data = yaml.load(f)
        # for step in data:
        #     xpath = step.get("find")
        #     action = step.get("action")
        #     content=step.get("content")
        #     if action == "find_and_click":
        #         self.find_and_click(By.XPATH,xpath)
        #
        #     elif  action == "send":
        #         self.find_send_keys(By.XPATH, xpath,content)
        self.load("../page/search.yml")
        return True
