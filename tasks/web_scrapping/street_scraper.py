from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://divar.ir/s/tehran/real-estate"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
app = soup.find(id = "app")
streets = app.find_all('div', attrs={'class' : 'multi-select-modal__list'})
new_soup = BeautifulSoup(str(streets), 'html.parser')
ref_list = [a['href'] for a in new_soup.find_all('a', href=True)]
print(ref_list)
