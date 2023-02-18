from smtplib import SMTP_SSL
from email.mime.text import MIMEText

def sendMail(message,Subject,sender_show,recipient_show,to_addrs,cc_show=''):
    '''
    :param message: str 邮件内容
    :param Subject: str 邮件主题描述
    :param sender_show: str 发件人显示，不起实际作用如："xxx"
    :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
    :param to_addrs: str 实际收件人
    :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
    '''
    # 填写真实的发邮件服务器用户名、密码
    user = '2609260594@qq.com'
    password = '1234567890000000'
    # 邮件内容
    msg = MIMEText(message, 'plain', _charset="utf-8")
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["from"] = sender_show
    # 收件人显示，不起实际作用
    msg["to"] = recipient_show
    # 抄送人显示，不起实际作用
    msg["Cc"] = cc_show
    with SMTP_SSL(host="smtp.exmail.qq.com",port=465) as smtp:
        # 登录发邮件服务器
        smtp.login(user = user, password = password)
        # 实际发送、接收邮件配置
        smtp.sendmail(from_addr = user, to_addrs=to_addrs.split(','), msg=msg.as_string())

if __name__ =='__main':
    message = 'Python 测试邮件...'
    Subject = '主题测试'
    # 显示发送人
    sender_show = 'kristenqin'
    # 显示收件人
    recipient_show = 'kristen'
    # 实际发给的收件人
    to_addrs = '2609260594@qq.com'
    sendMail(message,Subject,sender_show,recipient_show,to_addrs)