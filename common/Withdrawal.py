import json
import time

import pyotp
import requests

from common.bind_googleVerifyCode import Login
from common.mysql_san import mysql_select


def withdrawal(address,googleVerifyCode):

    url = "http://test-public-rest.abcdefg123.info/user/user-send-code"

    payload = json.dumps({
        "type": "9"
    })
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_gid=GA1.2.1596252772.1702448896; _ga=GA1.1.43299971.1701914347; locale=zh-HK; _ga_BC2SP908YM=GS1.1.1702531098.32.1.1702531326.60.0.0',
        'Origin': 'http://test.abcdefg123.info',
        'Referer': 'http://test.abcdefg123.info/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMmFhYTIzOS0yNzU4LTRjYTktOGVhNi1jNWI5MjY0MDdjM2YxOTgwMzg0MDExIiwidWlkIjoiSGQrTUd1MXFyWjBvODZDOWo1VHpBUT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJTM1h6NU5WdVNkN0lBVkJNMlNRb2FnPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTcwMjUzNTY2MCwiZXhwIjoxNzAyNjIyMDYwLCJpc3MiOiJ3Y3MifQ.F1rdOYNOMvJTmHX9uiFuB5s8D1m7af2Bfr_uq7q4CEk',
        'X-Lang': 'zh-HK',
        'x-locale': 'zh-HK'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    url = f"http://test-public-rest.abcdefg123.info/wallet/withdraw?currency=QTT&address={address}&amount=100&verifyCode=111111&googleVerifyCode={googleVerifyCode}&agreementChannel=TRC20&withdrawFee=1"
    print("url,",url)
    payload = json.dumps({})
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_gid=GA1.2.1596252772.1702448896; _ga=GA1.1.43299971.1701914347; locale=zh-HK; _ga_BC2SP908YM=GS1.1.1702531098.32.1.1702531326.60.0.0',
        'Origin': 'http://test.abcdefg123.info',
        'Referer': 'http://test.abcdefg123.info/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Authorization': "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMmFhYTIzOS0yNzU4LTRjYTktOGVhNi1jNWI5MjY0MDdjM2YxOTgwMzg0MDExIiwidWlkIjoiSGQrTUd1MXFyWjBvODZDOWo1VHpBUT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJTM1h6NU5WdVNkN0lBVkJNMlNRb2FnPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTcwMjUzNTY2MCwiZXhwIjoxNzAyNjIyMDYwLCJpc3MiOiJ3Y3MifQ.F1rdOYNOMvJTmHX9uiFuB5s8D1m7af2Bfr_uq7q4CEk",
        'X-Lang': 'zh-HK',
        'x-locale': 'zh-HK'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
def read_google_authenticator_code():
    """
    读取并返回谷歌身份验证器的动态验证码
    :param secret_key: 谷歌身份验证器的密钥
    :return: 动态验证码
    """
    secret_key="HF23IXQ42EFDBTNR"
    totp = pyotp.TOTP(secret_key)
    current_time = int(time.time())
    return totp.at(current_time)


def generate_address(user):

    Authorization=Login().login(user, "qa123456")
    url = "http://test-public-rest.abcdefg123.info/wallet/deposit/address/QTT/TRC20"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_ga=GA1.1.2007675370.1702533236; locale=en-US; _ga_BC2SP908YM=GS1.1.1702533235.1.1.1702533329.52.0.0',
        'Origin': 'http://test.abcdefg123.info',
        'Referer': 'http://test.abcdefg123.info/',
        'Source': 'web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Authorization': Authorization,
        'X-Lang': 'en',
        'x-locale': 'en-US'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    # list=[
    #
    #     "70001120@163.com",
    #     "70001121@163.com",
    #     "70001122@163.com",
    #     "70001123@163.com",
    #     "70001124@163.com",
    #     "70001125@163.com",
    #     "70001126@163.com",
    #     "70001127@163.com",
    #     "70001128@163.com",
    #     "70001129@163.com",
    #     "700011210@163.com",
    #     "700011211@163.com",
    #     "700011212@163.com",
    #     "700011213@163.com",
    #     "700011214@163.com"
    # ]
    # for i in list:
    #     generate_address(i)

    sql="select address from wallet.qtt_trc20_address where id>8;"
    datas=mysql_select(sql,3)
    for i in datas:
        address=i[0]
        print("address:",address)
        time.sleep(10)
        googleVerifyCode=read_google_authenticator_code()
        withdrawal(address, googleVerifyCode)