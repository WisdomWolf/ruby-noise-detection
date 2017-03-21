import smtplib
fromaddr = 'developingwisdom@gmail.com'
toaddrs  = 'wisdomwolf@gmail.com'
msg = 'Why,Oh why!'
username = 'developingwisdom@gmail.com'
password = '91meknvzi3w4CKuLOLe5'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()