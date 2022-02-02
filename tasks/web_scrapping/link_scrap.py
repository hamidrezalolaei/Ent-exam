from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://divar.ir/s/tehran/real-estate"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
app = soup.find(id = "app")
houses = app.find_all('a', attrs={'class' : 'kt-post-card kt-post-card--outlined', 'class' : 'kt-post-card kt-post-card--outlined kt-post-card--has-chat'})
new_soup = BeautifulSoup(str(houses), 'html.parser')
ref_list = [a['href'] for a in new_soup.find_all('a', href=True)]
print(ref_list)
