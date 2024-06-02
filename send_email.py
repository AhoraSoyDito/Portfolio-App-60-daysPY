import smtplib, ssl
import os
def main():
    send_email()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "ahorasoydito@gmail.com"
    password = os.getenv("PASSWORD")
    #print(password)
    


    receiver = "ahorasoydito@gmail.com"
    context = ssl.create_default_context()

    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
if __name__ == "__main__":
    main()