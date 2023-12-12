import base64
import hashlib
import hmac
import json
import time
import asyncio
import websockets
import requests as requests
'''
现货测试环境ws ip=ws://testwss.qkex.com/
orderbook={"event":"sub","params":{"zip":false,"pairCode":"BTC_USDT","biz":"exchange","type":"orderBook"}}
candles={"event":"sub","params":{"biz":"exchange","type":"candles","pairCode":"BTC_USDT","index":"USDT","interval":"15min","since":1682390087566,"zip":false}}
'''
api_key = "e4288533dc26663aa699b9b0037b1a360"
api_secret = "7ec8f76207300a576622705358a922d49b7858eaf2207fd8e153a978a3bb7644"
api_passphrase = "test123"
base_url = 'http://test-public-rest.abcdefg123.info'


# 下单函数，用于创建订单
def placeOrder(symbol, side, price, volume, systemOrderType):
  path = '/openapi/exchange/' + symbol + '/bulkOrders'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = [{
    "side": side,
    "price": price,
    "volume": volume,
    "systemOrderType": systemOrderType
  }]
  data_json = json.dumps(data)
  print(data_json)
  signature = sign(now, 'POST', path, '', data_json)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "zh-HK"
  }
  response = requests.request('POST', url, headers=headers, data=data_json)
  jsonStr=response.json()
  print(jsonStr)
  return
# 获取交易对信息
def currency():
  path = '/openapi/exchange/public/currencies'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = {}
  # data_json = json.dumps(data)
  #
  # print(data_json)
  signature = sign(now, 'GET', path, '', '')
  # signature = sign(now, 'GET', path, '', data_json)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "en-US"
  }
  response = requests.request('GET', url, headers=headers)
  jsonStr=response.json()
  print(jsonStr)
  return
# 获取指定交易对的信息
def getCurrency(pairCode):
  path = '/openapi/exchange/public/getCurrency?pairCode='+pairCode
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  # data = {'pairCode':pairCode}
  # data_json = json.dumps(data)
  #
  # print(data_json)
  signature = sign(now, 'GET', path, '', '')
  # signature = sign(now, 'GET', path, '', data_json)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "en-US"
  }
  response = requests.request('GET', url, headers=headers)
  jsonStr=response.json()
  print(jsonStr)
  return
# 获取订单信息
def getOrder(currency: object, orderId: object) -> object:
  path = '/openapi/exchange/'+currency+'/orders/'+str(orderId)
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  data = {}
  data_json = json.dumps(data)
  print(url)
  signature = sign(now, 'GET', path, '', data_json)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "en-US"
  }
  response = requests.request('GET', url, headers=headers, data=data_json)
  jsonStr=response.json()
  print(jsonStr)
  return
# 获取指定交易对的行情信息
def ticker(currency):
  path = '/openapi/exchange/public/'+currency+'/ticker'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  signature = sign(now, 'GET', path, '', '')
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "en-US"
  }
  response = requests.request('GET', url, headers=headers)
  jsonStr=response.json()
  print(jsonStr)
  return
# 获取指定交易对的 K 线数据
def kline(currency):
  path = '/openapi/exchange/public/'+currency+'/candles?interval=1hour'
  url = base_url + path
  timestamp = time.time()
  now = int(timestamp * 1000)
  signature = sign(now, 'GET', path, '', '')
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json",
    "Cookie": "locale=en-US",
    "x-locale": "en-US"
  }
  response = requests.request('GET', url, headers=headers)
  jsonStr=response.json()
  print(jsonStr)
  return
# 生成签名
def sign(timestamp, method, requestPath, queryString, body):
  if len(queryString) == 0:
    queryString = ""
  else:
    queryString = "?" + queryString
  preHash = str(timestamp) + method + requestPath + queryString + body
  print(preHash)
  signature = base64.b64encode(
      hmac.new(api_secret.encode('utf-8'), preHash.encode('utf-8'),
               hashlib.sha256).digest())
  print(signature)
  return signature
# WebSocket 客户端，用于订阅数据
async def ws_client(url):
  data = {"event": "sub",
          "params": {"zip": False, "pairCode": "BTC_USDT", "biz": "exchange",
                     "type": "orderBook"}}
  async with websockets.connect(url) as websocket:
    await websocket.send(json.dumps(data))
    while True:
      response = await websocket.recv()
      print(response)




# asyncio.run(ws_client('ws://testwss.qkex.com'))
#
# placeOrder('BTC_USDT', 'buy', '0.403', '1', 'limit')
# currency()
# getCurrency('BTC_USDT')
# getOrder('BTC_USDT',188226362153024)
# ticker('BTC_USDT')
# kline('BTC_USDT')

if __name__ == '__main__':
    # placeOrder('BTC_USDT', 'buy', '0.403', '1', 'limit')
    currency()