import smtplib as x

y=x.starttls()

y.login("your@mail.adress","password")
hedef("target@mail.adress")
mesaj="text"
y.sendmail("By ",hedef,mesaj)
y.quit()
print("sending e mail is ok")
