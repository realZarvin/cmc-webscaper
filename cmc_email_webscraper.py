from bs4 import BeautifulSoup
import requests



#defining the url
url = "https://coinmarketcap.com/ico-calendar/ended/?page=2"

#sending a get request to the url and getting the html info
response = requests.get(url)
html_content = response.content

#creating a beautiful soup object to parse the html
soup = BeautifulSoup(html_content, "html.parser")
 
#finding the elements with the specific class
elements = soup.find_all("a", class_= "sc-2b58611b-0 BSke cmc-link")

#for collecting the links from the elements
https_links =[]
for element in elements:
    link = element.get("href")
    # petch here !!!!
    if link.startswith("/"):
        https_links.append("https://coinmarketcap.com" + link)
        
        #print the https links 
        for links in https_links:
            print(links)
# FOR GETTING THE WEBSITE LINKS FROM CMC
for link in https_links:
   # Send a request to the webpage
   response = requests.get(link)
   html_code = response.content

   # Create a BeautifulSoup object
   soup = BeautifulSoup(html_code, 'html.parser')
# FOR SEARCHING FOR THE HREF INSIDE THE CLASS
   parent_element = soup.find("div", class_="sc-16891c57-0 sc-643230d4-0 TYXRf")
   if parent_element:
       child_elements = parent_element.find_all("a")
       href_values = [child.get("href") for child in child_elements]
       for each in href_values:
           print(each)
           
   
       
          
       
        



