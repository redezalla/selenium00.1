from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.youtube.com/')
driver.get('https://www.fbi.gov/services')