import requests
from bs4 import BeautifulSoup
def full_text(url):
    try:
        html=requests.get(url).text
        sp=BeautifulSoup(html,'html.parser')
        p=sp.find_all('p')
        return " ".join([i.get_text() for i in p])
    except Exception as e:
        print(e)