#cameras_554 ={ "project number": "here IP camera"}
#emails = {  "project number" :  "here PM email" }
body_mail = "Drogi PM-ie, wykryliśmy że kamera na Twoim projekcie na problemy z połączeniem. Spróbuj ponownie ją uruchomić. Jeśli będziesz miał problem, skontaktuj się z działem IT."
import socket
from email.mime.text import MIMEText
import smtplib
open_port = []
closed_ports = []
def check_port(port):
    if port==554:
        print("Checking port {}".format(port))
        for cam,ip in cameras_554.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print ("Port is open")
                open_port.append(cam)
            else:
                print ("Port is not open")
                closed_ports.append(cam)
            sock.close()
check_port(554)
def sent_email():
    for port in closed_ports:
        s = ""
        s+= "({}) Niedziałająca kamera".format(port) # string to title
        #fromaddr = "smtp email adress"
        #toaddr = 'to who sent email'
        html = open("mailTemplate.html").read().replace("mail_head",s).replace("body_mail",body_mail) # read template and sent as email
        msg = MIMEText(html.encode('utf-8'), 'html', 'UTF-8')
        msg['From'] =  fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "({}) Niedziałająca kamera".format(port) # title
        debug = False
        if debug:
            print(msg.as_string())
        else:
            server = smtplib.SMTP('smtp.office365.com',587)
            server.ehlo()
            server.starttls()
            server.login("smtp email adress", "smtp password")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
sent_email()