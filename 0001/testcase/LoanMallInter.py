import unittest

import requests

class loanMallinterfaceTest(unittest.TestCase):
    '''
    钱大大接口测试
    '''
    def setUp(self):
        self.headers={'Content-Type':'pplication/json;charset=UTF-8'}
    def dopost(self,url,json):
        return requests.post(url=url,json=json,headers=self.headers)

    def test_updateCommonProductStatusOK(self):
        '''
        修改产品上架下架 无效
        id :common_loan的id
        status :0下架;1正常;2暂停',
        :return:
        '''
        url='http://qddadmin.wuxcl.com/loanmall/product/updateCommonProductStatus'
        json={'id': 84, 'status': 1}
        res = self.dopost(url=url,json=json)
        print (res.text)

    def test_setCommonProductSortOK(self):
        '''
        修改产品在推荐页面的位置
        :return:
        '''
        url='http://qddadmin.wuxcl.com/loanmall/product/setCommonProductSort'
        json={'productId': 73, 'position': 3}
        res=self.dopost(url=url,json=json)
        print(res.text)

    def test_addRegistrationsFalse(self):
        url='http://qddadmin.wuxcl.com/loanmall/statistics/addRegistrations'
        json={'productId':73, 'beginDate': '2019-04-12','registrations': 10}
        res=self.dopost(url=url,json=json)
        print(res.text)

    def test(self):
        '''`billing_method` int(1) DEFAULT NULL COMMENT '合作方式: 0.CPA 1.CPC 2.CPT 3.CPM',
        0cpa：注册量*单价   1cpc：点击量*单价  2cpt：投放时长*单价     3cpm：展现量*单价
        '''
        pass


    def test_singin(self):
        '''注册
        '''
        url = 'http://qdd.wuxcl.com/sms/checkCode' \
              '?mobile=18501034355&code=469525&channel=000601&device_type=1'
        # json={'mobile':'18501034355','code':'380066','channel':'000601','device_type':1}
        res=self.dopost(url=url,json=None)
        print(res.text)
