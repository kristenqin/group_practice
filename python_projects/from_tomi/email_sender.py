
"""
how to send an email with python
TODO: go over to our gmail account and setup 2 factor authentication
TODO: generate app password "rsjihwxjepvtzzcd"
TODO: create a function to send the email
TODO: try to use another email account to send an email
"""

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "yqin07184@gmail.com"
email_password = "rsjihwxjepvtzzcd" #TODO: 不清楚这里的密码是什么 是自己邮箱的还是刚刚双重认证生成的

email_receiver = "2609260594@qq.com"

subject = "HELLO THIS IS AN AWESOME MESSAGE FROM MY PYTHON PROJECT"
body = """
you can download this from my github https://github.com/kristenqin/group_practice
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp: #TODO: 弄清楚with这块代码是在干什么
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

