import json
from time import sleep

import requests

from common.boss_transfer_to_person import BossTransferToPerson


def user_regist(email):

    email_url= "http://test-public-rest.abcdefg123.info/user/send-code/email"

    payload1 = json.dumps({
        "type": 2,
        "email": email,
        "countdownType": "emailSignUp"
    })
    headers1 = {
        'Content-Type': 'application/json',
        'Cookie': 'locale=zh-HK'
    }
    response = requests.request("POST", email_url, headers=headers1, data=payload1)
    print(response.text)

    url = "http://test-public-rest.abcdefg123.info/user/reg/email"

    payload = json.dumps({
      "email": email,
      "verifyCode": "111111",
      "password": "QK4wM729u6jI79lrTOu0b407guahsRDxpu+LfWRf2VDty7jcaJ3EjhEmcElx0zXlYBUy+axdCImQWE+D1u9TdtraEqF19aESOSu5dIJPH1dRSE2rt7khTDA/gOUQzS4397XgCtVskIc/m4BUoJjvrzdSGxIzgdzafomaxkc2ShC47Q6u0FWTv2TV8Z28yL3ckwdL+f1bCXI5N/7SbKtdiPk4z/DYLw53VLDUeTv5F9Z/7Ht4hy4bdyZuZty2ImGrQvc0PRP+kXuA2hLDyrE+Ycv/Bf71Kf3GovNQ76vtBe0jZ63xPnzgiCPRpzQ5dhllMPeRJIWzkoueeBCW7Gowhg==",
      "confirmPassword": "QK4wM729u6jI79lrTOu0b407guahsRDxpu+LfWRf2VDty7jcaJ3EjhEmcElx0zXlYBUy+axdCImQWE+D1u9TdtraEqF19aESOSu5dIJPH1dRSE2rt7khTDA/gOUQzS4397XgCtVskIc/m4BUoJjvrzdSGxIzgdzafomaxkc2ShC47Q6u0FWTv2TV8Z28yL3ckwdL+f1bCXI5N/7SbKtdiPk4z/DYLw53VLDUeTv5F9Z/7Ht4hy4bdyZuZty2ImGrQvc0PRP+kXuA2hLDyrE+Ycv/Bf71Kf3GovNQ76vtBe0jZ63xPnzgiCPRpzQ5dhllMPeRJIWzkoueeBCW7Gowhg==",
      "agreement": "1",
      "areaCode": 86,
      # "verificationCode": ""
    })
    headers = {
      'Content-Type': 'application/json',
      'Cookie': 'locale=zh-HK'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.json()

def get_regist_uid(email):
    try:
        data=user_regist(email)
        if data["code"] !=0:
            raise ValueError("注册接口报错",data)
        else:
            accessToken=data['data']['accessToken']
            print(accessToken)
            url="http://test-public-rest.abcdefg123.info/user/detail"
            headers = {
                'Content-Type': 'application/json',
                'X-Authorization': accessToken
            }

            response = requests.request("Get", url, headers=headers)

            print(response.json())
            uid=response.json()['data']["userId"]
            print(email,"  ",uid)
            # BossTransferToPerson().process(symbol="QQT", amount="10000", user=uid)

            #生成邀请关系

            url = "http://test-invite.abcdefg123.info/api/scenarios/list"

            payload = {}
            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Cookie': '_ga=GA1.1.1658184569.1701309730; _ga_BC2SP908YM=GS1.1.1701607829.16.1.1701607844.45.0.0',
                'Origin': 'http://test.abcdefg123.info',
                'Referer': 'http://test.abcdefg123.info/',
                'Source': 'web',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'X-Authorization': accessToken,
                'X-Lang': 'zh-HK',
                'x-locale': 'zh-HK'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            print(response.text)


    except Exception as e:
        print("错误",e)
if __name__ == '__main__':
    # user_regist("80091Ma@163.com")
    # get_regist_uid("dd109@163.com")
    email1="7000112"
    for i in range(10000):
        email=email1+str(i)+str("@163.com")
        print(email)
        get_regist_uid(email)
