import redis

class redistool(object):
    '''
    '''
    def __init__(self,product,env):
        self.direct={}
        jhk_prod={
            'host':'l-jhkredis01.prod.qd3.corp.agrant.cn',
            'port':'6380',
            'password':'WuXcl@redis01',
            'db':'2'
        }
        yhqb_prod={
            'host':'l-jhkredis01.prod.qd3.corp.agrant.cn',
            'port':'6380',
            'password':'WuXcl@redis01',
            'db':'3'
            }
        yhsd_prod={
            'host':'l-tjyredis01.prod.qd3.corp.agrant.cn',
            'port':'6379',
            'password':'Abcd12345',
            'db':'3'
        }
        yhqb_test={
            'host':'l-test18.dev.cn2.corp.agrant.cn',
            'port':'6379',
            'password':None,
            'db':'0'
        }
        if (product=='yhqb' and env=='test'):
            self.direct = yhqb_test
        elif(product=='yhqb' and env=='prod'):
            self.direct = yhqb_prod
        elif(product=='yhsd' and env=='prod'):
            self.direct = yhsd_prod
        elif(product=='jhk' and env=='prod'):
            self.direct = jhk_prod

        self.pool= redis.ConnectionPool(
            host=self.direct.get('host'),
            port=self.direct.get('port'),
            password=self.direct.get('password'),
            db=self.direct.get('db')
        )
        self.r=redis.Redis(connection_pool=self.pool)

    def getInstance(self):
        return self.r

    def keys(self,str):
        if(str=='' or str==None):
            return '参数不能为空'
        val='*'+str+'*'
        a =self.r.keys(pattern=val)
        if(a==None):
            print('no data')
            return self
        for i in a:
            print(i)
        return self

    def get(self,str):
        print(self.r.get(str))
        return self

    def set(self,key,value):
        self.r.set(key,value)
        return self

    def hgetall(self,str):
        print(self.r.hgetall(str))
        return self
    def hget(self,key,valu):
        print(self.r.hget(key,valu))
        return self
    def hset(self,key,valu):
        print(self.r.hset(key,valu))
        return self
    def delete(self,name):
        print(self.r.delete(name))
        return self


redistool('yhqb','test').keys('13717607755').get(b'sms_code:2:login:13717607755')
# redistool('yhqb','test').keys('auth').hget(b'user_auth:aa5dda4e4da14eff93c4d238fa87525c',0)
