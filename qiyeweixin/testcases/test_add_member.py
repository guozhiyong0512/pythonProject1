from qiyeweixin.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        res = self.main.goto_add_member().add_member().get_member()
        assert "老白" in res

    def test_add_member_fail(self):
        res = self.main.goto_add_member().add_member_fail()
        assert res == "该帐号已被“老白”占有"

    def test_add_member_by_contact(self):
        result = self.main.goto_contact().goto_add_menber().add_member().get_member()
        if result != None:
            assert '老白' in result

    def teardown_class(self):
        self.main.quit()
