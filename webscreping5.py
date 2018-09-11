# coding: utf-8

# Agora vamos trabalhar com Selenium e usar um User-Agent.
# O segredo é usar o inspecionar elementos..

# In[1]:


from bs4 import BeautifulSoup
import requests


def pegaDetalhes(info):

    info = str(info)
    info = info.split('<div class=\"_label_event\">')
    info = info[2].split('</div></div><div class="feed-media-wrapper">')
    print(info[0])


# Aqui entra a novidade, vamos carregar a biblioteca selenium.

# In[2]:


# o site que queremos crawlear é um site de legendas gratuitas..
site_alvo="https://globoesporte.globo.com/"


# In[3]:


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


# In[6]:


dados=requests.get(site_alvo,headers=headers)
#print dados.text


# In[7]:


#destaques = navegador.find_elements_by_class_name('destaque')
soup=BeautifulSoup(dados.content,"html.parser")


# In[24]:


destaques=soup.find_all("div",{"class":"pigeon"})

print(destaques)
# In[23]:


for destaque in destaques:
    print "Legenda:",destaque.a.text
    print "Detalhes:",destaque.findAll("p")[1].text
    #pegaDetalhes(destaque)
