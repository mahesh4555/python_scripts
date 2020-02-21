
#In Gmail account security,
#Allow less secure apps to sign in

import smtplib
fromaddr = 'mahesh4125@gmail.com'
toaddrs  = 'mahesh4675@gmail.com'
msg = '2222Why,Oh why!'
username = 'mahesh4007@gmail.com'
password = 'xxxxxxxxxxxxxxxx'
list = ["mahesh4785@gmail.com", "mahe4005@gmail.com"]

for i in range(len(li)):

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, list[i], msg)
    server.quit()
