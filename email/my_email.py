#-*- coding=utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders
#from email.header import Header
from datetime import datetime

smtp_host = 'smtp.163.com'
smtp_port = 25
subject = 'test 中文 subject ' + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
mail_from = 'a@b.com'
mail_password = raw_input('passwoord: ')
mail_to = ['a@b.com', 'x@y.com']
mail_cc = ['a@b.com', ]
mail_attach1 = 'stores1.xlsx'
mail_attach2 = 'stores2.xlsx'
mail_body = '''
<p>没有样式</p><br/>
<p><b>just a test</b></p><br/>
<p><strong>加点中文会怎么样</strong></p>
'''

#body = MIMEMultipart('alternative')
body = MIMEMultipart()
html_body = MIMEText(mail_body, 'html', _charset='utf-8')
body.attach(html_body)
body['Subject'] = subject
body['From'] = mail_from
body['To'] = ', '.join(mail_to)
body['Cc'] = ', '.join(mail_cc)

contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)
attachment1 = MIMEBase(maintype, subtype, _charset='utf-8')
with open(mail_attach1, 'rb') as fp:
    attachment1.set_payload(fp.read())
Encoders.encode_base64(attachment1)
basename = os.path.basename(mail_attach1)  #.decode('utf-8')
attachment1.add_header('Content-Disposition', 'attachment', filename=basename)
body.attach(attachment1)

attachment2 = MIMEBase(maintype, subtype, _charset='utf-8')
with open(mail_attach2, 'rb') as fp:
    attachment2.set_payload(fp.read())
Encoders.encode_base64(attachment2)
basename = os.path.basename(mail_attach2)  #.decode('utf-8')
attachment2.add_header('Content-Disposition', 'attachment', filename=basename)
body.attach(attachment2)

s = smtplib.SMTP(smtp_host, smtp_port)
s.login(mail_from, mail_password)
mail_to.extend(mail_cc)
s.sendmail(mail_from, mail_to + mail_cc, body.as_string())
s.quit()
