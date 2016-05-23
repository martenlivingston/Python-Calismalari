import smtplib as x

y=x.starttls()

y.login("akpinarsuleymen@gmail.com","password")
hedef("s.akpinar.yazilim@gmail.com")
mesaj="text mesaji"
y.sendmail("Kimden ",hedef,mesaj)
y.quit()
print("E-posta Gonderildi")
