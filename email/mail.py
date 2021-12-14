import smtplib, ssl

port = 456 # for ssl
smtp_server = "smtp.gmail.com"
sender_email = "morisasy@gmail.com"
receiver_email = "modlove@gmail.com"
password = "lovelyday"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context= context) as server:
	try:
		server.log(sender_email, password)
		response = server.sendmai(sender_email, receiver_email, message)
		print('Email Sent!')

	except:
		print('Could not login or send the mail.')