import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
#SMTP fot gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 
EMAIL = 'midasscanner@gmail.com'  # Remember to ask Yagaz to make a Gmail for our web scraper
PASSWORD = 'Melo2006.' 

# Yagaz abeg make code to be saved as a CSV file
email_list = pd.read_csv('emails.csv')

# Trying to make a letter template for our outreach
# I need the recipent to be able to change each cycle.
subject = "Opportunity to List Your Project on Our CEX"
body_template = """
Dear {recipient},

We are reaching out to invite you to list your project on our Centralized Exchange (CEX). Our platform offers a range of benefits, including increased visibility and access to a large user base.

If you are interested, please reply to this email, and we will provide you with more details on how to proceed.

Best regards,
zarvin
Community Manager
zarvinns@gmail.com
"""

# Improvising an email to send emails (yagaz look at this shit, i might be getting it wrong.)
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD) #changing var?
            server.sendmail(EMAIL, to_email, msg.as_string())
            print('Email sent to {}'.format(to_email))
    except Exception as e:
        print('Failed to send email to {}: {}'.format(to_email, e))

# Send emails
for index, row in email_list.iterrows():
    recipient_email = row['email']
    # Yagaz, review this part that's talking about recipient
    body = body_template.format(recipient=recipient_email)
    send_email(recipient_email, subject, body)
          
