import requests
from common import googleCode as gc
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Cookie":"token=c7ebd817-d668-46eb-a80f-d5de9cd2f866; expire_time=20211029155728",
               "Accept": "application/json, text/plain, */*","Content-Type":"application/json","Connection":"close","Accept-Language":"zh-CN","X-Authorization":"","language":"Chinese"}
# Authorization='eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5MmU0Y2Y4ZC1hODdmLTQ4MTgtODJmMS0xNDgxYjYwOTRhMTAxMTEyODg0ODYzIiwidWlkIjoic1F6S2RTODJUN0dDeEluck1XSDBpUT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiI4NFJ2dzRsWUo3SUZUamdLTDFZbjJ3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY3ODE4MDg3NywiZXhwIjoxNjc4MjY3Mjc3LCJpc3MiOiJ3Y3MifQ.mZjUU6EYebXG-NijCZ80bMKeCE_1f24sMnR89tIgEUo'
# headers['X-Authorization']=Authorization
url = 'http://13.215.135.141'
account='10086@qq.com'
password='aa123456'


#登录
def userLoginVerify(account,password):
    params = {
        'account':account,
        'password':password,
    }
    path='/user/login/verify'
    # session = requests.Session()
    # session.post(url + path, data=params)
    # request_cookies = session.cookies.get_dict()
    # request_cookies = 'JSESSIONID=' + request_cookies['JSESSIONID']
    # headers['Cookie']=request_cookies
    res =requests.post(url=url+path,json=params,headers=headers).json()
    return res
def userLogin(account,password,verifyCode):
    params = {
        'account': account,
        'password': password,
        'verifyCode':verifyCode
    }
    path = '/user/login'
    res = requests.post(url=url + path, json=params, headers=headers).json()
    return res


def aaa():
    userLoginVerify(account,password)
    code = gc.get_google_code()
    res = userLogin(account,password,verifyCode=code)
    return res

if __name__ == '__main__':
    print(aaa())