# from email.mime.text import MIMEText
# from smtplib import SMTP
# msg=MIMEText('''

# ''','html','utf-8')
# from_addr='lochleee@gmail.com'
# password='sbpeccwt'
# smtp_server='smtp.gmail.com'
# to_addr='lochlee@qq.com'

# server=SMTP(smtp_server,587)
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()

# cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user(id,name) values(\'1\',\'Micheal\')')