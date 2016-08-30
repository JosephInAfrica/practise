import smtplib
from email.mime.text import MIMEText

msg=MIMEText('hello,send by Python...','plain','utf-8')

to_addr='lochlee@qq.com'

from_addr='lochlee@qq.com'
password='sbpeccwt@901215'
smtp_server='smtp.qq.com'
smtp_port=465
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

