import base64

import requests


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5


def registe():
    url1="http://test-public-rest.qkex.com/user/send-code/email"
    data1={"type":2,"email":"8114Ma@163.com","countdownType":"emailSignUp"}
    url="http://test-public-rest.qkex.com/user/reg/email"
    password='"'+get_token()+'"'
    data={"email":"8144Ma@163.com",
          "verifyCode":"111111",
          # "password":"GNNMsg8Fes/wHmhdD3nEUqospT1fwxQys/9sqrQYcApm9Ne6T0kZZGkjSwXHiDXOhgwCzxoFFLW0+tehvigjj1X563nYN5QVvG8xOvo+zFvAx+HzSCB3ZLByMKgi0tSSfYXrAGZry+j/VEdOFTYJXmS1LlDhv5vXRGrWuli0B/S8/3xUBUhxgJaXA+9LNOkFPOFK6X6G6Bbrxw+AxJLkjCfT2IX8IOpEbGgTSS1xZZoftzkFRblOxiXHoFib3gNfO5qdGQea3kqSLIkBk8sSweu6s9zgFuoaL950kx8gPfcgxoeHwDqfrNBGaYe4MSG9A9We/ppzdh+3d4gTxqpfGA==",
          "password": password,
          # "confirmPassword":"GNNMsg8Fes/wHmhdD3nEUqospT1fwxQys/9sqrQYcApm9Ne6T0kZZGkjSwXHiDXOhgwCzxoFFLW0+tehvigjj1X563nYN5QVvG8xOvo+zFvAx+HzSCB3ZLByMKgi0tSSfYXrAGZry+j/VEdOFTYJXmS1LlDhv5vXRGrWuli0B/S8/3xUBUhxgJaXA+9LNOkFPOFK6X6G6Bbrxw+AxJLkjCfT2IX8IOpEbGgTSS1xZZoftzkFRblOxiXHoFib3gNfO5qdGQea3kqSLIkBk8sSweu6s9zgFuoaL950kx8gPfcgxoeHwDqfrNBGaYe4MSG9A9We/ppzdh+3d4gTxqpfGA==",
          "confirmPassword": password,
          "agreement":"1",
          "areaCode":86,
          "verificationCode":""}
    headers={"Content-Type":"application/json",
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
             "X-Locale":"zh-HK"}
    res1=requests.request(method="post",url=url1,json=data1,headers=headers)
    print(res1.json())
    res=requests.request(method="post",url=url,json=data,headers=headers)
    print(res.json())
    # ste="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo5ZPAsOoRZSc7XHPXj0Y" \
    #     "xt8YrE/Kmg34BGctMSamn6d9LbqhF8vyeWVlBtpo4xjBrQLGl3kxoe7bhTX1YYG4" \
    #     "8z84/HHqPVk7MFlXILoHhIXt7x3saisL/BUN2s2ga92wLqBzJkieCUFXOFqC+QIl" \
    #     "hwL+zOu6bJPtjTX2r6fr2iZvGi0D7uzE9Q9H8VNV48jFIzN8lr02kU/LiAoA7NAM" \
    #     "8ZrgfV3xhDLSWFXUH/Geo10v6IzT5Dl5kdTZOPaQijcJkYazygBOsa9PEnT89GMW" \
    #     "61axPzdbV5IdlFNLuHBQCXUXixdpfeC0qswEk16nJGWZfMLmXj/A6HxgTM9Mx+PT"\
    #     "pQIDAQAB"

def get_token():
    with open('public_key.pem') as f:
        public_key = RSA.import_key(f.read())

    message="qa123456".encode("utf-8")
    cipher=PKCS1_v1_5.new(public_key)
    encrypted_data= base64.b64encode(cipher.encrypt(message))
    print("加密前的原文：", message)
    print("加密后的密文：", encrypted_data.hex())
    return encrypted_data.hex()
if __name__ == '__main__':
    # get_token()
    registe()