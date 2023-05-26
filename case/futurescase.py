symbol = 'BTCUSDT';tradeType = 'linearPerpetual';side = 'sell';marginType = 'cross';positionSide = 'short'
postOnly = None;reduceOnly = None;orderType = 'limit';priceType=None;pageNum = '1';pageSize = '10';timeInForce=None
fromAccountType='exchange';toAccountType='perpetual';currency='USDT';amount=40;pairCode='P_R_USDT_USD';gear='depth0';limit=1000;period='1m'##short，long
from BU.futures.api import webapi as wb
from common import util as ut
import random,time
def order_ad(use,side,positionSide):
    '''一键平仓、撤单
    当前资金、订单、持仓查询
    历史资金、订单、持仓查询'''
    user = wb.webapi(use, 'test')
    tradingAccount=user.web_tradingAccount()#资金查询
    if tradingAccount['code'] != '0':
        print(f"web_tradingAccount() failed with error code {tradingAccount['code']}: {tradingAccount['msg']}")

    else:
        print('资产接口',tradingAccount)
        # if 'currency' not in tradingAccount['data'][0] or 'marginEquity' not in tradingAccount['data'][0]:
        #     print("Error: tradingAccount response does not contain 'currency' or 'marginEquity' field")
    tra=user.web_transfer(fromAccountType=fromAccountType,toAccountType=toAccountType,currency=currency,amount=amount)
    if tra['code'] != 0:
        print(f"web_transfer() failed with error code {tra['code']}: {tra['msg']}")
    else:
        print('划转接口',tra)
    available=user.web_wallet_transfer(fromAccountType=fromAccountType,toAccountType=toAccountType,currency=currency,amount=amount,pairCode=pairCode,symbol=currency)#划转
    if available['code'] != 0:
        print(f"web_wallet_transfer() failed with error code {available['code']}: {available['msg']}")

    else:
        print('旧版本划转接口',available)
    # se=user.web_order(tradeType=tradeType, symbol=symbol, side=side, positionSide=positionSide, orderType=orderType, reduceOnly=reduceOnly,
    #               marginType=marginType, price='20042', priceType=priceType, orderQty=1, postOnly=postOnly, timeInForce=timeInForce)#下单
    # if se['code'] != '0':
    #     print(f"web_order() failed with error code {se['code']}: {se['msg']}")
    #
    # else:
    #     print('下单接口',se)
    op=user.web_position(tradeType=tradeType)
    if op['code'] != '0':
        print(f"web_position() failed with error code {op['code']}: {op['msg']}")

    else:
        print('持仓接口',op)
    w=user.web_openOrders(tradeType=tradeType) #当前委托
    if w['code'] != '0':
        print(f"web_openOrders() failed with error code {w['code']}: {w['msg']}")

    else:
        print('当前委托接口',w)
        # if 'list' in w['data'] and len(w['data']['list']) > 0:
        #     id=w['data']['list'][0]['orderId']
        #     if id is not None:
        #         cl=user.web_orders_cancel(tradeType=tradeType,orderId=id,symbol=symbol)#撤单
        #         if cl['code'] != '0':
        #             print(f"web_orders_cancel() failed with error code {cl['code']}: {cl['msg']}")
        #             return
        #         else:
        #             print('撤单接口',cl)
    ws=user.web_orders_history(tradeType=tradeType)
    if ws['code'] != '0':
        print(f"web_orders_history() failed with error code {ws['code']}: {ws['msg']}")

    else:
        print('历史委托接口', ws)
    clo=user.web_position_closed(tradeType=tradeType)
    if clo['code'] != '0':
        print(f"web_position_closed() failed with error code {clo['code']}: {clo['msg']}")

    else:
        print('历史仓位接口', clo)
    fle=user.web_orders_fills(tradeType=tradeType)
    if fle['code'] != '0':
        print(f"web_orders_fills() failed with error code {fle['code']}: {fle['msg']}")

    else:
        print('历史成交接口', fle)
    zij=user.web_account_income(tradeType=tradeType)
    if zij['code'] != '0':
        print(f"web_account_income() failed with error code {zij['code']}: {zij['msg']}")

    else:
        print('历史资金接口', zij)

    Close=user.web_orders_oneClickClose(tradeType=tradeType,symbol=symbol)
    if Close['code'] != '0':
        print(f"web_orders_oneClickClose() failed with error code {Close['code']}: {Close['msg']}")

    # cll=user.web_oneClickClose(tradeType=tradeType,symbol=symbol)
    # if cll['code'] != '0':
    #     print(f"web_oneClickClose() failed with error code {cll['code']}: {cll['msg']}")
    # else:
    #     print('一键平仓',cll)
    print('查询档位深度接口',user.web_market_depth(tradeType=tradeType,gear=gear,symbol=symbol,limit=limit))
    print('查询行情简化信息接口',user.web_market_ticker_mini(tradeType=tradeType,symbol=symbol,limit=limit))
    print('查询行情接口',user.web_market_ticker_24hr(tradeType=tradeType, symbol=symbol, limit=limit))
    print('历史成交接口',user.web_market_trade(tradeType=tradeType, symbol=symbol, limit=limit))
    print('k线接口',user.web_market_kline(tradeType=tradeType, symbol=symbol, limit=limit,period=period))
    lev=user.web_leverage(tradeType=tradeType,symbol=symbol,leverage=20,marginType=marginType)
    print('调整杠杆接口',lev)
    #stop=user.se

