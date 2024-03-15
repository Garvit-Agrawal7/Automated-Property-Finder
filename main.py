from selenium import webdriver
from selenium.webdriver.common.by import By
from listings_data import ListingsData

ld = ListingsData()
data = ld.get_listings()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)

browser.get("https://forms.gle/f6hEKu3Ds4yEfBVb7")

address_selector = '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
price_selector = "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
link_selector = '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
button_selector = "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div"

for i in range(len(data)):
    address = browser.find_element(By.CSS_SELECTOR, address_selector)
    price = browser.find_element(By.CSS_SELECTOR, price_selector)
    link = browser.find_element(By.CSS_SELECTOR, link_selector)
    button = browser.find_element(By.CSS_SELECTOR, button_selector)

    address.send_keys(data[i][0])
    price.send_keys(data[i][1])
    link.send_keys(data[i][2])

    button.click()

    browser.get("https://forms.gle/f6hEKu3Ds4yEfBVb7")

browser.quit() #Property data: https://docs.google.com/spreadsheets/d/1vkEqLiEFgnOdBxwzJEc5neLRE3PN30jk5CSRTeZ-YTs/edit?resourcekey#gid=802369170
