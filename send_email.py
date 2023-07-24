import smtplib
import pywhatkit
import datetime
import pytz


def send_mail_fun(city):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # with open('password.txt', 'r') as x:
    password = "Project@22"
    server.login('accidentdetect22@gmail.com', password)

    subject = f"Accident Alert at {city}!!"
   # with open('body.txt', 'r') as n:
    #    body = n.read()
    body = f"An accident has been detected at {city}. Please send the help immediately"
    msg = f"subject: {subject} \n\n\n {body}"

    server.sendmail(
        'accidentdetect22@gmail.com',
        'mhv2408@gmail.com',
        msg
    )
    server.sendmail(
        'accidentdetect22@gmail.com',
        'naveengovind649@gmail.com',
        msg
    )

    print('Message is sent succesfully!')

