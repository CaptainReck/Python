from bs4 import BeautifulSoup
import requests
url="https://www.newegg.com/p/pl?d=mobile"
result = requests.get(url)

doc=BeautifulSoup(result.text,"html.parser")


data=doc.find_all('a',class_='item-title','')
print(data)