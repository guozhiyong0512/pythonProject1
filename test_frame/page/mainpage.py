import yaml
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        # self.find_and_click(By.XPATH,"//android.widget.ImageView[@resource-id='com.xueqiu.android:id/post_status']")
        # # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")
        # self.find_and_click(By.XPATH,"//android.widget.TextView[@text='行情']")
        # with open("../page/main.yml",encoding="utf8") as f:
        #     data= yaml.load(f)
        # for step in data:
        #     xpath = step.get("find")
        #     action= step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(By.XPATH,xpath)
        self.load("../page/main.yml")

        return MarketPage(self.driver)
