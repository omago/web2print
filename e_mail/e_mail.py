#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:

    def __init__(self, recipients=[], subject=None, content=None):
        self.recipients = recipients
        self.subject = subject
        self.content = content

    def add_recipient(self, recipient):
        self.recipients.append(recipient)

    def send(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = 'Web2print <no-reply@web2print.com>'
        msg['To'] = ', '.join(self.recipients)

        html = """
            <html>
            <head></head>
            <body>
            <p>
            %s
            </p>
            </body>
            </html>
            """ % self.content

        msg.attach(MIMEText(html, 'html', 'utf-8'))

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login("doctorkovac@gmail.com", "1809domagoj")

        s.sendmail('Web2print <no-reply@web2print.com>', self.recipients, msg.as_string())
