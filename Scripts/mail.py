import smtplib

def sendMail(sender,receiver,link):
	messag = 'You have been invited to join the meeting by '+sender+' . Please click on the link to join '+link
	message = 'Subject: {}\n\n{}'.format('Meeting Invitation',str(messag))
	#print(message)
	server=smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login("testiotsap@gmail.com","dynamo2818")
	server.sendmail("testiotsap@gmail.com",receiver,message)
	server.quit()

sendMail("nishantnimbalkar98@gmail.com","nimbalkarnishant98@gmail.com","http://test.php")