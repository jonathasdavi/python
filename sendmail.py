# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = "This mail was sent by a Python script created by Jonathas Santos."

# setup the parameters of the message
password = "*jonathas123"
msg['From'] = "testphytoncode@gmail.com"
msg['To'] = "testphytoncode@gmail.com"
msg['Subject'] = "This is a Python Email Test"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print
"successfully sent email to %s:" % (msg['To'])