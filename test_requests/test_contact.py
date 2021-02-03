import requests


def test_contact():
    res = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwa50a825b2be98d47&corpsecret=IaSqhhALhrwKvaSsN9kepqB_vQllQWUQzZ4kgPBALAI')
    print(res.json()['access_token'])
    token = res.json()['access_token']
    return token


def test_get_member():
    token = test_contact()
    res1 = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=123')
    print(res1.json())


def test_update():
    token = test_contact()
    url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}'
    data = {
        "userid": "123",
        "name": "李四"
    }
    res2 = requests.post(url=url_update, json=data)
    print(res2.json())


def test_delete():
    token = test_contact()
    url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=bbbb'

    res2 = requests.get(url=url_update)
    print(res2.json())


def test_add():
    token = test_contact()
    url_update = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
    data = {
        "userid": "123www",
        "name": "李四",
        "mobile": "+86 13800000000"
    }
    res2 = requests.post(url=url_update, json=data)
    print(res2.json())
