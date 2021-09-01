from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
import sqlite3
import time


def driver_initialize():   # selenium 구동
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	driver = webdriver.Chrome(options=options)
#	driver = webdriver.Chrome('C:/Users/pllab/Desktop/chromedriver/chromedriver.exe'. options=options)
	url = 'https://news.naver.com'
	driver.get(url)
	driver.implicitly_wait(5)
	return driver

def off_clean_bot(driver):    # 클린봇 기능 끄기
	try:
		driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[1]/a').click()
		driver.find_element_by_xpath('//*[@id="cbox_module"]/div[2]/div[7]/a').click()    # -> Error
		driver.find_element_by_xpath('//*[@id="cleanbot_dialog_checkbox_cbox_module"]').click()
		driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]/button').click()
		driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()
	except exceptions.NoSuchElementException:
		driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div/a[1]/div').click()
		driver.find_element_by_xpath('//*[@id="cbox_module"]/div[2]/div[7]/a').click()
		driver.find_element_by_xpath('//*[@id="cleanbot_dialog_checkbox_cbox_module"]').click()
		driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]/button').click()
		driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()
	except:
		return False

def crawling_comment(driver):	# 댓글 크롤링
	temp = []
	comments = driver.find_elements_by_css_selector('span.u_cbox_contents')
	for comment in comments:
		reply = comment.text
		temp.append(reply)
	return temp

def get_info(driver, temp, total_info, news_type):	# db에 넣을 튜플 집합 생성
	src = driver.current_url
	for x in temp:
		date = time.localtime().tm_mday
		length = len(x) - x.count(' ')
		info = [news_type, src, x, length, date]
		if info not in total_info:
			total_info.append( info )
	
def crawl_section(driver, news_type):   # 크롤링 함수
	if news_type not in ["politics", "economy", "society", "life", "world", "it"]:
		print("wrong news_type!")
		return false
	else:
		total_info = []
		for idx in range(1,6):
			try:
				driver.find_element_by_xpath(f'//*[@id="section_{news_type}"]/div[2]/div/ul/li[{idx}]/a').click()
				try:
					driver.find_element_by_xpath('//*[@id="cbox_module"]/div[2]/div[9]/a').click()   # 댓글 바로보기 가능한 경우
					while True:
						try:
							driver.find_element_by_xpath('//*[@id="cbox_module"]/div[2]/div[9]/a/span/span/span[1]').click()
						except:
							temp = crawling_comment(driver)  # db에 저장
							get_info(driver, temp, total_info, news_type)
							driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()
							break
				except exceptions.NoSuchElementException:	# 댓글보기 창이 따로 있는 경우
					try:
						driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div/a[1]/div').click()		# 댓글보기 창 클릭
						while True:
							try:
								driver.find_element_by_xpath('//*[@id="cbox_module"]/div[2]/div[9]/a/span/span/span[1]').click()
							except:
								temp = crawling_comment(driver)  # db에 저장
								get_info(driver, temp, total_info, news_type)
								driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()   # 네이버 기사 홈으로 가기
								break
					except: #exceptions.ElementNotInteractableException:    # 댓글이 달려 있지 않을 경우
						driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()
						pass
				except: #exceptions.ElementNotInteractableException:    # 댓글 바로보기 가능한 경우 - 댓글이 달려 있지 않을 경우
					driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[2]').click()
					pass
			except:
				return total_info
		else:
			return total_info














