from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라주저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)
# 브라우저를 자동화한 후 >> browser window 창 유지
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

# excludeSwitches: 불필요한 로깅 메시지 >> 브라우저에서 제외

driver = webdriver.Chrome(options=chrome_options)

keyword = input('뉴스 키워드 입력해 주세요: ')
driver.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}')

# 뉴스 출처 >> info.press
# api_txt_lines dsc_txt_wrap

ref_list = driver.find_elements(By.CLASS_NAME, 'info.press')
cont_list = driver.find_elements(By.CLASS_NAME, 'api_txt_lines.dsc_txt_wrap')

for i in range(len(ref_list)):
    refer = ref_list[i].text
    contn = cont_list[i].text
    print(refer)
    print(contn)


driver.quit()
