import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# https://smstome.com/netherlands/phone/3197010587743/sms/7381
# https://sms24.me/en/numbers/84851418261
# mail.live.com

# if you want that, take it 😘
user = "testsmtplib.123@outlook.com"
passwd = "Hellomaycung@312@@123#*"

from_addr = "testsmtplib.123@outlook.com"
to_addr = "buitien747@gmail.com"
smtp_srv = "smtp.live.com"


# Create the email
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Test Email"

# Body of the email
with open("data.txt", encoding='utf-8') as message:
    body = message.read()
msg.attach(MIMEText(body, 'plain'))

# Connect to the server and send the email
with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
    connection.starttls() 
    connection.login(user=user, password=passwd)
    connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
# print(day)