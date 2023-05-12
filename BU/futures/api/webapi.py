import copy
import requests

symbol = 'BTCUSDT';tradeType = 'linearPerpetual';side = 'buy';marginType = 'cross';positionSide = 'positionSide'
postOnly = 'false';reduceOnly = 'false';orderType = 'limit';priceType = 'optimalN';pageNum = '1';pageSize = '10'
headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN", "source": "web", "X-Authorization": ""}
Authorization = 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MjI0MzhiNy1jODRjLTQ5YWQtYjZkMS1jYzFhNjU3NWYwNmQxMzcwMjYyOTIxIiwidWlkIjoiT3dBa05jdFk5R1Jpcy9GekJaY2RkQT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJiaDBpVFlFS0VGNFZOT2lXc3FMUnN3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY4Mzg3ODI4NCwiZXhwIjoxNjgzOTY0Njg0LCJpc3MiOiJ3Y3MifQ.-N-qRUlZ8a6GRLtLpCpxnCXPqCDQEI2fgWxvSWWQQgg'
Authorization1 = 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlNTk4ZDBiOS1lOTcyLTQ1N2MtOWRmOS1lMTAyOGQ2MmM1Y2YxOTkyNDEyMzQzIiwidWlkIjoiaDBsVXZiR0t2SkdkdGVscGYxQWRZUT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJkRmxJM3RwSFdJdHpsNk9rTDRBSlBRPT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY4Mzc5MjQ0NiwiZXhwIjoxNjgzODc4ODQ2LCJpc3MiOiJ3Y3MifQ.IErDpB3ydg6mbOxbq6TlMA-0quPgzx6ep2uNkE0Q7nU'
headers['X-Authorization'] = Authorization
tradeurl = 'https://qraft-trade-api.qkex.com'
queryurl = 'https://qraft-trade-api.qkex.com'


# 划转
def web_transfer(fromAccountType=None, toAccountType=None, currency=None, amount=None):
    path = '/v1/trade/web/account/transfer'
    params = {
        "fromAccountType": fromAccountType,
        "toAccountType": toAccountType,
        "currency": currency,
        "amount": amount}
    res = requests.post(url=tradeurl + path, json=params, headers=headers).json()
    return res

# 单个下单
def web_order(tradeType=None, symbol=None, side=None, positionSide=None, orderType=None, reduceOnly=None,
                  marginType=None, price=None, priceType=None, orderQty=None, postOnly=None, timeInForce=None):
    path = '/v1/trade/web/orders'
    params = {"tradeType": tradeType,
              "symbol": symbol,
              "side": side,
              "positionSide": positionSide,
              "orderType": orderType,  # market，limit
              "reduceOnly": reduceOnly,
              "marginType": marginType,
              "price": price,
              "priceType": priceType,
              "orderQty": orderQty,
              "postOnly": postOnly,
              "timeInForce": timeInForce}  # GTC/IOC/FOK
    res = requests.post(url=tradeurl + path, json=params, headers=headers).json()
    return res

 # 一键平仓
def web_oneClickClose(tradeType=None, symbol=None):
    path = '/v1/trade/web/oneClickClose'
    params = {
        "tradeType": tradeType,
        "symbol": symbol}
    res = requests.post(url=tradeurl + path, json=params, headers=headers).json()
    return res


 # 查询持仓
def web_position(tradeType=None, symbol=None, marginType=None):
    path = '/v1/trade/web/position'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "marginType": marginType}
    res = requests.get(url=tradeurl + path, params=params, headers=headers).json()
    return res

 # 撤销单个订单
def web_orders_cancel(tradeType=None, symbol=None, orderId=None):
    path = '/v1/trade/web/orders/cancel'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "orderId": orderId}
    res = requests.post(url=tradeurl + path, json=params, headers=headers).json()
    return res


def web_orders_oneClickClose(tradeType=None, symbol=None):  # 一键撤销所有订单
    path = '/v1/trade/web/orders/oneClickCancel'
    params = {
        "tradeType": tradeType,
        "symbol": symbol}
    res = requests.post(url=tradeurl + path, json=params, headers=headers).json()
    return res

# 当前委托
def web_openOrders(tradeType=None, symbol=None, side=None, clOrdId=None, orderId=None, pageNum=None,
                       pageSize=None):
    path = '/v1/trade/web/openOrders'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "side": side,
        "orderId": orderId,
        "clOrdId": clOrdId,
        "pageNum": pageNum,
        "pageSize": pageSize}
    res = requests.get(url=tradeurl + path, params=params, headers=headers).json()
    return res


