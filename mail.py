import requests,smtplib,config
#this function sends the mail with subject 'subject' , message 'msg' to the user = 'receiever'
def send_email(subject,msg,reciever):
    try:
        #print(reciever)
        #print(msg)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAILADDRESS,config.PASSWORD)
        message = 'Subject:{}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAILADDRESS,reciever,message)
        server.quit()
        print("SUCCESS")
    except:
        print("FAILED")
