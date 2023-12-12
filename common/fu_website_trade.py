import base64
import binascii
import hashlib
import hmac
import json
import time
import asyncio
import websockets
import requests as requests
# from Crypto.Hash import HMAC, SHA256

'''
合约测试环境ws ip=ws://testwss.qkex.website/#/home
orderbook={"event":"sub","params":{"zip":false,"pairCode":"BTC_USDT","biz":"exchange","type":"orderBook"}}
candles={"event":"sub","params":{"biz":"exchange","type":"candles","pairCode":"BTC_USDT","index":"USDT","interval":"15min","since":1682390087566,"zip":false}}
'''
# api_key = "aff1d248c82270d65ed63683fc55e2b2"
api_key = "58674e5cc769ebf393b33e656a3325fe"
# api_secret = "a14b1305418a9e689e64b90623f74a39406201627a8c8eb988b6af797057f5fb"
api_secret = "88b8bc2e7f42db839d80e12503837800f75643e2b11c070f9d73c88d122b4914"
# api_passphrase = "f4fcf5713475d2c012905f379991d5cc400029046632e2654ccc2c1e00a055ea"
api_passphrase = "a2762abfa6999c411ddf75ad76b84bac71665e3370da1ec42af7eddf8e3658e7"
base_url = 'http://test-futures-rest.abcdefg123.info'


