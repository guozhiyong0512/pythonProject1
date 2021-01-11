from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        self.find_and_click(By.XPATH, "//android.widget.ImageView[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")
        self.find_and_click(By.XPATH, "//android.widget.TextView[@text='行情']")

        return MarketPage(self.driver)
