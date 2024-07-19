from email.message import EmailMessage
import ssl  #secure socket layer
import smtplib #simple mail transfer protocal
import random

# generate otp

otp = 0

while(otp < 10000): # if I use for i can't able to use 0
    digit = random.randint(0,9)
    otp = otp*10 + digit

#convert a int otp to string otp for mail

otp_copy = str(otp)

# mail

sender_id = "example@gmail.com"
sender_password = "*************" #app password

# Reciver mail with lowercase

reciver_id = input("TO (gmail account): ").lower()

# checking entered mail is correct or not

check = "@gmail.com"
if(check in reciver_id):
    print("Correct Gmail\n")
else:
    print("Enter correct Gmail \n\tEg:example@gamil.com")
    quit()

subject = "OTP Verification"
body = "You requested ONE TIME PASSWORD for verification \n\n\t\t     OTP : "+otp_copy

email = EmailMessage()
email["from"] = sender_id
email["to"] = reciver_id
email["subject"] = subject
email.set_content(body)

security = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=security) as smtp:
    smtp.login(sender_id,sender_password)
    smtp.sendmail(sender_id,reciver_id,email.as_string())

print("OTP is sent to your Gmail\n")
# verifing OTP
otp_check = input("Enter the OTP : ")

if(otp_check.isdigit()):
    otp_check = int(otp_check)
    if(otp == otp_check):
        print("\n\tCorrect OTP")
    else:
        print("\n\tWrong OTP")
else:
    print("\n\tEnter a digit")
