#http requests
import requests 
# web scrapping
from bs4 import BeautifulSoup 
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''

# extraction Hacker News Stories

def extract_news(url):
	print('Extracting Hacker News Stories...')
	cnt = ''
	cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
	response = requests.get(url)
	content = response.content
	soup = BeautifulSoup(content, 'html.parser')
	found_content = soup.find_all('td', attrs={'class':'title', 'valign':''})
	for i, tag in enumerate(found_content):
		cnt +=((str(i+1)+' :: '+ tag.text + '\n'+ '<br>') if tag.text != 'more' else '')
		#print(tag.prettify) #find_all('span', attrs={'class': 'sitestr'})
	return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt 
content += ('<br> --------<br>')
content += ('<br><br> End of Message')


# lets send the email
print('Composing Email...')

SERVER = 'smtp.gmail.com' # your smtp server
PORT = 587 # your port number
FROM = 'ericaanapatrice@gmail.com' # your email id (SENDER EMAIL)
TO = 'morisay@gmail.com'  # receiver email id (list of emails)
PASS = 'Momomomo' # your email id's passward

# fb = open(file_name, 'rb')
# create a text/ plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename ='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]'+ ''+ str(now.day) + '-'+ str(now.month)+ '-'+ str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fb.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1) # 1 or 0
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()
