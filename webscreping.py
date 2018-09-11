import requests
from bs4 import BeautifulSoup

site= requests.get("http://example.com")
print(site.status_code)

soup=BeautifulSoup(site.content,"html.parser")

print (soup.find_all("h1")[0].text)
print("Ar")
print(soup.select("p"))
print("\n")

links = soup.select("a")
print(links)

for  link in links:
    print(link['href'])
