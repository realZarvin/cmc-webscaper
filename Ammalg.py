#Accumulating Email List


from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# URL
base_url = "https://coinmarketcap.com/ico-calendar/ended/?page="


# Email Addresses
email_addresses = []


# Repeating over multiple pages
for page in range(1, 11):
    url = base_url + str(page)

  
    # Pulling HTML content
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the main page (page {page}): {e}")
        continue

  
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

  
    # Find the elements with the specific class
    elements = soup.find_all("a", class_="sc-2b58611b-0 BSke cmc-link")

  
    # Collect the links from the elements
    https_links = []
    for element in elements:
        link = element.get("href")
        if link.startswith("/"):
            https_links.append("https://coinmarketcap.com" + link)
          
    
    # Print the collected https links (for verification)
    for link in https_links:
        print(link)

  
    # Collect email addresses from the project pages
    for link in https_links:
        try:
            # Add a delay to prevent getting blocked
            time.sleep(4.7)
            
            # Send a request to the project page
            response = requests.get(link)
            response.raise_for_status()
            html_code = response.content

          
            # Create a BeautifulSoup object
            soup = BeautifulSoup(html_code, 'html.parser')
            
            # Find the div with the project website links
            parent_element = soup.find("div", class_="sc-16891c57-0 sc-643230d4-0 TYXRf")
            if parent_element:
                child_elements = parent_element.find_all("a")
                href_values = [child.get("href") for child in child_elements]

              
                for each in href_values:
                    if each and "mailto:" in each:
                        email_address = each.split("mailto:")[1]
                        email_addresses.append(email_address)

      
        except requests.exceptions.RequestException as e:
            print(f"Error fetching project page {link}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {link}: {e}")
          

# Saving List of Emails as a CSV file
df = pd.DataFrame(email_addresses, columns=['email'])
df.to_csv('emails.csv', index=False)


print(f'Collected {len(email_addresses)} email addresses.')
#End of Accumulating List




          
#Start of sending Emails


SMTP_SERVER = 'smtp.gmail.com'#Email Configuration 
SMTP_PORT = 587 
EMAIL = 'midasscanner@gmail.com'  # Sending Email, Var?
PASSWORD = 'Melo2006.'  # Password


# Email list accumulated in Phase O
email_list = pd.read_csv('emails.csv')


# Email;
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

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, to_email, msg.as_string())
            print('Email sent to {}'.format(to_email))
    except Exception as e:
        print('Failed to send email to {}: {}'.format(to_email, e))

# Send emails
for index, row in email_list.iterrows():
    recipient_email = row['email']
    body = body_template.format(recipient=recipient_email)
    send_email(recipient_email, subject, body)
    