# OpenApi函数，资金查询接口
def tradefun():
  path = '/v1/trade/web/tradingAccount/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = ''
  signature = sign(now, 'get', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  # jsonStr=response.json()
  print(response.text)
  return

#OpenApi杠杆，切换杠杆
def tradeleverage():
  path = '/v1/trade/web/leverage/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
    "tradeType": "linearPerpetual",
    "symbol": "BTCUSDT",
    "leverage": "10",
    "marginType": "cross"
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

#OpenApi杠杆，获取用户当前杠杆
def tradeleverage_info():
  path = '/v1/trade/web/leverage/info/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = ''
  signature = sign(now, 'get', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,单个下单
def orders():
  path = '/v1/trade/web/orders/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT",
  "side": "buy",
  "positionSide": "long",
  "orderType": "limit",
  "reduceOnly": False,
  "marginType": "cross",
  "price": "20000",
  "priceType": "optimalN",
  "orderQty": "1",
  "clOrdId": "123456",
  "postOnly": False,
  "timeInForce": "GTC",
  "currency": "",
  "startTime": 0
})
  signature = sign(now, 'POST', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,批量下单
def batchOrders():
  path = '/v1/trade/web/batchOrders/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "data": {},
  "startTime": 0
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单, 单个撤单
def orders_cancel():
  path = '/v1/trade/web/orders/cancel/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "tradeType": "linearSwap",
  "symbol": "BTCUSDT",
  "orderId": "",
  "clOrdId": "",
  "currency": "",
  "startTime": 0
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,批量撤单
def orders_batchCancelOrders():
  path = '/v1/trade/orders/batchCancelOrders/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "data": {},
  "startTime": 0
})
  print(data)
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  print(headers)
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,一键撤单
def orders_oneClickCancels():
  path = '/v1/trade/web/orders/oneClickCancel/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT"
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,查看当前委托
def openOrders():
  path = '/v1/trade/web/openOrders/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = ''
  signature = sign(now, 'get', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi持仓, 持仓查询接口
def position():
  path = '/v1/trade/web/position/'
  url = base_url + path
  timestamp = time.time()
  now = str(int(timestamp * 1000))
  data = ''
  signature = sign(now, 'GET', path,  data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi持仓, 调整逐仓保证金
def position_margin():
  path = '/v1/trade/web/position/margin/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT",
  "positionSide": "long",
  "amount": "1.5",
  "type": 1
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi 查看风险限额,查看风险限额-与仓位挂单对应档位
def riskLimit():
  path = '/v1/trade/web/riskLimit/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = ''
  signature = sign(now, 'get', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openapi 划转,web发起划转
def account_transfer():
  path = '/v1/trade/web/account/transfer/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "fromAccountType": "funding",
  "toAccountType": "futures",
  "currency": "USDT",
  "amount": "2.666666"
})
  signature = sign(now, 'POST', path, '', data)
  # headers = {
  #   "ACCESS-SIGN": signature,
  #   "ACCESS-TIMESTAMP": str(now),
  #   "ACCESS-KEY": api_key,
  #   "ACCESS-PASSPHRASE": api_passphrase,
  #   "Content-Type": "application/json",
  #   "x-locale": "zh-HK"
  # }
  headers = {
    'apiSecret': 'a14b1305418a9e689e64b90623f74a39406201627a8c8eb988b6af797057f5fb',
    'ACCESS-KEY': 'aff1d248c82270d65ed63683fc55e2b2',
    'ACCESS-PASSPHRASE': 'f4fcf5713475d2c012905f379991d5cc400029046632e2654ccc2c1e00a055ea',
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'ACCESS-SIGN': signature,
    'ACCESS-TIMESTAMP': str(now),
    'Content-Type': 'application/json'
  }

  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openApi 计划委托,计划委托下单
def stopOrders():
  path = '/v1/trade/web/stopOrders/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "tradeType": "",
  "symbol": "",
  "side": "",
  "positionSide": "",
  "marginType": "",
  "orderType": "",
  "price": "",
  "orderQty": "",
  "tpOrdPx": "",
  "slOrdPx": "",
  "ordPx": "",
  "tpTriggerPxType": "",
  "slTriggerPxType": "",
  "triggerPxType": "",
  "clOrdId": "",
  "timeInForce": ""
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openApi 计划委托,计划委托撤单
def stopOrders_cancel():
  path = '/v1/trade/web/stopOrders/cancel/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = json.dumps({
  "stopOrderId": "",
  "clOrdId": "",
  "tradeType": "",
  "symbol": ""
})
  signature = sign(now, 'post', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('post', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi 计划委托,查询未触发计划委托
def stopOrders_search():
  path = '/v1/trade/web/stopOrders/search/'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = ''
  signature = sign(now, 'get', path, '', data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK"
  }
  response = requests.request('get', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return



# 生成签名
def sign(now, method, requestPath, data):

  if data == "":
    preHash = now + method + requestPath
  else:
    preHash = str(now) + method.upper() + requestPath + data
  print(preHash)

  signature = hmac.new(api_secret.encode('utf-8'), preHash.encode('utf-8'), hashlib.sha256).hexdigest()

  # signature2 =hmac.new(api_secret.encode(encoding='UTF8'),message.encode(encoding='UTF8'),
  #                hashlib.sha256).hexdigest()

  print("signature2",signature)

  return signature
# # WebSocket 客户端，用于订阅数据
# async def ws_client(url):
#   data = {"event": "sub",
#           "params": {"zip": False, "pairCode": "BTC_USDT", "biz": "exchange",
#                      "type": "orderBook"}}
#   async with websockets.connect(url) as websocket:
#     await websocket.send(json.dumps(data))
#     while True:
#       response = await websocket.recv()
#       print(response)

# asyncio.run(ws_client('ws://testwss.abcdefg123.info/'))


# public enum OpenApiErrorCodeEnum {
#     /**
#      * "请求头"ACCESS_KEY"不能为空","ACCESS_KEY header is required"
#      */
#     ACCESS_KEY_EMPTY(40001),
#     /**
#      * "请求头"ACCESS_SIGN"不能为空","ACCESS_SIGN header is required"
#      */
#     ACCESS_SIGN_EMPTY(40002),
#     /**
#      * "请求头"ACCESS_TIMESTAMP"不能为空","ACCESS_TIMESTAMP header is required"
#      */
#     ACCESS_TIMESTAMP_EMPTY(40003),
#     /**
#      * "请求头"ACCESS_PASSPHRASE"不能为空","ACCESS_PASSPHRASE header is required"
#      */
#     ACCESS_PASSPHRASE_EMPTY(40004),
#     /**
#      * "无效的ACCESS_TIMESTAMP","Invalid ACCESS_TIMESTAMP"
#      */
#     INVALID_ACCESS_TIMESTAMP(40005),
#     /**
#      * "无效的ACCESS_KEY","Invalid ACCESS_KEY"
#      */
#     INVALID_ACCESS_KEY(40006),
#     /**
#      * "无效的Content_Type，请使用“application/json”格式","Invalid Content_Type, please use the application/json format"
#      */
#     INVALID_CONTENT_TYPE(40007),
#     /**
#      * "请求时间戳过期","Request timestamp expired"
#      */
#     ACCESS_TIMESTAMP_EXPIRED(40008),
#     /**
#      * "系统错误","System error"),
#      */
#     SYSTEM_ERROR(40009),


def leverege():
  path = '/v1/trade/leverage'
  url = base_url + path
  timestamp = time.time()
  now = str(int(timestamp * 1000))
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT",
  "leverage": "10",
  "marginType": "cross"
  })
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "x-locale": "zh-HK",
    "source":"api"
  }
  response = requests.request('post', url, headers=headers, data=data)
  # jsonStr=response.json()
  # print(jsonStr)
  print(response.text)
  return


def orderss():
  path = '/v1/trade/orders'
  url = base_url + path
  timestamp = str(int(time.time()*1000))
  # now = int(1702206163975)

  # url = "http://test-futures-rest.abcdefg123.info"
  # signature = sign(now, 'POST', path, '', data)
  payload = json.dumps({
    "tradeType": "linearPerpetual",
    "symbol": "BTCUSDT",
    "side": "sell",
    "positionSide": "short",
    "orderType": "market",
    "reduceOnly": False,
    "marginType": "cross",
    "price": "28324",
    "priceType": "optimalN",
    "orderQty": "55",
    "postOnly": False,
    "timeInForce": "IOC",
    "currency": ""
  })
  signature = sign(timestamp, 'POST', path,  payload)
  headers = {
    'apiSecret': api_secret,
    'ACCESS-KEY': api_key,
    'ACCESS-PASSPHRASE': api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'ACCESS-SIGN': signature,
    'ACCESS-TIMESTAMP': str(timestamp),
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)


if __name__ == '__main__':
  # position()
  # leverege()
  # orders()
  # sign("", "", "", "", "")
  # orderss()
  # account_transfer()
  orderss()