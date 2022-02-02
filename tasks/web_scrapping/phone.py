from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests

url = "https://api.divar.ir/v5/posts/QYcD1qnT/contact/"

contact = requests.get(url)






