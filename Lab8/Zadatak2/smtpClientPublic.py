import smtplib

gmail_user = 'marin1985@gmail.com'
gmail_password = 'rdtooskmwzovwoth'

sent_from = gmail_user
to = ['anteprojic@gmail.com']
subject = 'LAB8'
body = 'Testna poruka'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
