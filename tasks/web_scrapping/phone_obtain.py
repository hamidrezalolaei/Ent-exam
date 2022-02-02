from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import contextlib as closing

url = "https://divar.ir/v/%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%DB%B1%DB%B4%DB%B2-%D9%85%D8%AA%D8%B1%DB%8C-%DB%B3-%D8%AE%D9%88%D8%A7%D8%A8%D9%87-%D8%AA%DA%A9-%D9%88%D8%A7%D8%AD%D8%AF%DB%8C_%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86_%D8%AA%D9%87%D8%B1%D8%A7%D9%86_%D8%A7%D9%86%D8%AF%DB%8C%D8%B4%D9%87_%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/QY5TblWc"


# page = requests.get(url)

# soup = BeautifulSoup(page.content, 'html.parser')
# driver = webdriver.Chrome()
# button = driver.find_element_by_class_name("kt-button kt-button--primary post-actions__get-contact")
# button.click()
# # wait to load
# element = wait(driver, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "kt-unexpandable-row__action kt-text-truncate ltr")))
# # print(element)
# page_source = driver.page_source

# soup = BeautifulSoup(page_source)
# items = soup.find('div', {"class":"kt-unexpandable-row__action kt-text-truncate ltr"})
# print(items)