import smtplib

import ssl

def email_sender(message,user):
  port=645
  host="smtplib.gmail.com"
  user_name="fa7222518@gmail.com"
  password="crac wuun exsg lmcl"
  context=ssl.create_default_context()
  
  with smtplib.SMTP_SSL(host,port,context=context) as server:
      server.login(user_name,password)
      server.sendmail(user_name,user,message)