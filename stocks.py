from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 5)

#  웹 페이지 주소 위치로 이동
keyword = input('원하는 주식회사를 입력해주세요(단 상장된 회사만 가능): ')

driver.get(f"https://www.google.com/search?q={keyword}+주식")

# css 선택자를 사용하여 원하는 클래스를 가진 웹요소에 접근
name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".DoxwDb"))).text
price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".IsqQVc"))).text
high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최고"]'))).text
low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최저"]'))).text
world_market = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".knFDje"))).text


if world_market == 'KRW':
    price = price + '₩'
    high_price = high_price + "₩"
    low_price = low_price + "₩"
    
elif world_market == 'USD':
    price = price + "$"
    high_price = high_price + "$"
    low_price = low_price + "$"

# 데이터 출력
print(f"애플 주식 정보 수집 완료")
print(f"주식명: {name}")
print(f"현재가: {price}")
print(f"최고가: {high_price}")
print(f"최저가: {low_price}\n")

driver.quit()