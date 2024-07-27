from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# Url
url = "https://coinmarketcap.com/ico-calendar/ended/?page=2"

# Getting HTML content
try:
    response = requests.get(url)
    response.raise_for_status()
    html_content = response.content
except requests.exceptions.RequestException as e:
    print(f"Error fetching the main page: {e}")
    exit()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the elements with the specific class
elements = soup.find_all("a", class_="sc-2b58611b-0 BSke cmc-link")

# Collect the links from the elements
#I don't even understand this part 
https_links = []
for element in elements:
    link = element.get("href")
    if link.startswith("/"):
        https_links.append("https://coinmarketcap.com" + link)

# Print the collected https link
for link in https_links:
    print(link)

# Collect email addresses from the project pages
#Use Email address to make a list for the CSV file
email_addresses = []

for link in https_links:
    try:
        # 2s too small, need time lim of >3s
        time.sleep(4.7)
        
        # Send a request to the project page
        response = requests.get(link)
        response.raise_for_status()
        html_code = response.content

        # Create a BeautifulSoup object
        # I no understand this shit
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

# Saving information to a CSV file
df = pd.DataFrame(email_addresses, columns=['email'])
df.to_csv('emails.csv', index=False)

print(f'Collected {len(email_addresses)} email addresses.')
#Cooked!
