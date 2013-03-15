#!/usr/bin/python
import smtplib
import socket
import os
import netrc

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'aaprindle@gmail.com'
recipient = 'aaprindle@gmail.com'
# Read from the .netrc file in your home directory
secrets = netrc.netrc()
username, account, password = secrets.authenticators( SMTP_SERVER )
subject = socket.gethostname() + " ** IP ADDRESS"


body = ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])[0]
 
"Sends an e-mail to the specified recipient."
 
body = "" + body + ""
 
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
 
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password.decode('base64')) #or just password
 
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()