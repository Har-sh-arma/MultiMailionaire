import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
df = pd.read_excel("mails.xlsx")
   
fromaddr = "ui21cs20@iiitsurat.ac.in"
toaddr = list(map(lambda i: df.loc[i]['Mails'], range(len(df))))
   
# instance of MIMEMultipart
msg = MIMEMultipart()
  
msg['From'] = os.environ.get("SENDERMAIL")
msg['To'] =", ".join(toaddr)

body = ""
with open("mail.txt") as f:
    bdy = False
    l = f.readline()
    while(l):
        if bdy and l[0]=='#':
            l = f.read()
            body+=l  
        elif l[0]!='#' and l[0]!='\n' and not bdy:
            msg['Subject'] = l
            bdy = True
        l = f.readline()
        
        
 
msg.attach(MIMEText(body, 'plain'))


# open the file to be sent

for i in range(len(sys.argv)-1):
    filename = sys.argv[i+1]
    attachment = open(filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login(fromaddr, os.environ.get("SENDERPASS"))
  
# Converts the Multipart msg into a string
text = msg.as_string()
#print(text)
# sending the mail
s.sendmail(fromaddr, toaddr, text)
  
# terminating the session
s.quit()
