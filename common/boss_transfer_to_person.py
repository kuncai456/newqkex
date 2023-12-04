import json
import time

import pyotp
import requests


class BossTransferToPerson:


    def boss_login(self):
        """boss登录"""
        url = "http://192.168.200.122:9999/login/auth"

        payload = 'account=testxin&password=qa123456&captcha=111111'
        headers = {
            'Host': '192.168.200.122:9999',
            'Connection': 'keep-alive',
            'Content-Length': '48',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://192.168.200.122:9999',
            # 'Cookie': 'JSESSIONID=1EAB731FA0D05C3750D89F5FF91B495F; locale=en-US'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        print(response.headers)
        return response

    def boss_transfer_apply(self,Cookie,symbol,applyAmount,toUserId,googleVerifyCode):
        """boss平台转账申请"""
        url = "http://192.168.200.122:9999/boss/platform/transfer/apply"
        payload = json.dumps({
            "toBiz": "2",
            "symbol": symbol,
            "toUserId": "10132972",
            "fromUserId": "10",
            "fromBiz": "9",
            "applyAmount": applyAmount,
            "applyRemark": "1000",
            "applyTransferType": 1,
            "receiveUser": [
                {
                    "toUserId": toUserId
                }
            ],
            "googleVerifyCode": googleVerifyCode
        })
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': Cookie,
            'Origin': 'http://192.168.200.122:9999',
            'Referer': 'http://192.168.200.122:9999/views/modules/platform/transferManage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return response

    def boss_tranfer_list(self,Cookie):
        """boss平台转账申请列表"""
        url = "http://192.168.200.122:9999/boss/platform/transfer?page=1&rows=50&sortField=createStartTime&order=DESC"

        payload = {}
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': Cookie,
            'Referer': 'http://192.168.200.122:9999/views/modules/platform/transferManage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.json())
        return response.json()

    def boss_audit(self,Cookie,id,approveAmount,googleVerifyCode):
        """boss平台转账申请审核"""
        url = "http://192.168.200.122:9999/boss/platform/transfer/audit"

        payload = json.dumps({
            "id": id,
            "checkStatus": "10",
            "approveAmount": approveAmount,
            "checkRemark": "测试虚增",
            "googleVerifyCode": googleVerifyCode
        })
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': Cookie,
            'Origin': 'http://192.168.200.122:9999',
            'Referer': 'http://192.168.200.122:9999/views/modules/platform/transferManage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def read_google_authenticator_code(self):
        """
        读取并返回谷歌身份验证器的动态验证码
        :param secret_key: 谷歌身份验证器的密钥
        :return: 动态验证码
        """
        secret_key="THQMOKDRGUM2MKFN"
        totp = pyotp.TOTP(secret_key)
        current_time = int(time.time())
        return totp.at(current_time)

    def get_kyc_aply_list(self,uid,Cookie):
        """获取kyc申请接口"""

        url = f"http://192.168.200.122:9999/boss/uCenter/kyc/list?userId={uid}&status=4&range=0&page=1&rows=50"

        payload = {}
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': Cookie,
            'Referer': 'http://192.168.200.122:9999/views/modules/uCenter/IdentityAuth',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def kyc_pass(self,id,userId,level,countryCode,email,googleVerifyCode,Cookie):
        """kyc审核通过"""
        url = "http://192.168.200.122:9999/boss/uCenter/kyc/pass"

        payload ={
            "id":id,
            "leavingMessage":"审核通过",
            "userId":userId,
            "level":level,
            "countryCode":countryCode,
            "mobile":"",
            "email":email,
            "googleVerifyCode":googleVerifyCode
        }
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': Cookie,
            'Origin': 'http://192.168.200.122:9999',
            'Referer': 'http://192.168.200.122:9999/views/modules/uCenter/IdentityAuth',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def process(self,symbol,amount,user):
        try:
            Cookie=self.boss_login().headers["Set-Cookie"]
            print(Cookie)
            self.boss_transfer_apply(Cookie=Cookie,symbol=symbol,applyAmount=amount,toUserId=user,googleVerifyCode=self.read_google_authenticator_code())
            id=self.boss_tranfer_list(Cookie=Cookie)["data"]['rows'][0]['id']
            self.boss_audit(Cookie=Cookie,id=id,approveAmount=amount,googleVerifyCode=self.read_google_authenticator_code())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # j = 10135826
    # for i in [
    #     10194596,
    #     10194606,
    #     10194597,
    #     10194598,
    #     10194599,
    #     10194600,
    #     10194601,
    #     10194602,
    #     10194603,
    #     10194604,
    #     10194605
    # ]:
    #     BossTransferToPerson().process(symbol="QQT",amount="1000",user=i)
    #     print(i,"--","充币完成")


    BossTransferToPerson().process(symbol="QQT", amount="400000", user="10194606")