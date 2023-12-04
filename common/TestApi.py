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


api_key = "ec26abc7cf85004651c99def7b456137"
api_secret = "0516daeef962dce3216d160b95a57481cc6dc7d59080be5c9918273f4ff2502c"
api_passphrase = "test123"

base_url = 'http://test-public-rest.qkex.com'


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
    "x-locale": "en-US"
  }
  response = requests.request('POST', url, headers=headers, data=data_json)
  jsonStr=response.json()
  print(jsonStr)
  return


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
  print("currency",jsonStr)
  return


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
  return signature


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

currency()

getCurrency('BTC_USDT')

# getOrder('BTC_USDT',188226362153024)

# ticker('BTC_USDT')

kline('BTC_USDT')


