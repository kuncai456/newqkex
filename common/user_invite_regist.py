import json

import requests

from case.user_center.kyc_commit import Login


def user_invite_regist(email,uid):
    import requests

    url = "http://test-invite.qkex.website/api/user/sendCode"

    payload = {"email":email}
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Origin': 'http://test-invite.qkex.com',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        # 'X-Lang': 'zh-hk',
        # 'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    url = "http://test-invite.qkex.website/api/user/register"
    invitation_code=str(uid)+str("1")
    print("invitation_code",invitation_code)
    payload = {"email":email,
                "verify_code":"111111",
               "password":"qa123456",
               "confirm_password":"qa123456",
                "invitation_code":str(invitation_code)}

    headers = {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'X-Requested-With': 'XMLHttpRequest',
      'X-Lang': 'zh-hk',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    Authorization=Login().login(email, "qa123456")
    # print("Authorization",Authorization)
    # 生成邀请关系

    url = "http://test-invite.qkex.website/api/scenarios/list"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701607829.16.1.1701607844.45.0.0',
        'Origin': 'http://test.qkex.website',
        'Referer': 'http://test.qkex.website/',
        'Source': 'web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Authorization': Authorization,
        'X-Lang': 'zh-HK',
        'x-locale': 'zh-HK'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    #获取uid
    url="http://test-public-rest.qkex.center/user/detail"
    headers = {
        'Content-Type': 'application/json',
        'X-Authorization': Authorization
    }

    response = requests.request("Get", url, headers=headers)

    # print(response.json())
    uid=response.json()['data']["userId"]
    print(email," ",uid)

if __name__ == '__main__':
    # user_invite_regist("90043Ma@163.com",uid=)
    for i in range(1,10):
        email=str("dd10511")+str(i)+str("@163.com")
        print(email)
        user_invite_regist(email,10194641)
    # user_invite_regist("900431Ma@163.com",10194414)

