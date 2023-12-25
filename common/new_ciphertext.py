import base64
import json

import Crypto
from Crypto.Cipher import AES




pad = lambda s: s + chr(16 - len(s) % 16) * (16 - len(s) % 16)
unpad = lambda s: s[:-s[-1]]





def aes_CBC_Encrypt(data, key, iv):  # CBC模式的加密函数，data为明文，key为16字节密钥,iv为偏移量
    key = key
    print("key,",key)
    iv = iv.encode('utf-8')  # CBC 模式下的偏移量
    print('iv,',iv)
    data = pad(data)  # 补位
    data = data.encode('utf-8')
    print("data,",data)
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)  # 创建加密对象
    # encrypt AES加密  B64encode为base64转二进制编码
    result = base64.b64encode(aes.encrypt(data))
    print(str(result, 'utf-8'))
    return str(result, 'utf-8')


def aes_CBC_Decrypt(data, key, iv):  # CBC模式的解密函数，data为密文，key为16字节密钥
    key = key
    iv = iv.encode('utf-8')
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)  # 创建解密对象

    # decrypt AES解密  B64decode为base64 转码
    result = aes.decrypt(base64.b64decode(data))
    result = unpad(result)  # 除去补16字节的多余字符
    # print("result,",result)
    print(str(result, 'utf-8'))
    return str(result, 'utf-8')




if __name__ == '__main__':
#     data=json.dumps({
#   "fromAccountType": "funding",
#   "toAccountType": "futures",
#   "currency": "USDT",
#   "amount": "10000"
# })
    data="tradeType=linearPerpetual&symbol=BTCUSDT&marginType=cross&orderType=triggerLimit&positionSide=long&side=buy&pageNum=1&pageSize=10"
    key=base64.b64decode("/IU7atGrDN+nwaAjTNJvFz01t8sCgV848p+b1i87VVQ=")
    iv="c3fuq7hrx3v1wi37"
    # payload=aes_CBC_Encrypt(data,key,iv)
    data1="2UgdomxKY/TiYEVqPQnxjgNl1shPXKOY93/uIKbaSCqj1nC+v7DOqyvj1Li+++wsaX2gC03b5Ia2Ka0GkV3I4DJOwO1CY1eKSqbK8TJpsxm14olIUz9671DDYYEnv5ulKM9+DWakuwQayFVKNV9jwgloW9Woz9edyobCczGMt42nEdLREKors1Bw0TiFW5iiO2X4jbmgDe6j33G9KAIcWBYmhIUWHBKWTjUHa3dzdS9weSm/K8z2nXkPmN0mmYV4gtyNmyUIbrajJw5J/kTsLwDOM/jSZ0L/a51c55K9V1OxPD5IaWcr9rQist56w7BNphZ2oLUpWmFapoXszIM04Xm4fAzlJZ96gOnzeMmFE51ADB2fGjOfd2i8y1Yg192zLMFLN/ILgJDvkZLjfzBmgnseEfaXfhkL28Mz4Osm7tQdMJ1TAstwywrHZIifut0kch59x6jzY/8D8gq1W8G71qSQfxAo9uN6BxIyKl5Kb3Xlp/sD8sHEqDGLAftIDsRQrTZwbnvDK5X9XTE9+P3Xz2vkZvVZyhy8Aq0kiXggZXp3x0REK5ANm3byo0G+sP7ms6Nkm7oh8+QkZ7N0Z5cxuoYtvT5FhyngEB4KLIG5IeZ/swtBC+QuHyv9PTbPyulRK92rtJwDsojfqZU0ZIYMswRehy7CYzy272hmkqWGGFsQP7MHRSgnXZBBi6DSJEm9WbYzm0rmeX5h5bK9lB8RxpGgcD3PvlvfU04Y03HhI396uqlArjrBhpa8Rkt4LJHDVIH5oBt9dtxPgxLLjyR1TM8G9zjO4rTIez7VzId15DnvuP79hYkhGbXustlRG1vY2vaosBY7/9+MoVIlE9DO4A=="
    aes_CBC_Decrypt(data1,key,iv)

    # import requests
    # import json
    #
    # url = "http://test-futures-rest.abcdefg123.info/v1/trade/web/orders"
    #
    # payload = payload
    # headers = {
    #     'x-locale': 'zh-CN',
    #     'source': 'web',
    #     'X-Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MTNiMmMwMS1lZjU2LTQ0NWUtYTAyZS02OGUxZmFhMTYxYTUxODAyNDM5MDM0IiwidWlkIjoiSGQrTUd1MXFyWjBvODZDOWo1VHpBUT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJTM1h6NU5WdVNkN0lBVkJNMlNRb2FnPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTcwMjg2NDc3NCwiZXhwIjoxNzAyOTUxMTc0LCJpc3MiOiJ3Y3MifQ.IxhKGu7kpjmQvXf8h6JTJCMHR5pPda_ZOOQ0mrk7Kn4',
    #     'ciphertext': 'true',
    #     'Content-Type': 'application/json'
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload)
    # data2=response.text
    # print(response.text)
    # aes_CBC_Decrypt(data2,key,iv)
