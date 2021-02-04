import pytest

from test_requests.req_page.contact import Contact


class TestContact():

    def setup_class(self):
        self.contact = Contact()
        self.userid = "112233"
        self.username = "测试"

    @pytest.mark.parametrize("corpid,corpsecret,tmp", [(None, None, 0)])
    def test_token(self, corpid, corpsecret, tmp):
        result = self.contact.get_token(corpid, corpsecret)
        print(result)
        assert result.get('errcode') == tmp

    def test_add(self):

        res = self.contact.add(userid=self.userid, name=self.username, mobile="13344445555", department=[1],
                               alias="XXXXX")
        try:
            find_result = self.contact.get_member(self.userid)
        finally:
            self.contact.delete(self.userid)
        assert find_result['name'] == self.username

    def test_delete(self):
        res = self.contact.delete("ccc")
        print(res)

    def test_update(self):
        res = self.contact.add(userid=self.userid, name=self.username, mobile="13344445555", department=[1],
                               alias="XXXXX")
        change_mobile = "13222221111"
        self.contact.update(self.userid, self.username, change_mobile)
        try:
            find_result = self.contact.get_member(self.userid)
        finally:
            self.contact.delete(self.userid)
        assert find_result['mobile'] == change_mobile

    def test_select(self):
        res = self.contact.get_member(123)
        print(res)
