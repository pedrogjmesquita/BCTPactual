import smtplib

class EmailClient():
  def __init__(self):
    self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

  def send(self, to, message):
    self.server.login("bctpactual@gmail.com", "ulfs jbmw yddy lpis")
    self.server.sendmail(
      "bctpactual@gmail.com",
      to,
      message,
      )
    self.server.quit()
