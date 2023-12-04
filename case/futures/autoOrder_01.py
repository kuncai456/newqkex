import random
import time

import requests
import urllib3

urllib3.disable_warnings()
class AutoOrder:
    """
    摆盘
    """
    def __init__(self,user,password):
        self.Authorization=Login().login(user,password)
        # self.Authorization="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MDEwZGIzMy0xOTdmLTRlYzYtYmMwMy03Nzc2NzgyYmQwYjYxODI5NjE4MDA3IiwidWlkIjoiUVY0U3lPK2ZvemtvK0ZuWklyeE85QT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiIvY2s4bE52T0JwME5WanNoSUhDSG5RPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MTQwMDQyOSwiZXhwIjoxNjkxNDg2ODI5LCJpc3MiOiJ3Y3MifQ.HRTofaT77i4GTT0GsDBeq6qw_nUYQjLEL5xpE2rYa0M"
        self.headers={"Content-Type":"application/json",
                      "X-Locale":"zh-HK",
                      "X-Authorization":self.Authorization,
                      "Source":"web"}


    def buy_order(self,price):
        """
        开多
        :param price:
        :return:
        """
        url="http://test-futures-rest.qkex.com/v1/trade/web/orders"
        data={"tradeType":"linearPerpetual",
              "symbol":"BTCUSDT",
              "side":"buy",
              "positionSide":"long",
              "orderType":"limit",
              "orderQty":"10",
              "marginType":"cross",
              "postOnly":False,
              "timeInForce":"GTC",
              "price":price}
        response=requests.request(method="post",url=url,json=data,headers=self.headers,verify=False)
        print("做多成功，价格为：",price)
        return response.json()


    def sell_order(self,price):
        """
        开空
        :param price:
        :return:
        """
        url="http://test-futures-rest.qkex.com/v1/trade/web/orders"
        data={"tradeType":"linearPerpetual",
              "symbol":"BTCUSDT",
              "side":"sell",
              "positionSide":"short",
              "orderType":"limit",
              "orderQty":"10",
              "marginType":"cross",
              "postOnly":False,
              "timeInForce":"GTC",
              "price":price}
        response=requests.request(method="post",url=url,json=data,headers=self.headers,verify=False)
        print("做空成功，价格为：",price)
        return response.json()

    def get_price(self):
        """
        获取价格
        :return:
        """
        url="http://test-futures-rest.qkex.com/v1/market/ticker/24hr?symbol=BTCUSDT&tradeType=linearPerpetual"
        res=requests.request(method="get",url=url)
        return res.json()


    def get_openOrders(self):
        """
        获取委托列表
        :return:
        """
        url="http://test-futures-rest.qkex.com/v1/trade/web/openOrders?tradeType=linearPerpetual&pageNum=1&pageSize=100"
        res=requests.request(method="get",url=url,headers=self.headers)
        print("委托列表",res.json())
        return res.json()
    def do_oneClickCancel(self):
        """
        一键撤单
        :return:
        """
        url = "http://test-futures-rest.qkex.com/v1/trade/web/orders/oneClickCancel"
        data = {"tradeType":"linearPerpetual"}
        response = requests.request(method="post", url=url, json=data, headers=self.headers, verify=False)
        print("一键撤单成功")
        return response.json()

    def do_oneClickClose(self):
        """一键平仓"""
        url="http://test-futures-rest.qkex.info/v1/trade/web/oneClickClose"
        data={"tradeType":"linearPerpetual"}
        response=requests.request(method="post", url=url, json=data, headers=self.headers, verify=False)
        print("一键平仓成功")
        return response.json()

class Login:

    def login(self, user, password):
        url = "http://test-public-rest.qkex.com/user/login"
        headers = {"Content-Type": "application/json"}
        data = {"account": user, "password": password,
                "verifyCode": "111111"}

        rep = requests.request(method="post", json=data, url=url, headers=headers, verify=False)
        print(rep.json())
        return rep.json()["data"]["accessToken"]

class AutoProcess:
    def process(self):
        while True:
            try:
                user=AutoOrder(user="800956Ma@163.com",password="qa123456")
                n=0
                while True:
                    if n%10!=0:
                        if (int(user.get_openOrders()['data']["totalSize"])<50):
                            price=user.get_price()["data"][0]["lastPrice"]
                            # offset=random.random(0,1)
                            # price_order=float(price)+round(offset,2)
                            side_list=["buy","sell"]
                            if random.choice(side_list)=="buy":
                                offset = random.random()
                                price_order = float(price) + round(offset, 2)
                                #做多
                                user.buy_order(price_order)
                            else:
                                offset = random.random()
                                price_order = float(price) - round(offset, 2)
                                #做空
                                user.sell_order(price_order)


                        else:
                            #一键撤单
                            user.do_oneClickCancel()

                    if n%10 == 0:
                        #一键平仓
                        user.do_oneClickClose()
                    n+=1
            except Exception as e:
                print("错误:",e)
if __name__ == '__main__':
    # print(AutoOrder(user="697Ma@163.com",password="qa123456").get_price())
    AutoProcess().process()
