import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = "email@gmail.com"
FROM_PASSWORD = "password"

def send_email_with_subject (recipient, subject, body):
    msg = MIMEMultipart()
    msg['FROM'] = FROM_EMAIL
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        text = msg.as_string()
        server.sendmail(from_addr=FROM_EMAIL, to_addrs=recipient, msg=text)
        server.quit()
        print("Successfully sent email with subject")
    except:
        print("Failed on sending email with subject")


def send_email_with_attachment (recipient, subject, body, filename, filepath):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = recipient
    msg['Subject']= subject

    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filepath, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

    msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, to_addrs=recipient, msg=text)
        server.quit()
        print("Successfully on sending the email and file")
    except:
        print ("Failed on sending the email and file")