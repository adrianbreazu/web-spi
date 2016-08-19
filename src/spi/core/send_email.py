import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import logging

logger = logging.getLogger(__name__)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = "email@gmail.com"
FROM_PASSWORD = "password"


def send_email_with_subject(recipient, subject, body):
    logger.debug("beginning send_email_with_subject to: {0} with subject: {1}".format(recipient, subject))
    try:
        msg = MIMEMultipart()
        msg['FROM'] = FROM_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        text = msg.as_string()
        server.sendmail(from_addr=FROM_EMAIL, to_addrs=recipient, msg=text)
        server.quit()
    except Exception as e:
        logger.debug("send_email_with_subject to: {0} with subject: {1} exception: {3}".format(recipient, subject, e))
    finally:
        logger.debug("end send_email_with_subject to: {0} with subject: {1}".format(recipient, subject))


def send_email_with_attachment(recipient, subject, body, filename, filepath):
    logger.debug("beginning send_email_with_attachment to: {0} with subject: {1}".format(recipient, subject))

    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filepath, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

        msg.attach(part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, to_addrs=recipient, msg=text)
        server.quit()
    except Exception as e:
        logger.debug("send_email_with_attachment to: {0} with subject: {1} exception: {3}".format(recipient, subject, e))
    finally:
        logger.debug("end send_email_with_attachment to: {0} with subject: {1}".format(recipient, subject))