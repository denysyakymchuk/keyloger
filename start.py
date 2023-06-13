import smtplib
import ssl
from email.message import EmailMessage


class Email:
    def __init__(self):
        self.email_sender = ''
        self.ema_password = ''

    def sender(self, message):
        email_receiver = ''
        subject = 'Alegro'

        em = EmailMessage()

        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject

        em.set_content(f'{message}')

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.ema_password)
            smtp.sendmail(self.email_sender, email_receiver, em.as_string())

