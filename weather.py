# coding=utf-8

from requests import get
from datetime import date
import matplotlib

matplotlib.use("Pdf")
import matplotlib.pyplot as plt
import json
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import time
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

url = "http://t.weather.sojson.com/api/weather/city/101010100"
# url = 'http://www.weather.com.cn/data/sk/101010100.html'
weather = get(url)
weather.encoding = "utf-8"
# print(weather.text)
# 格式化中文
result = json.dumps(weather.text, ensure_ascii=False, encoding='UTF-8')
result = json.loads(weather.text, encoding="utf-8")
# print(result)

## create a plot of timestamps against temperature and show it
ymd_list = [record["ymd"] for record in result["data"]["forecast"]]
type_list = [record["type"] for record in result["data"]["forecast"]]
# print ymd_list
ymds = json.dumps(ymd_list, ensure_ascii=False, encoding='UTF-8')
types = json.dumps(type_list, ensure_ascii=False, encoding='UTF-8')

high_temperatur_list = [float(record["high"][3:5]) for record in result["data"]["forecast"]]
low_temperatur_list = [float(record["low"][3:5]) for record in result["data"]["forecast"]]
date_list = [int(record["date"]) for record in result["data"]["forecast"]]
dates = json.dumps(date_list, ensure_ascii=False, encoding='UTF-8')

## create a plot of timestamps against temperature and show it
plt.plot(date_list, high_temperatur_list, color='red', label="high")
plt.plot(date_list, low_temperatur_list, color='skyblue', label="low")
plt.savefig("weather.png")
# plt.show()

# today
day_num = date.today().day

for item in result["data"]["forecast"]:
    if int(item["date"]) == day_num:
        today = item

# send email
sender = "scyangle1314@126.com"
mail_pass = "coder1314"
receivers = ["444395258@qq.com", "scyangle1314@126.com"]
msgRoot = MIMEMultipart('related')
msgRoot["From"] = sender
msgRoot["To"] = ",".join(receivers)
subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '天气'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<p>天气折线图：</p>
<p>日期：%(ymd)s </p>
<p>星期：%(week)s </p>
<p>高温：%(high)s </p>
<p>低温：%(low)s </p>
<p>天气：%(type)s </p>
<p>提醒：%(notice)s </p>
<p>天气折线图：</p>
<p><img src="cid:image1"></p>
""" % today
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('weather.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# try:
smtpObj = smtplib.SMTP()
smtpObj.connect('smtp.126.com', 25)
smtpObj.login(sender, mail_pass)
smtpObj.sendmail(sender, receivers, msgRoot.as_string())
smtpObj.close()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "邮件发送成功"
# except smtplib.SMTPException:
#     print "Error: 无法发送邮件"
