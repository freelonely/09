# -*- coding: utf-8 -*-

import sys
import json
import stomp
import time


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

class mqTool(object):
    def __init__(self,host,port,destination,user=None,passwd=None):
        self.conn = stomp.Connection([(host,port)])
        self.conn.set_listener(destination, MyListener())
        self.conn.start()
        self.conn.connect(user,passwd,wait=True)

    def delete(self):
        self.conn.disconnect()

    def doPorduct(self,destination,message):
        '''生产消息'''
        self.conn.send(destination, message)


def customer(str):
    conn = stomp.Connection([('10.4.1.128', 61613)])
    conn.start()
    conn.set_listener('mytest', MyListener())
    conn.connect(wait=True)
    # conn.send('/queue/test', 'test message')
    conn.send(body=str, destination='mytest')
    conn.disconnect()




def test():
    conn = stomp.Connection([('10.16.20.15', 61613)])
    conn.start()
    conn.set_listener('heliPayTransferProd', MyListener())
    conn.connect(username='wuxcl',passcode='wuxc',wait=True)
    # f1= open(r'E:\Project\IdeaJAVA\xd\GalaxywalletAutotest\lib\MQSendData.txt','r')
    # f2= open(r'E:\Project\IdeaJAVA\xd\GalaxywalletAutotest\lib\MQSendData1.txt','r',encoding='utf-8')
    conn.send(body='{"rt1_bizType":"Transfer","rt2_retCode":"0000","rt3_retMsg":"接收成功","rt4_customerNumber":"C1800275867","rt5_orderId":"1108175338711683072","rt6_serialNumber":"179921531","sign":"6ec047542235a31ed6db76e45a12edbb"}', destination='heliPayTransferProd')

    # for line in f2.readlines():
    #     conn.send(body=line.encode('utf-8'), destination='heliPayTransferProd')
    #     print(type(line.encode('utf-8')))
    conn.disconnect()
    # f1.close()

# a ='{"rt1_bizType":"Transfer","rt2_retCode":"0000","rt3_retMsg":"接收成功","rt4_customerNumber":"C1800275867","rt5_orderId":"1108175338711683072","rt6_serialNumber":"179921531","sign":"6ec047542235a31ed6db76e45a12edbb"}\n'
# customer(a)
# test()