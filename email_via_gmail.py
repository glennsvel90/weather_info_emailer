import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from GMAIL_PWD import GMAIL_PWD
from Get_Weather_Data import get_weather_data
from Create_Html_file import create_html_report

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message: #Open report html file for reading binary
        msg = MIMEText(message.read(), 'html', 'html') #Create html message


    msg['Subject'] = 'Minute Weather {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M"))
    msg['From'] = 'stringhopper90@gmail.com'
    msg['To'] = 'sonyericson718@gmail.com, stringhopper90@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo() # Extended Hello
    server.starttls()  # Put the SMTP connection in TLS(Transport Layer Security) mode.
    server.ehlo()  # All SMTP commands that follow will be encrypted.
    server.login('stringhopper90@gmail.com', GMAIL_PWD)
    server.send_message(msg)
    server.close()

weather_dict, icon = get_weather_data('KLAX')
email_file = "Test_Email_File.html"
create_html_report(weather_dict, icon, email_file)
send_gmail(email_file)
