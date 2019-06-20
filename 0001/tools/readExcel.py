# -*- coding: utf-8 -*-
import xlrd

# 静态类 更多的是作为父类使用 如添加员工的计数
class test(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    def __new__(self):
        test.addNum()
        return super(test, self).__new__(self)

# 更多的使用来做工具类 此处使用此方式
class ExcelTool(object):
    '''
    通过excel获取数据的工具类
    '''
    # @staticmethod
    # def funtest(filePath,sheetPage,row):
    #     print(sheetPage)

    @staticmethod
    def getoneRow(filePath,sheetPage,row):
        '''
        获取某一行数据
        :param filePath:
        :param sheetPage:
        :param row:
        :return:
        '''
        excelFile=xlrd.open_workbook(filePath)
        sheet=excelFile.sheet_by_index(sheetPage)
        return sheet.row_values(row)

    @staticmethod
    def getoneCol(filePath,sheetPage,row):
        '''
        获取某一列数据
        :param filePath:
        :param sheetPage:
        :param row:
        :return:
        '''
        excelFile=xlrd.open_workbook(filePath)
        sheet=excelFile.sheet_by_index(sheetPage)
        return  sheet.col_values(row)

    @staticmethod
    def getallRow(filePath,sheetPage):
        '''
        获取该sheet页下所有行数据
        :param filePath:
        :param sheetPage:
        :return:
        '''
        excelFile=xlrd.open_workbook(filePath)
        sheet=excelFile.sheet_by_index(sheetPage)
        res=[]
        for x in range (sheet.nrows):
            # print(sheet.row_values(x))
            res.append(sheet.row_values(x))

        return res



# file = r'E:\Project\IdeaJAVA\xd\GalaxywalletAutotest\lib\test.xls'
# a=ExcelTool.getoneRow(file,1,0)
# b=ExcelTool.getoneCol(file,1,0)
# c=ExcelTool.getallRow(file,1)
# print(a)
# print(b)
# print(c)