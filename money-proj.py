# coding:utf8
from __future__ import unicode_literals
import sys
import MySQLdb


class TransferMoney(object):
    """docstring for TransferMoney"""

    def __init__(self, conn):
        self.conn = conn

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from testpy where account = '%s'" % acctid
            cursor.execute(sql)
            print "check_acct_available:" + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception(" %s not exsit" % acctid)
        finally:
            cursor.close()

    def show_data(self):
        cursor = self.conn.cursor()
        try:
            sql = "select * from testpy where account = 'djj'"
            cursor.execute(sql)
            print "check_acct_available:" + sql
            rs = cursor.fetchall()
            print rs
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        sql = "select * from testpy where account = '%s' and money >%s" % (
            acctid, money)
        try:
            cursor.execute(sql)
            print "check_acct_available:" + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception(" %s account not has enough money" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        sql = "update testpy set money = money-%s where account = '%s'" % (
            money, acctid)
        try:
            cursor.execute(sql)
            print "reduce_money:" + sql
            if cursor.rowcount != 1:
                raise Exception(" %s account reduce money error" % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        sql = "update testpy set money = money+%s where account = '%s'" % (
            money, acctid)
        try:
            cursor.execute(sql)
            print "add_money:" + sql
            if cursor.rowcount != 1:
                raise Exception(" %s account add money error" % acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
            # print "transfer success"
        except Exception, e:
            self.conn.rollback()
            raise e

# 脚本执行入口
if __name__ == '__main__':
    # source_acctid = sys.argv[1]
    # target_acctid = sys.argv[2]
    # money = sys.argv[3]
    source_acctid = 'djj'
    target_acctid = 'dh'
    money = 100
    conn = MySQLdb.Connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='123456',
                           db='test',
                           charset='utf8')
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
        # tr_money.transfer('djj', 'dh', 100)
        # tr_money.show_data()
    except Exception as e:
        print "出现问题：" + str(e)
    finally:
        conn.close()
