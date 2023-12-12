import json
import random
import time

import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

from common.boss_transfer_to_person import BossTransferToPerson

urllib3.disable_warnings()




class Login:

    def login(self, user, password):
        url = "http://test-public-rest.abcdefg123.website/user/login"
        headers = {"Content-Type": "application/json"}
        data = {"account": user, "password": password,
                "verifyCode": "111111"}

        rep = requests.request(method="post", json=data, url=url, headers=headers, verify=False)
        # print(rep.json())
        return rep.json()["data"]["accessToken"]


class KYCCommit:
    def __init__(self,user,password):
        self.Authorization=Login().login(user,password)
        # self.Authorization="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MDEwZGIzMy0xOTdmLTRlYzYtYmMwMy03Nzc2NzgyYmQwYjYxODI5NjE4MDA3IiwidWlkIjoiUVY0U3lPK2ZvemtvK0ZuWklyeE85QT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiIvY2s4bE52T0JwME5WanNoSUhDSG5RPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MTQwMDQyOSwiZXhwIjoxNjkxNDg2ODI5LCJpc3MiOiJ3Y3MifQ.HRTofaT77i4GTT0GsDBeq6qw_nUYQjLEL5xpE2rYa0M"
        self.headers={"Content-Type":"application/json",
                      "X-Locale":"zh-HK",
                      "X-Authorization":self.Authorization,
                      "Source":"web"}

    def commit_kyc_upload(self,type):
        import requests

        url = "http://test-public-rest.abcdefg123.info/user/kyc/upload/v2"
        #type 1:正面照，2：背面照，4:手持证件照
        payload = {'type': type}
        files = [
            ('file',
             ('QQ图片20230808101221.jpg', open('C:/Users/86186/Desktop/QQ图片20230808101221.jpg', 'rb'), 'image/jpeg'))
        ]
        headers = {
            'Connection': 'keep-alive',
            # 'Cookie': 'locale=en-US; _ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701508338.12.1.1701508349.49.0.0',
            'Origin': 'http://test.abcdefg123.info',
            'Referer': 'http://test.abcdefg123.info/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'accept': 'application/json, */*',
            'accept-language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'x-authorization': self.Authorization,
            'x-locale': 'zh-HK'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.json())
        return response.json()

    def user_kyc_commit(self):
        n_threads=3
        list=[1,2,4]
        with ThreadPoolExecutor(max_workers=n_threads) as pool:

            frontImg1=pool.submit(self.commit_kyc_upload,1)
            # print("frontImg1",frontImg1.result())
            backImg1=pool.submit(self.commit_kyc_upload,2)
            # print("backImg1", backImg1.result())
            handsImg1=pool.submit(self.commit_kyc_upload,4)
            print("handsImg1", handsImg1.result())
            # results=pool.map(self.user_kyc_commit,list)



        frontImg=frontImg1.result()["data"]["fileName"]
        print("frontImg",frontImg)
        backImg=backImg1.result()["data"]["fileName"]
        print("backImg1", backImg)
        handsImg=handsImg1.result()["data"]["fileName"]
        print("handsImg",handsImg)


        url = "http://test-public-rest.abcdefg123.info/user/kyc/info/save"
        num = random.randint(1000000000, 9999999999)
        num1 = random.randint(1000, 9999)
        payload = json.dumps({
            "firstName": "test"+str(num1),
            "lastName": "test"+str(num1),
            "cardType": "id_card",
            "cardNumber": str(num),
            "birthDay": "12/02/2023",
            "countryCode": "8",
            "frontImg": frontImg,
            "backImg": backImg,
            "handsImg": handsImg
        })
        print("payload:",payload)
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': 'locale=en-US; _ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701508338.12.1.1701508349.49.0.0',
            'Origin': 'http://test.abcdefg123.info',
            'Referer': 'http://test.abcdefg123.info/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Authorization': self.Authorization,
            'X-Lang': 'zh-HK',
            'x-locale': 'zh-HK'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    def get_uid(self):
        url = "http://test-public-rest.abcdefg123.info/user/detail"
        headers = {
            'Content-Type': 'application/json',
            'X-Authorization':self.Authorization
        }

        response = requests.request("Get", url, headers=headers)

        print(response.json())
        uid = response.json()['data']["userId"]
        return uid

class KYCCommitProcess:
    def __init__(self,user,password):
        self.user=user
        self.password=password
    def process(self):
        try:

            #登录
            user=KYCCommit(user=self.user,password=self.password)

            #提交kyc
            user.user_kyc_commit()

            #获取uid
            uid=user.get_uid()

            #登录boss
            Cookie = BossTransferToPerson().boss_login().headers["Set-Cookie"]

            #获取kyc审核列表
            res=BossTransferToPerson().get_kyc_aply_list(uid,Cookie)
            #审核kyc
            id=res["data"]["rows"][0]["id"]
            userId=uid
            level=res["data"]["rows"][0]["level"]
            countryCode=res["data"]["rows"][0]["countryCode"]
            email=self.user
            googleVerifyCode=BossTransferToPerson().read_google_authenticator_code()

            res=BossTransferToPerson().kyc_pass(id=id,userId=userId,level=level,countryCode=countryCode,email=email,googleVerifyCode=googleVerifyCode,Cookie=Cookie)
            print(res)
            print(uid,"---",email,"---","审核成功")
            return res

        except Exception as e:
            print("错误",e)


if __name__ == '__main__':
    # user=KYCCommit(user="d1011Ma@163.com",password="qa123456")
    # user.user_kyc_commit()
    user=KYCCommitProcess(user="dd109@163.com",password="qa123456")
    user.process()
    # for i in [
    #     "dd1071@163.com ",
    #     "dd1072@163.com ",
    #     "dd1073@163.com ",
    #     "dd1074@163.com ",
    #     "dd1075@163.com ",
    #     "dd1076@163.com ",
    #     "dd1077@163.com ",
    #     "dd1078@163.com ",
    #     "dd1079@163.com ",
    # ]:
    #     user = KYCCommitProcess(user=i, password="qa123456")
    #     user.process()