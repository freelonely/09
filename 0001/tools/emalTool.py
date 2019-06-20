#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from tools.configTool import configTool


class emailTool(object):


    def __init__(self):
        fkey='email'
        self.conf = configTool()
        self.conf.buid(self.conf.getCurrentPath()+r'\..\config\config.ini')
        self.sender=self.conf.get(fkey,'sender')   # 发件人邮箱账号
        self.password = self.conf.get(fkey,'password')             # 发件人邮箱密码
        self.receiver=self.conf.get(fkey,'receiver').split(',')   # 收件人邮箱账号，我这边发送给自己

    def _doMail(self,subject,content,type):
        try:
            msg=MIMEText(content,type,'utf-8')
            msg['From']=formataddr(["发送人",'utf-8'])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["接收人",'utf-8'])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=subject               # 邮件的主题，也可以说是标题

            server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender,self.receiver,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except NameError:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            return False
        return True

    def doMail_html(self,subject,content):
            return self._doMail(subject,content,'html')
    def doMail_text(self,subject,content):
        return self._doMail(subject,content,'plain')

# t =emailTool()
# print(t.doMail_text('subjectTest2','conterntTest2'))
# print(t.doMail_html('subjectTest2','<p>htmlcontent</p>'))