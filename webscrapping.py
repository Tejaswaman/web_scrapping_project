#Web Scrapping

# step1:install pip and bs4
#install pip
#install bs4
# import libraries
import requests
from bs4 import BeautifulSoup
# step 2: set the url and get the webpage specified in the url.
url="https://codewithharry.com"
#get the html
content = requests.get(url)
htmlContent= content.content
print(htmlContent)
# Parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)


# html traversal
# title=soup.title
print(soup.find('title'))
# get all the tag 
content=soup.find_all("div",class_='toc')
for i in content:
    print(i.text)
