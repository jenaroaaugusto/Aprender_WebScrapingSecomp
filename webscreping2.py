# coding: utf-8

import requests
from bs4 import BeautifulSoup

site= requests.get("http://dcomp.ufsj.edu.br/pessoas/professores/")

#print(site.encoding)

soup=BeautifulSoup(site.text,"html.parser")

corpo=soup.find_all("div",{"class":"profile-entry"})
print "Total de Professores:",len(corpo)
for i in corpo:
    print "Professor:",i.h1.text
    print "Área de pesquisa:",i.findAll("p")[2].text
    print "Lattes:",i.findAll("a")[-1]['href']
    print("-------")
