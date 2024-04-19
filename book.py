from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 주소의 위치로 이동
path = "https://product.kyobobook.co.kr/bestseller/online?period=001&per=50"
driver.get(path)

books = driver.find_elements(By.CLASS_NAME, 'prod_item')

for index, book in enumerate(books):
    title = book.find_element(By.CLASS_NAME, 'prod_info').text
    author = book.find_element(By.CLASS_NAME, 'prod_author').text
    rank = index + 1
    price = book.find_element(By.CLASS_NAME, 'price').text
    
    print(rank, title, author, price)

driver.quit()