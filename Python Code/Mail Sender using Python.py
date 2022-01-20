#first turn on Less secure app access in security of google account
# dont remove any dobule quotes, just fill your details

import smtplib as s  
# smtplib protocall to send email

ob = s.SMTP("smtp.gmail.com",587)
# object is created for server and port

ob.starttls()
# starting the connection with "tls"
# tls is a method of encryption

# Log in 
ob.login("your email", "password")

# Type subject below
subject="this is subject text"

# Type body text below
body="this body text"

message="Subject:{}\n\n{}".format(subject,body)
# joining subject and body

# Type emails where to send message
sendToAdress=["type sender email 1","type sender email 2"]

ob.sendmail("your email", sendToAdress, message)
# function for send email

ob.quit()
# closing the tls

print("message sent successfully")