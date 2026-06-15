import smtplib
from email.mime.text import MIMEText

from config import EMAIL_TO
from config import QQ_SMTP_AUTH
from config import FROM_EMAIL

msg = MIMEText("Flight monitor test success!")
msg["Subject"] = "URC-CAN Flight Monitor"
msg["From"] = FROM_EMAIL
msg["To"] = EMAIL_TO

server = smtplib.SMTP_SSL("smtp.qq.com", 465)

server.login(FROM_EMAIL, QQ_SMTP_AUTH)

server.sendmail(
    FROM_EMAIL,
    EMAIL_TO,
    msg.as_string()
)

server.quit()

print("Email sent successfully")