# 사용 할 패키지, 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import sys

input_text = sys.argv[1]

# 크롬 제어 변수 선언
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 선언한 driver 동작 제어 시간 10초
driver.implicitly_wait(10)

# 네이버 접속
driver.get("https://www.naver.com")

# 검색창 선택
search_box = driver.find_element(By.CSS_SELECTOR, "input#query.search_input")

# 검색어 입력
search_box.send_keys(input_text)
# search_box.send_keys("파이썬")

# 검색 실행(enter)
search_box.send_keys(Keys.ENTER)

# 뉴스 탭 선언
news_tab = driver.find_element(By.LINK_TEXT,"뉴스")

# 뉴스 탭 클릭
news_tab.click()

# 로딩 시간을 위해 2초 대기
time.sleep(2)

# 현재 페이지의 html 소스 가져오기
html = driver.page_source

# html 소스 BeautifulSoup 형식으로 변환
soup = BeautifulSoup(html,"lxml") # pip install lxml

# 뉴스 제목 span 태그의 class를 선택
title = soup.select("span.sds-comps-text-type-headline1")

# 리스트의 갯수
print("총 뉴스 기사의 갯수는",len(title),"개 입니다.")

# 리스트 출력
for i in title:
    print(i.get_text(strip=True))

# 웹 브라우저 종료
driver.quit()