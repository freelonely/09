# -*- coding: utf-8 -*-
import json
import os
import unittest

import requests

from services.OriginService import OriginService
from services.yhqbAppserver.YHQBRequest import YHQBRequest


class test(unittest.TestCase):
    def setUp(self):
        # path=os.curdir+'/../testfile/test.xls'
        path=os.curdir+'/../testfile/test-originadmin.xls'
        # path= r'E:\Project\IdeaJAVA\xd\GalaxywalletAutotest\testfile\test.xls'
        self.t = OriginService(filePath=path);
    def test(self):
        self.t.done()


    # def test2(self):
    #     url ='http://test.yinheqianbao.com/test18/auth/userid'
    #     pathfront=os.curdir+'/../testfile/front.jpg'
    #     pathback=os.curdir+'/../testfile/backjpg.jpg'
    #     # file = open(path,'rb')
    #     headers = {'Cookie': 't=37989becde7e80a8365694bb1e7c5c44adaae0b5; hostid=abf2fa090bde4b7ab45356dcebd21696',
    #                'User-Agent':'yinheqianbao.com 2.5.0 22 com.rendongws.galaxywallet android C10003 OPPOR11s 25 867677031543553'}
    #     files3 = [('frontImage', ('frontImage',open(pathfront,'rb'),'image/png')),('backImage', ('backImage',open(pathback,'rb'), 'image/png'))]
    #     res = requests.post(url=url,files=list(files3),headers=headers)
    #     print(res.headers)
    #     print(res.text)

    # def test3(self):
    #     headers = {'Cookie': 't=37989becde7e80a8365694bb1e7c5c44adaae0b5; hostid=abf2fa090bde4b7ab45356dcebd21696',
    #     'User-Agent':'yinheqianbao.com 2.5.0 22 com.rendongws.galaxywallet android C10003 OPPOR11s 25 867677031543553'
    #     }
    #     headers=json.dumps(headers)
    #     param ={'frontImage':os.curdir+'/../testfile/front.jpg','backImage':os.curdir+'/../testfile/backjpg.jpg'}
    #     # res =YHQBRequest('http://test.yinheqianbao.com/test18').\
    #     #     doPost_file_img('auth/userid',param,headers)
    #     # print(res.text)
    #     a ={'aaaa':'bbbbb'}
    #     b='{"aaaa":"bbbbb"}'
    #     print(type(json.loads(b)))
    #     for x,y in json.loads(b).items():
    #         print( x ,y)






