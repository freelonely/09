import configparser
import os

def readconfig(tagname,name,logger):
    try:
        cf=configparser.ConfigParser()
        cfpath=os.path.dirname(os.path.abspath('.'))+'\\config\\config.ini'
        cf.read(cfpath)
        res_name=cf.get(tagname,name)
    except:
        logger.error(('读取配置文件失败，传输值为：',tagname,name))
    else:
        return res_name

