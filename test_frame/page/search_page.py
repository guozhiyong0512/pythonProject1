from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage


class SearchPage(BasePage):

    def search(self):
        # self.find_send_keys(By.XPATH,"//android.widget.EditText[@resource-id='com.xueqiu.android:id/search_input_text']","XXXX")
        self.find(By.XPATH,
                  "//android.widget.EditText[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("XXXX")

        return True
