
import random
import time

import requests
import urllib3

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


class KYCCommit:
    def __init__(self,user,password):
        self.Authorization=Login().login(user,password)
        # self.Authorization="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MDEwZGIzMy0xOTdmLTRlYzYtYmMwMy03Nzc2NzgyYmQwYjYxODI5NjE4MDA3IiwidWlkIjoiUVY0U3lPK2ZvemtvK0ZuWklyeE85QT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiIvY2s4bE52T0JwME5WanNoSUhDSG5RPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MTQwMDQyOSwiZXhwIjoxNjkxNDg2ODI5LCJpc3MiOiJ3Y3MifQ.HRTofaT77i4GTT0GsDBeq6qw_nUYQjLEL5xpE2rYa0M"
        self.headers={"Content-Type":"application/json",
                      "X-Locale":"zh-HK",
                      "X-Authorization":self.Authorization,
                      "Source":"web"}


    def user_exchange_order(self):
        """
        开多
        :param price:
        :return:
        """
        url="http://test-public-rest.qkex.website/exchange/BTC_USDT/orders"
        data={"systemOrderType":"market","side":"buy","volume":"","quoteVolume":"344.58","source":"web","price":""}
        response=requests.request(method="post",url=url,json=data,headers=self.headers,verify=False)
        # print("做多成功，价格为：",price)
        print("下单成功",response.json())
        return response.json()

if __name__ == '__main__':
    for i in [
        "b1011Ma@163.com",
        "b1012Ma@163.com",
        "b1013Ma@163.com",
        "b1014Ma@163.com",
        "b1015Ma@163.com",
        "b1016Ma@163.com",
        "b1017Ma@163.com",
        "b1018Ma@163.com",
        "b1019Ma@163.com",
        "b10110Ma@163.com",
    ]:

        user=KYCCommit(user=i,password="qa123456")
        user.user_exchange_order()
        print(i," --- ","现货下单完成")