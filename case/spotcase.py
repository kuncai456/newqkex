from BU.spot.api import webapi as wp
from common import util as ut, data as dt

symbol = 'BTC_USDT';
side = 'buy';
price = 20000.12;
volume = 0;
source = 'app'


# 限价成交场景
def PlaceOrder(symbol=None):

    sides = ['buy','sell']
    for side in sides:

        # 获取余额信息
        assets = ut.assets()
        basequote = ut.symbolbase(symbol)

        base = basequote['base']
        quote = basequote['quote']
        totalquote = assets[quote]
        # 获取买卖盘数据
        priceamount = ut.price(symbol=symbol)
        # 买入btc
        if side == 'buy':
            price = priceamount['ask'][0]
            amount = priceamount['ask'][1]
        else:
            price = priceamount['bid'][0]
            amount = priceamount['bid'][1]
        res = wp.orders(symbol=symbol, side=side, price=price, systemOrderType='limit', volume=amount, source='web')
        orderid = res['data']
        if res['code'] != 0:
            print("下单失败，失败原因：", res['msg'])
            return
        if side == 'buy':
            # 预算剩余计价币、基础币、手续费
            quotebalance = ut.d(assets[quote]) - ut.d(price) * ut.d(amount)
            basebalance = ut.d(assets[base]) + ut.d(amount) * ut.d(1 + dt.feeRate[symbol][1])
        else:
            quotebalance = ut.d(assets[quote]) + ut.d(price) * ut.d(amount) * ut.d(1 + dt.feeRate[symbol][1])
            basebalance = ut.d(assets[base]) - ut.d(amount)
            hisquotebalance = ut.d(assets[quote]) + ut.d(price) * ut.d(amount)

        # 查询余额接口
        newassets = ut.assets()
        if quotebalance - ut.d(newassets[quote]) < 0.0001:
            print(f"限价{side}:校验计价币余额成功，预期=", quotebalance, "实际返回：", ut.d(newassets[quote]))
        else:
            print(f"限价{side}:校验计价币余额失败，预期=", quotebalance, "实际返回：", ut.d(newassets[quote]))
        if basebalance - ut.d(newassets[base]) < 0.000001:
            print(f"限价{side}:校验基础币余额成功，预期=", basebalance, "实际返回：", ut.d(newassets[base]))
        else:
            print(f"限价{side}:校验基础币余额失败，预期=", basebalance, "实际返回：", ut.d(newassets[base]))
        # 校验历史委托
        his = ut.newhisorder(orderid=orderid, symbol=symbol)
        # 成交均价
        if side =='buy':
            avgprice = (ut.d(totalquote) - ut.d(newassets[quote])) / ut.d(amount)
        else:
            avgprice = (ut.d(hisquotebalance) - ut.d(totalquote)) / ut.d(amount)
        if avgprice == ut.d(his['averagePrice']):
            print(f"限价{side}:校验历史委托，成交均价成功，预期=", avgprice, "实际返回：", his['averagePrice'])
        else:
            print(f"限价{side}:校验历史委托，成交均价失败，预期=", avgprice, "实际返回：", his['averagePrice'])
        if ut.d(his['entrustPrice']) == ut.d(price):
            print(f"限价{side}:校验历史委托，委托价格成功，预期=", price, "实际返回：", his['entrustPrice'])
        else:
            print(f"限价{side}:校验历史委托，委托价格失败，预期=", price, "实际返回：", his['entrustPrice'])
        if ut.d(his['amount']) == ut.d(amount):
            print(f"限价{side}:校验历史委托，委托数量成功，预期=", amount, "实际返回：", his['amount'])
        else:
            print(f"限价{side}:校验历史委托，委托数量失败，预期=", amount, "实际返回：", his['amount'])



def marketOrder(symbol=None):
    sides = ['buy', 'sell']
    for side in sides:
        # 获取余额信息
        assets = ut.assets()
        basequote = ut.symbolbase(symbol)

        base = basequote['base']
        quote = basequote['quote']
        totalquote = assets[quote]
        # 获取买卖盘数据
        priceamount = ut.price(symbol=symbol)

        if side == 'buy':
            # price = priceamount['ask'][0]
            amount = priceamount['ask'][1]
        else:
            # price = priceamount['bid'][0]
            amount = priceamount['bid'][1]
        #下单
        res = wp.orders(symbol=symbol, side=side, price='', systemOrderType='market', volume=amount, source='web')
        orderid = res['data']
        if res['code'] != 0:
            print("下单失败，失败原因：", res['msg'])
            return
        # 查询余额接口
        newassets = ut.assets()
        # 查询历史委托
        his = ut.newhisorder(orderid=orderid, symbol=symbol)
        ut.d(his['averagePrice']) * ut.d(amount) * ut.d(1 + dt.feeRate[symbol][1])



if __name__ == '__main__':
    print(PlaceOrder(symbol='BTC_USDT'))
