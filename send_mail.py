import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '这是来自deantong的邮件', 'tongfeng@benlai.com', '942661261@qq.com'
    text_content = '欢迎关注我http://dashboard.aide.benlai.net，谢谢了！'
    html_content = '<p>欢迎关注<a href="http://dashboard.aide.benlai.net" target=blank>http://dashboard.aide.benlai.net</a>,这是grafana网站！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()