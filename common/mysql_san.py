import decimal
import sys

import pymysql,time
import logging
from common import slacksend
host='192.168.200.150';user='test_user';password='test-user@123456';port=3306
dev_host='192.168.200.101';dev_user='dev-user';dev_password='dev-user@123456';port=3306
host1='172.31.24.122';user1='root';password1='12@3456';port1=4000
uat_host='172.31.28.33';uat_user='dev_user';uat_password='dev_user#dev_us111er'

# user='admin'
# password='6Gp0iz1ZHNceJKwSpNg6'
# database='otc'
from decimal import Decimal as d
#sql='SELECT available_balance FROM assets WHERE id=4594227'
sql="SELECT a.fee_rate,b.`status`, b.ratio,b.target_uid AS s_uid ,b.source_uid as f_uid,(SELECT platform_commission_rate FROM config_currency WHERE symbol='btc' AND legal_symbol='usd') AS fee FROM user_info a,rebate_config b WHERE a.user_id=b.source_uid AND a.user_id in (10122165)"
def mysql_select(sql,ac):#根据主库,返回内容,查询表,查询条件进行查询
    if ac==0:
        db = pymysql.connect(host=host1, user=user1, password=password1,port=port1, database="")# 打开数据库连接
    elif ac==1:
        db = pymysql.connect(host=uat_host, user=uat_user, password=uat_password, port=port1, database="")
    elif ac==2:
        db = pymysql.connect(host=dev_host, user=dev_user, password=dev_password, port=port, database="")  # 打开数据库连接
    else:
        db = pymysql.connect(host=host, user=user, password=password, database="")  # 打开数据库连接
    cursor = db.cursor()# 使用cursor()方法获取操作游标
    sql = sql# 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()# 关闭数据库连接
    return data
def sql_send(sql,ac):
    id=[]
    res = mysql_select(sql,ac=ac)
    for tmp in res:
        id.append(tmp[0])
    return id
def mysql_execute(sql):#修改数据库内容或拆入数据
    db = pymysql.connect(host=host, user=user, password=password, database="")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("执行成功")
    except:
        db.rollback()
        print("执行失败")
    db.close()
def add_account(uid,currency,balance):#给钱包价钱，加到钱包账户
    sql_select = f"SELECT balance FROM wallet.user_balance WHERE user_id in ({uid}) AND parent_symbol='{currency}' AND currency_id=0"
    install_select = f"INSERT INTO wallet.user_balance ( `currency_id`, `parent_symbol`, `user_id`, `balance`, `create_on`, `update_on`) VALUES ( 0, '{currency}', {uid}, {balance}, '2023-02-22 11:08:19', '2023-02-25 14:30:41')"
    updata_select = f"UPDATE wallet.user_balance SET balance = '{balance}' WHERE parent_symbol ='{currency}' AND currency_id=0 AND user_id in ({uid})"
    abc=mysql_select(sql_select,ac=1)
    if len(abc)==0:#判断钱包是否有数据
        a=mysql_execute(install_select)
        print(a,install_select)
    else:
        a=mysql_execute(updata_select)
        print(updata_select,a)

def mysql_reconciliation(ac,uid):#排除用户的账是否正确
    a=mysql_select(f"SELECT action_id,income,after_balance FROM futures_btc1.t_account_action WHERE uid={uid} AND create_date='2023-08-07'  ORDER BY id DESC ",ac=ac)
    id2=[];id1=[];id3=[]
    equal_flag = True
    for tmp in a:
        id1.append(tmp[2])
        id2.append(tmp[1])
        id3.append(tmp[0])
    for i in range(len(id1) - 1):
        if id1[i] - id2[i] != id1[i + 1]:
            equal_flag = False
            print("数据当前的action_id：", id3[i])
            print("数据上一个的action_id：", id3[i+1])
            print("id1[{}]-id2[{}] 不等于 id1[{}]: ".format(i, i, i + 1))
            print("id1[{}]-id2[{}] = {}".format(i, i, id1[i] - id2[i]))
            print("id1[{}] = {}".format(i + 1, id1[i + 1]))
            print("id1[{}] = {}".format(i + 1, id1[i + 1]))
    if equal_flag:
        print("当前用户的数据正常")
        #return "当前用户的数据正常"
def sql_send_with_timeout(sql, timeout):
    start_time = time.time()
    while True:
        try:
            a = sql_send(sql,ac=0)
            return a
        except Exception as e:
            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout:
                raise TimeoutError('查询超时')
            print(f'查询失败，重试中...({elapsed_time:.2f}s)')
            time.sleep(1)