def order(use):
    user = wb.webapi(use, 'test')
    side1=['buy','sell']
    positionSide1=['long']
    price1=['20042.23','25000.34','21000.33']
    side=random.choice(side1);positionSide=random.choice(positionSide1);price=random.choice(price1)
    # se=user.web_order(tradeType=tradeType, symbol=symbol, side='buy', positionSide='long', orderType='market', reduceOnly=reduceOnly,
    #               marginType=marginType, price=price, priceType='optimalN', orderQty=3, postOnly=postOnly, timeInForce=timeInForce)#下单
    # if se['code'] != '0':
    #     print(f"web_order() failed with error code {se['code']}: {se['msg']}")
    ak=user.web_market_depth(tradeType=tradeType,gear=gear,symbol=symbol,limit=limit)
    cc=ak['data']['bids'];cc2=ak['data']['asks']
    aa=[float(x[0]) for x in cc]
    aa1=[float(x[0]) for x in cc2]
    print('买盘盘口',cc2)
    print('卖盘盘口',cc)
    print(max(aa),min(aa1))
    print('历史成交接口', user.web_market_trade(tradeType=tradeType, symbol=symbol, limit=limit))
    print('k线接口1m',user.web_market_kline(tradeType=tradeType, symbol=symbol, limit=limit,period='1m'))
    print('k线接口5m', user.web_market_kline(tradeType=tradeType, symbol=symbol, limit=limit, period='5m'))
    print('k线接口15m', user.web_market_kline(tradeType=tradeType, symbol=symbol, limit=limit, period='15m'))
    print('k线接口30m', user.web_market_kline(tradeType=tradeType, symbol=symbol, limit=limit, period='30m'))
    # ac1=(max(ak['data']['bids'], key=lambda x: float(x[1])))[0];ac2=ak['data']['asks'][-1][0]
    # # ac3=(min(cc, key=lambda x: float(x[-1])))
    # print(ac1,ac2)
    se1=user.web_order(tradeType=tradeType, symbol=symbol, side='sell', positionSide='short', orderType=orderType, reduceOnly=reduceOnly,
                  marginType=marginType, price=max(aa), priceType=priceType, orderQty=1, postOnly=postOnly, timeInForce=timeInForce)#下单
    print(se1)
    orderid1=se1['data']['orderId']
    time.sleep(60)
    se2=user.web_order(tradeType=tradeType, symbol=symbol, side='buy', positionSide='long', orderType=orderType, reduceOnly=reduceOnly,
                  marginType=marginType, price=min(aa1), priceType=priceType, orderQty=1, postOnly=postOnly, timeInForce=timeInForce)#下单
    print(se2)
    time.sleep(60)

if __name__ == '__main__':
    #user = wb.webapi(3, 'test')
    # print(order_ad(use=2,side='buy',positionSide='long'))
    # print(order_ad(use=2,side='buy',positionSide='short'))
    # print(order_ad(use=2,side='sell',positionSide='long'))
    # print(order_ad(use=2,side='sell',positionSide='short'))
    for i in range(10):
        print(order(2))
    # lev=user.web_leverage(tradeType=tradeType,symbol=symbol,leverage=20,marginType=marginType)
    # print(lev)


