import json
import random
import time

import pyotp
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

from common.boss_transfer_to_person import BossTransferToPerson

urllib3.disable_warnings()




class Login:

    def login(self, user, password):
        url = "http://test-public-rest.qkex.center/user/login"
        headers = {"Content-Type": "application/json"}
        data = {"account": user, "password": password,
                "verifyCode": "111111"}

        rep = requests.request(method="post", json=data, url=url, headers=headers, verify=False)
        print(rep.json())
        return rep.json()["data"]["accessToken"]


class BindGoogleVerifyCode:
    def __init__(self,user,password):
        self.user=user
        self.Authorization=Login().login(user,password)
        # self.Authorization="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MDEwZGIzMy0xOTdmLTRlYzYtYmMwMy03Nzc2NzgyYmQwYjYxODI5NjE4MDA3IiwidWlkIjoiUVY0U3lPK2ZvemtvK0ZuWklyeE85QT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiIvY2s4bE52T0JwME5WanNoSUhDSG5RPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MTQwMDQyOSwiZXhwIjoxNjkxNDg2ODI5LCJpc3MiOiJ3Y3MifQ.HRTofaT77i4GTT0GsDBeq6qw_nUYQjLEL5xpE2rYa0M"
        self.headers={"Content-Type":"application/json",
                      "X-Locale":"zh-HK",
                      "X-Authorization":self.Authorization,
                      "Source":"web"}

    def bind(self):

        url = "http://test-public-rest.qkex.website/user/google/bind"

        payload = {}
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': 'locale=en-US; _ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701607829.16.1.1701609363.59.0.0',
            'Origin': 'http://test.qkex.website',
            'Referer': 'http://test.qkex.website/',
            'Source': 'web',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Authorization': self.Authorization,
            'X-Lang': 'zh-HK',
            'x-locale': 'zh-HK'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    def bind_send_code(self):
        import requests
        import json

        url = "http://test-public-rest.qkex.website/user/user-send-code"

        payload = json.dumps({
            "type": "10"
        })
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': 'locale=en-US; _ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701607829.16.1.1701609363.59.0.0',
            'Origin': 'http://test.qkex.website',
            'Referer': 'http://test.qkex.website/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Authorization': self.Authorization,
            'X-Lang': 'zh-HK',
            'x-locale': 'zh-HK'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    def read_google_authenticator_code(self,secret_key):
        """
        读取并返回谷歌身份验证器的动态验证码
        :param secret_key: 谷歌身份验证器的密钥
        :return: 动态验证码
        """
        # secret_key="THQMOKDRGUM2MKFN"
        totp = pyotp.TOTP(secret_key)
        current_time = int(time.time())
        return totp.at(current_time)

    def bind_google_verify_code(self):
        bind=self.bind()
        secret=bind["data"]['secret']
        googleVerifyCode=self.read_google_authenticator_code(secret)
        self.bind_send_code()


        url = f"http://test-public-rest.qkex.website/user/google/verify?verifyCode=111111&googleVerifyCode={googleVerifyCode}"

        payload = json.dumps({})
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': 'locale=en-US; _ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701607829.16.1.1701610255.60.0.0',
            'Origin': 'http://test.qkex.website',
            'Referer': 'http://test.qkex.website/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Authorization': self.Authorization,
            'X-Lang': 'zh-HK',
            'x-locale': 'zh-HK'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        print("绑定谷歌验证码成功")
        print(self.user,"  ",secret)
        with open("./googleVerify.text",'a',encoding="utf-8")as f:
            f.write(str(self.user)+"  "+secret+"\n")

if __name__ == '__main__':
    # user=KYCCommit(user="d1011Ma@163.com",password="qa123456")
    # user.user_kyc_commit()
    user=BindGoogleVerifyCode(user="dd1052@163.com",password="qa123456")
    user.bind_google_verify_code()