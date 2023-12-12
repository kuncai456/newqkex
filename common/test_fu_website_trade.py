import pytest
import hmac
import json
import time
import requests as requests
import hashlib
# api_key = "aff1d248c82270d65ed63683fc55e2b2"
api_key = "58674e5cc769ebf393b33e656a3325fe"
# api_secret = "a14b1305418a9e689e64b90623f74a39406201627a8c8eb988b6af797057f5fb"
api_secret = "88b8bc2e7f42db839d80e12503837800f75643e2b11c070f9d73c88d122b4914"
# api_passphrase = "f4fcf5713475d2c012905f379991d5cc400029046632e2654ccc2c1e00a055ea"
api_passphrase = "a2762abfa6999c411ddf75ad76b84bac71665e3370da1ec42af7eddf8e3658e7"
base_url = 'http://test-futures-rest.abcdefg123.info'



# OpenApi函数，资金查询接口
def test_tradefun():
  path = '/v1/trade/tradingAccount'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ""
  signature = sign(now, 'GET', path,  data)
  print(signature)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers)
  jsonStr=response.json()
  print(jsonStr)
  return

#OpenApi杠杆，切换杠杆
def test_tradeleverage():
  path = '/v1/trade/leverage'
  url = base_url + path
  now = str(int(time.time() * 1000))
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
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  print(response.text)
  return

#OpenApi杠杆，获取用户当前杠杆
def test_tradeleverage_info():
  path = '/v1/trade/leverage/info'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ''
  signature = sign(now, 'GET', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,单个下单
def test_orderstes():
  path = '/v1/trade/orders'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
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
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# OpenApi订单,批量下单
def test_batchOrders():
  path = '/v1/trade/batchOrders/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "data": {},
  "startTime": 0
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单, 单个撤单
def test_orders_cancel():
  path = '/v1/trade/orders/cancel/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "tradeType": "linearSwap",
  "symbol": "BTCUSDT",
  "orderId": "",
  "clOrdId": "",
  "currency": "",
  "startTime": 0
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,批量撤单
def test_orders_batchCancelOrders():
  path = '/v1/trade/orders/batchCancelOrders/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "data": {},
  "startTime": 0
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,一键撤单
def test_orders_oneClickCancels():
  path = '/v1/trade/orders/oneClickCancel/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT"
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# OpenApi订单,查看当前委托
def test_openOrders():
  path = '/v1/trade/openOrders'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ''
  signature = sign(now, 'GET', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi持仓, 持仓查询接口
def test_position():
  path = '/v1/trade/position/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ''
  signature = sign(now, 'GET', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi持仓, 调整逐仓保证金
def test_position_margin():
  path = '/v1/trade/position/margin/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "tradeType": "linearPerpetual",
  "symbol": "BTCUSDT",
  "positionSide": "long",
  "amount": "1.5",
  "type": 1
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi 查看风险限额,查看风险限额-与仓位挂单对应档位
def test_riskLimit():
  path = '/v1/trade/riskLimit/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ''
  signature = sign(now, 'GET', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openapi 划转,web发起划转
def test_account_transfer():
  path = '/v1/trade/account/transfer/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "fromAccountType": "funding",
  "toAccountType": "futures",
  "currency": "USDT",
  "amount": "2.666666"
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": str(now),
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openApi 计划委托,计划委托下单
def test_stopOrders():
  path = '/v1/trade/stopOrders/'
  url = base_url + path
  now = str(int(time.time() * 1000))
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
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# openApi 计划委托,计划委托撤单
def test_stopOrders_cancel():
  path = '/v1/trade/stopOrders/cancel/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = json.dumps({
  "stopOrderId": "",
  "clOrdId": "",
  "tradeType": "",
  "symbol": ""
})
  signature = sign(now, 'POST', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('POST', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return

# openApi 计划委托,查询未触发计划委托
def test_stopOrders_search():
  path = '/v1/trade/stopOrders/search/'
  url = base_url + path
  now = str(int(time.time() * 1000))
  data = ''
  signature = sign(now, 'GET', path, data)
  headers = {
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": now,
    "ACCESS-KEY": api_key,
    "ACCESS-PASSPHRASE": api_passphrase,
    'source': 'api',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json'
  }
  response = requests.request('GET', url, headers=headers, data=data)
  jsonStr=response.json()
  print(jsonStr)
  return


# 生成签名
def sign(now, method, requestPath, data):
  if data == "":
    preHash = now + method + requestPath
  else:
    preHash = now + method + requestPath + data
  print(preHash)
  signature = hmac.new(api_secret.encode('utf-8'), preHash.encode('utf-8'), hashlib.sha256).hexdigest()
  return signature

if __name__ == '__main__':
    pytest.main()

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
#     SYSTEM_ERROR(40009)