def t_account_action():
    try:
        sql1 = "SELECT t.uid, t.after_balance, m.total_income FROM futures_btc1.t_account_action AS t INNER JOIN (SELECT uid, MAX(id) AS max_id, SUM(income) AS total_income FROM futures_btc1.t_account_action WHERE currency='USDT' GROUP BY uid) AS m ON t.uid = m.uid AND t.id = m.max_id HAVING t.after_balance!=m.total_income  ORDER BY t.uid DESC"

        # 设置超时时间为10秒
        a = sql_send_with_timeout(sql1, timeout=10)

        if not a:  # 如果a为空或者a为[]
            print('当前所有用户对账正确')
        else:
            print(slacksend.send_Slack('对账异常，异常uid为：'))
            print(slacksend.send_Slack(a))
            ac=mysql_reconciliation(a[0])
            print(slacksend.send_Slack(ac))
    except TimeoutError:
        print('查询超时，请检查网络连接或稍后重试')
    except Exception as e:
        print('Error:', e)

def add_wallet_account(uid,currency,balance):#给钱包价钱，加到钱包账户
    sql_select = f"SELECT balance FROM wallet.user_balance WHERE user_id in ({uid}) AND parent_symbol='{currency}' AND currency_id=0"
    install_select = f"INSERT INTO wallet.user_balance ( `currency_id`, `parent_symbol`, `user_id`, `balance`, `create_on`, `update_on`) VALUES ( 0, '{currency}', {uid}, {balance}, '2023-02-22 11:08:19', '2023-02-25 14:30:41')"
    updata_select = f"UPDATE wallet.user_balance SET balance = '{balance}' WHERE parent_symbol ='{currency}' AND currency_id=0 AND user_id in ({uid})"

    install_transfer_record = f"insert into wallet.transfer_record (symbol, user_id, broker_id, to_address, amount,btc_amount, fee, confirmation, biz, trader_no, transfer_type, transaction_type,status, create_on, update_on) values ('USDT',  {uid}, 10000, unix_timestamp()+600, {balance}, 0, 0.00000000, 0, 9,unix_timestamp(), 13, 0, 2, now(), now());"
    install_bill_statements= f"insert into wallet.bill_statements (user_id, statements_no, symbol, amount, after_amount,trans_type, create_time)values ( {uid}, unix_timestamp(), 'USDT', {balance}, 0, 13, now());"

    abc=mysql_select(sql_select,ac=2)
    print(abc)
    if len(abc)==0:#判断钱包是否有数据
        a=mysql_execute(install_select)
        print(a,install_select)
        a = mysql_execute(install_transfer_record)
        # 插入钱包划转记录
        a = mysql_execute(install_bill_statements)
    else:
        balance=decimal.Decimal(balance)
        abc=abc[0][0]
        if balance>abc:#判断更新的资金是否比数据库中的大
            update_balance=balance-abc
        elif balance==abc:
            sys.exit()
        else:
            update_balance=abc-balance
        a = mysql_execute(updata_select)
        # print(updata_select,a)
        update_transfer_record = f"insert into wallet.transfer_record (symbol, user_id, broker_id, to_address, amount,btc_amount, fee, confirmation, biz, trader_no, transfer_type, transaction_type,status, create_on, update_on) values ('USDT',  {uid}, 10000, unix_timestamp()+600, {update_balance}, 0, 0.00000000, 0, 9,unix_timestamp(), 13, 0, 2, now(), now());"
        mysql_execute(update_transfer_record)
        update_bill_statements = f"insert into wallet.bill_statements (user_id, statements_no, symbol, amount, after_amount,trans_type, create_time)values ( {uid}, unix_timestamp(), 'USDT', {update_balance}, {balance}, 13, now());"
        mysql_execute(update_bill_statements)
    #插入钱包划转记录
    # a = mysql_execute(install_transfer_record)
    # # 插入钱包划转记录
    # a = mysql_execute(install_bill_statements)

if __name__ == '__main__':
    # user_id=10122165; legal_symbol='usd'; symbol='btc'
    # sql = f"SELECT a.fee_rate,b.`status`, b.ratio,b.target_uid AS s_uid ,b.source_uid as f_uid,(SELECT platform_commission_rate FROM OTC.config_currency WHERE symbol='{symbol}' AND legal_symbol='{legal_symbol}') AS fee FROM OTC.user_info a,OTC.rebate_config b WHERE a.user_id=b.source_uid AND a.user_id in ({user_id})"
    # a = mysql_select(sql)
    # print(mysql_reconciliation(ac=1,uid='169321'))
    # #print(sql_send("SELECT email FROM user_center.user_info WHERE id in (10122688)",ac=1))#查询账号邮箱
    # print(add_account(uid='10122628',currency="USDT",balance='10000'))#给钱包价钱，加到钱包账户
    # print(add_wallet_account(uid='10135683',currency="USDT",balance='1000000'))#给钱包价钱，加到钱包账户
    # for i in  range(2000):
    #     print(t_account_action())
    #     time.sleep(2 * 65)
    # uid="10122637"
    # currency="USDT"
    # sql=f"SELECT * FROM wallet.user_balance WHERE user_id in ({uid}) AND parent_symbol='{currency}' AND currency_id=0"
    # data=mysql_select(sql,3)
    # print(data[0][4])
    # data
    # mysql_execute()
    sql1="select id from user_center.user_info where type=0 limit 10;"
    datas=mysql_select(sql1,3)
    for i in datas:
        print(type(i[0]))