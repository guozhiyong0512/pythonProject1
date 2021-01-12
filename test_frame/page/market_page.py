import yaml
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.search_page import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        # self.find_and_click(By.XPATH,"//android.widget.ImageButton[@resource-id='com.xueqiu.android:id/action_search']")
        # with open("../page/market.yml",encoding="utf8") as f:
        #     data= yaml.load(f)
        # for step in data:
        #     xpath = step.get("find")
        #     action= step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(By.XPATH,xpath)
        self.load("../page/market.yml")
        return SearchPage(self.driver)
