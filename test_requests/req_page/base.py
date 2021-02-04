import requests
from requests import Session


class Base:

    def __init__(self):
        self.s = Session()
        self.corpid = 'wwa50a825b2be98d47'
        self.corpsecret = 'IaSqhhALhrwKvaSsN9kepjPtD_ltNS8DCbxqw9FbAk0'
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        param = {"corpid": corpid, "corpsecret": corpsecret}
        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        return res.json()
