ICO Email Web Scraper and Outreach Tool

Overview
This project is a web scraper designed to collect email addresses from ended ICO projects listed on CoinMarketCap. The scraper then sends outreach emails inviting project owners to list their projects on a Centralized Exchange (CEX).

Features
Web Scraping: Collects links to ICO project pages and extracts email addresses.
Rate Limiting: Includes a delay between requests to avoid getting blocked.
Error Handling: Handles potential errors during web requests.
Email Outreach: Sends personalized emails to the collected email addresses.
Requirements
Python 3.x
pandas
requests
BeautifulSoup (bs4)
smtplib

Usage
Web Scraper Script (web_scraper.py)
This script scrapes email addresses from ICO project pages on CoinMarketCap and saves them to a CSV file.

Scraping ICO Project Links:

Sends a GET request to the ICO calendar page on CoinMarketCap.
Parses the HTML to extract links to individual project pages.
Extracting Email Addresses:

Visits each project page and looks for email addresses.
Saves collected email addresses to emails.csv.
Email Outreach Script
This script reads email addresses from emails.csv and sends personalized outreach emails.

Load Email List:

Reads emails.csv to get the list of email addresses.
Compose and Send Emails:

Uses SMTP to send personalized emails to each address.

Contribution
Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
