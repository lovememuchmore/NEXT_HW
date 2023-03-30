from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'chromedriver_win32'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# file = open ('movie.csv', mode = 'w', newline = '')
# writer = csv.writer(file)
# writer.writerow(['outline', 'dir', 'star'])

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://movie.naver.com/")

# 네이버 영화 순위
# chartbotton = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
# chartbotton.click()
# for i in range(2,11):
#     time.sleep(3)
#     new_i = str(i)
#     s = driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr['+new_i+']/td[2]/div/a').text
#     print(s)
# file.close()





# 좋아하는 영화
# search_box = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/fieldset/div/span/input')
# search_box.send_keys('세 얼간이')
# time.sleep(1)
# chartbotton = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/button')
# chartbotton.click()
# time.sleep(1)
# chartbotton = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[2]/dl/dt/a')
# chartbotton.click()
# title = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/h3/a')
# dir = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a')
# print(title, dir)

# file.close()
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# score = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em')
# score_count = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/span/em')
# print(score, score_count)


#각 영화 클릭 -> 개요, 감독, 평점
# for i in range(2,10):
#     chartbotton = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#     chartbotton.click()
#     time.sleep(1)
#     new_i = str(i)
#     chartbotton = driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr['+new_i+']/td[2]/div/a')
#     chartbotton.click()
#     time.sleep(1)
#     outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#     dir = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#     star = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
# #     if star is not None: 
#        star = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
#     else:
#        star = None
for i in range(13,22):
    chartbotton = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    chartbotton.click()
    time.sleep(1)
    new_i = str(i)
    chartbotton = driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr['+new_i+']/td[2]/div/a')
    chartbotton.click()
    time.sleep(1)
    outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    dir = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    star = input()
    if star is not None: 
         star = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
    else:
         star = None
    print(outline, dir, star)