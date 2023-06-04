import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
link = "https://www.malaysiakini.com/news/655717"
response = requests.get(link)
soup = BeautifulSoup(response.content, "html.parser")

# Check if the request was successful
if soup.find("div", class_="article-content") is not None:
    text = soup.find("div", class_="article-content").get_text()
    print(text)
else:
	text = soup.get_text()
	print(text)
