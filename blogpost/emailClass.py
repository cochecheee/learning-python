import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# https://smstome.com/netherlands/phone/3197010587743/sms/7381
# https://sms24.me/en/numbers/84851418261
# mail.live.com

class SendEmail():

# if you want that, take it 😘
    def __init__(self,title,contentBody):
        self.user = "testsmtplib.123@outlook.com"
        self.passwd = "Hellomaycung@312@@123#*"

        self.from_addr = "testsmtplib.123@outlook.com"
        self.to_addr = "buitien747@gmail.com"
        self.smtp_srv = "smtp.live.com"

        self.contentBody = contentBody
        self.title = title

    def sendMain(self):
    # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = self.to_addr
        msg['Subject'] = self.title

        # Body of the email
        msg.attach(MIMEText(self.contentBody, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
            connection.starttls() 
            connection.login(user=self.user, password=self.passwd)
            connection.sendmail(from_addr=self.from_addr, to_addrs=self.to_addr, msg=msg.as_string())
