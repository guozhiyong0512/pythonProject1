from APPweixin.page.App import App


class TestContact():

    def setup(self):
        self.app = App()
        self.app.start()

    def test_add_member(self):
        res = self.app.goto_main().goto_address().click_addmember().add_member_menual().add_contact()
        assert res
