import send_email as email
import os

files_to_send = []
path = '/home/adrianbreazu/repositories/web-spi/src/spi/log'
def send_email():
    for file in os.listdir(path=path):
        if file.endswith(".log"):
            files_to_send.append(os.path.join(path, file))

    email.send_email_with_attachment(recipient="breazuadrian@gmail.com", subject="test", body="please see logs", file_path=files_to_send)

if __name__ == '__main__':
    send_email()