# 查询历史计划委托 /v1/trade/record/web/stopOrdersHistory
def web_stopOrdersHistory(tradeType=None, symbol=None, startTime=None, endTime=None, pageNum=None, pageSize=None,
                      marginType=None, orderType=None, stopOrderId=None):
    path = '/v1/trade/record/web/stopOrdersHistory'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "marginType": marginType,
        "orderType": orderType,
        "stopOrderId": stopOrderId
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 获取用户自选列表
def web_favorite(tradeType=None):
    path = '/v1/user/web/favorite'
    params = {
        "tradeType": tradeType
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 新增用户自选
def web_favorite_add(tradeType=None, symbolList=None):
    path = '/v1/user/web/favorite/add'
    params = {
        "tradeType": tradeType,
        "symbolList": symbolList
    }
    res = requests.post(url=queryurl + path, params=params, headers=headers).json()
    return res


# 取消用户自选
def web_favorite_delete(tradeType=None, symbolList=None):
    path = '/v1/user/web/favorite/delete'
    params = {
        "tradeType": tradeType,
        "symbolList": symbolList
    }
    res = requests.post(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询用户偏好设置/v1/user/web/favorite/setting/query
def web_favorite_setting_query(tradeType=None):
    path = '/v1/user/web/favorite/setting/query'
    params = {
        "tradeType": tradeType
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 更新用户偏好设置 /v1/user/web/favorite/setting/update
def web_favorite_setting_update(tradeType=None, preview=None, tradeUnit=None):
    path = '/v1/user/web/favorite/setting/update'
    params = {
        "tradeType": tradeType,
        "preview": preview,
        "tradeUnit": tradeUnit
    }
    res = requests.post(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询交易对列表 /v1/public/web/instruments
def web_instruments(tradeType=None, symbol=None):
    path = '/v1/public/web/instruments'
    params = {
        "tradeType": tradeType,
        "symbol": symbol
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询历史订单 /v1/trade/record/web/orders/history
def web_orders_history(tradeType=None, symbol=None, startTime=None, endTime=None, pageNum=None, pageSize=None,
                       side=None, orderType=None, orderId=None, clOrdId=None, orderStatus=None):
    path = '/v1/trade/record/web/orders/history'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "side": side,
        "orderType": orderType,
        "orderId": orderId,
        "clOrdId": clOrdId,
        "orderStatus": orderStatus
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询历史成交 /v1/trade/record/web/orders/fills
def web_orders_fills(tradeType=None, symbol=None, startTime=None, endTime=None, pageNum=None, pageSize=None,
                     side=None, orderType=None, orderId=None, clOrdId=None, tradeId=None):
    path = '/v1/trade/record/web/orders/fills'

    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "side": side,
        "orderType": orderType,
        "orderId": orderId,
        "clOrdId": clOrdId,
        "tradeId": tradeId
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询历史流水记录 /v1/trade/record/web/account/income
def web_account_income(tradeType=None, symbol=None, startTime=None, endTime=None, pageNum=None, pageSize=None,
                       incomeType=None, currency=None):
    path = '/v1/trade/record/web/account/income'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "incomeType": incomeType,
        "currency": currency
    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res


# 查询历史完全平仓记录 /v1/trade/record/web/position/closed
def web_position_closed(tradeType=None, symbol=None, startTime=None, endTime=None, pageNum=None, pageSize=None,
                        marginType=None, pnlType=None):
    path = '/v1/trade/record/web/position/closed'
    params = {
        "tradeType": tradeType,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "marginType": marginType,
        "pnlType": pnlType

    }
    res = requests.get(url=queryurl + path, params=params, headers=headers).json()
    return res
#/v1/trade/web/tradingAccount
def web_tradingAccount(currency=None):
    path = '/v1/trade/web/tradingAccount'
    params ={'currency':currency}
    res = requests.get(url=tradeurl+path,data=params,headers=headers).json()
    return res



if __name__ == '__main__':
    #print(web_order(tradeType,symbol,side,positionSide,orderType,reduceOnly))
    # print(web_openOrders(tradeType=tradeType, symbol=symbol))
    # print(web_position(tradeType, symbol, marginType))
    print(web_order())
