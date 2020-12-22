from qiyeweixin.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        res = self.main.goto_contact().goto_add_department().add_department().get_department()
        assert "test" in res
