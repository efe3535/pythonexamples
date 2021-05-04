from selenium import webdriver
from time import sleep

PATH = "chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://covid19.saglik.gov.tr/")
title = driver.find_element_by_tag_name("title")

print(title)