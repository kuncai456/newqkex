from common import mysql_san as sql1
data = [
    [0.0085, 0.00025499],
    [0.0066, 0.00019799],
    [0.0064, 0.00019199],
    [119.86, 3.5953846],
    [100.55, 3.01615383],
    [0.0087, 0.00026099],
    [0.0054, 0.00016199],
    [147.56, 4.42615383],
    [0.0085, 0.00025499],
    [0.0076, 0.00022799],
    [0.0054, 0.00016199],
    [0.0089, 0.00026699],
    [0.0087, 0.00026099],
    [0.0074, 0.00022199],
    [0.0062, 0.00018599],
    [0.007, 0.00020999],
    [0.0082, 0.00024599],
    [0.0067, 0.00020099],
    [0.0068, 0.00020399],
    [0.0088, 0.00026399],
    [0.0066, 0.00019799],
    [0.0066, 0.00019799],
    [0.0051, 0.00015299],
    [62.96, 1.8876923],
    [0.0056, 0.00016799],
    [84.87, 2.5453846],
    [22.25, 0.66692307],
    [0.0082, 0.00024599],
    [56.74, 1.70076922],
    [127.53, 3.82384614],
    [0.0081, 0.00024299],
    [0.0068, 0.00020399],
    [0.0084, 0.00025199],
    [197, 5.90999998],
    [0.0083, 0.00024899],
    [164.56, 4.93615382],
    [146.22, 4.38461537],
    [66.8, 2.00307691],
    [0.0068, 0.00020399],
    [0.0082, 0.00024599],
    [0.0089, 0.00026699],
    [0.0064, 0.00019199],
    [0.0077, 0.00023099],
    [0.0073, 0.00021899],
    [0.0088, 0.00026399],
    [159.35, 4.77923075],
    [0.0084, 0.00025199],
    [161.8, 4.8530769],
    [196.34, 5.88923074],
    [0.0059, 0.00017699],
    [170.92, 5.12538459],
    [0.0053, 0.00015899],
    [103.29, 3.09692306],
    [0.0089, 0.00026699],
    [0.0069, 0.00020699],
    [0.0071, 0.00021299],
    [0.008, 0.00023999],
    [0.0066, 0.00019799],
    [53.46, 1.60153845],
    [0.0086, 0.00025799],
    [0.007, 0.00020999],
    [0.0056, 0.00016799],
    [0.0056, 0.00016799],
    [117.69, 3.52846152],
    [0.0081, 0.00024299],
    [0.008, 0.00023999],
    [0.0073, 0.00021899],
    [0.0057, 0.00017099],
    [180.35, 5.40923075],
    [0.0083, 0.00024899],
    [115.18, 3.45461537],
    [0.0077, 0.00023099],
    [0.0056, 0.00016799],
    [72.98, 2.1876923],
    [0.0057, 0.00017099],
    [88.17, 2.64461537],
    [0.0064, 0.00019199],
    [0.0076, 0.00022799],
    [0.0054, 0.00016199],
    [0.0074, 0.00022199],
    [0.006, 0.00017999],
    [0.0077, 0.00023099],
    [0.0085, 0.00025499],
    [0.0058, 0.00017399],
    [0.0082, 0.00024599],
    [48.36, 1.44923076],
    [162.77, 4.8830769],
    [22.51, 0.67384615],
    [0.0059, 0.00017699],
    [0.0067, 0.00020099],
    [0.0074, 0.00022199],
    [0.0072, 0.00021599],
    [0.0083, 0.00024899],
    [0.0082, 0.00024599],
    [0.0065, 0.00019499],
    [0.0066, 0.00019799],
    [75.44, 2.26153845],
    [0.0069, 0.00020699],
    [186.2, 5.58461536],
    [50.37, 1.50923076]
]
def mysql_fee_selec(user_id,legal_symbol,symbol):#通过数据库获取用户数据计算广告费率
    sql = f"SELECT a.fee_rate,b.`status`, b.ratio,b.target_uid AS s_uid ,b.source_uid as f_uid,(SELECT platform_commission_rate FROM OTC.config_currency WHERE symbol='{symbol}' AND legal_symbol='{legal_symbol}') AS fee FROM OTC.user_info a,OTC.rebate_config b WHERE a.user_id=b.source_uid AND a.user_id in ({user_id})"
    wss = sql1.mysql_select(sql)
    fee_rate = wss[0][0];status = wss[0][1];ratio = wss[0][2];target_uid = wss[0][3];source_uid = wss[0][4];fee = wss[0][5]
    print('基于数据库''uid=', target_uid, f'法币为{legal_symbol}的币种{symbol}费率=', fee, '折扣=', fee_rate, '溢价率=',
          ratio, 'uid=', target_uid, '返佣关系(1正常0暂停)=', status)
    # print(fee_rate,status,ratio,source_uid,fee)
    if status==0:
        print('返佣关系暂停，不存在返佣')
    else:
        if fee_rate==0:
            fee_2 = fee * (1+ ratio)#币种费率*(1+溢价率)# cc="{:.2f}%".format(fee_1*100) #转换成功百分比
            return fee_2
        else:
            fee_1 = (fee * fee_rate + fee * ratio)#币种费率*手续折扣+手续费溢价率*币种费率,
            return fee_1
def otc_ratiofee(fee_rate,status,ratio,fee,account,cc):#计算费率返佣的
    print('基于币种费率=',fee,'折扣=',fee_rate,'溢价率=',ratio,'数量=',account,'返佣关系(1正常0暂停)=',status)
    if status==0:
        print('返佣关系暂停，不存在返佣关系')
        fee_1=fee * fee_rate
        print('手续费率为', "{:.2f}%".format(fee_1 * 100))
        cee = account * fee_1
        print('订单收取手续费为', cee)
    else:
        if fee_rate==0:
            fee_2 = fee * (1+ ratio)#币种费率*(1+溢价率)
            print('手续费率为',"{:.2f}%".format(fee_2*100))
            cee=account * fee_2
            print('订单收取手续费为',cee)
            f_fee=  fee_2 - fee
            feea = account * f_fee
            print(cc,'返佣手续费为',feea)
            order_account=account/(1+fee_2)
            print('若数量为发布广告数量，则可售数量为',order_account)
        else:
            fee_1 = (fee * fee_rate + fee * ratio)#币种费率*手续折扣+手续费溢价率*币种费率,
            print('手续费率为',"{:.8f}%".format(fee_1*100))
            cee = account * fee_1
            print('订单收取手续费为', "{:.8f}".format(cee))
            f_fee = fee_1 - (fee * fee_rate)
            feea = (account) * (f_fee)
            print('返佣手续费为', "{:.8f}".format(feea))
            order_account = account / (1 + fee_1)
            print('若数量为发布广告数量，则可售数量为', order_account)





if __name__ == '__main__':
    for tmp in data:
        c=otc_ratiofee(fee_rate=0,status=1,ratio=0.3,fee=0.1,account=tmp[0],cc=tmp[1])
        print(c)
    # a=mysql_fee_selec(user_id=10122165,legal_symbol='usd',symbol='ETH')
    # print(a)