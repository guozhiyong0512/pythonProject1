from typing import List

import requests

from test_requests.req_page.base import Base


class Contact(Base):

    def get_member(self, userid):
        param = {"userid": userid}
        res1 = self.s.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get', params=param)
        return res1.json()

    def update(self, userid: str, name: str, mobile: str, **kwargs):
        url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        data.update(kwargs)
        res2 = self.s.post(url=url_update, json=data)
        print(res2.json())
        return res2.json()

    def delete(self, userid):
        param = {"userid": userid}
        url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'

        res2 = self.s.get(url=url_update, params=param)
        return res2.json()

    def add(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        res2 = self.s.post(url=url_update, json=data)
        return res2.json()
