#-*- coding=utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders
#from email.header import Header
from datetime import datetime


class EmailHandler(object):

    def __init__(self, smtp_host=None, smtp_port=25):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.mail_from = None
        self.mail_passwd = None
        #self.mail_body = MIMEMultipart('alternative')
        self.mail_body = MIMEMultipart()

    def send_mail(self, mail_from, mail_passwd=None, mail_to=None, mail_cc=[], mail_msg='', mail_attachment=[]):
        self.mail_from = mail_from
        self.mail_passwd = mail_passwd
        self.__set_mail_msg(mail_to, mail_cc, mail_msg)
        self.__set_mail_attachment(mail_attachment)
        self.__send_mail(mail_to+mail_cc)

    def __set_mail_msg(self, mail_to, mail_cc, mail_msg):
        html_body = MIMEText(mail_body, 'html', _charset='utf-8')
        self.mail_body.attach(html_body)
        self.mail_body['Subject'] = subject
        self.mail_body['From'] = self.mail_from
        self.mail_body['To'] = ', '.join(mail_to)
        self.mail_body['Cc'] = ', '.join(mail_cc)

    def __set_mail_attachment(self, attachments):
        if not attachments: return
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)
        for file_name in attachments:
            attachment = MIMEBase(maintype, subtype, _charset='utf-8')
            with open(file_name, 'rb') as fp:
                attachment.set_payload(fp.read())
            Encoders.encode_base64(attachment)
            basename = os.path.basename(file_name)  #.decode('utf-8')
            attachment.add_header('Content-Disposition', 'attachment', filename=basename)
            self.mail_body.attach(attachment)

    def __send_mail(self, mail_to):
        s = None
        try:
            s = smtplib.SMTP(self.smtp_host, self.smtp_port)
            if self.mail_passwd: s.login(self.mail_from, self.mail_passwd)
            s.sendmail(self.mail_from, mail_to, self.mail_body.as_string())
        finally:
            if s != None:
                s.quit()
                s.close()


if __name__ == '__main__':
    smtp_host = 'smtp.163.com'
    smtp_port = 25
    subject = 'test 中文 subject ' + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    mail_from = 'a@b.com'
    mail_password = raw_input('passwd for %s: ' % mail_from)
    mail_to = ['a@b.com', 'c@d.com']
    mail_cc = ['e@f.com', ]
    mail_attachment = ['stores1.xlsx', 'stores2.xlsx']
    mail_body = '''
    <p>没有样式</p><br/>
    <p><b>just a test</b></p><br/>
    <p><strong>加点中文会怎么样</strong></p>
    '''

    email_handler = EmailHandler(smtp_host=smtp_host)
    email_handler.send_mail(mail_from, mail_password, mail_to, mail_cc, mail_body, mail_attachment)
