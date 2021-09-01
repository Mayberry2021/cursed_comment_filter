from crawler import *
from db_controller import *
import schedule
import time

class Crawl_Schedule(object):
	def __init__(self,db_name):
		self.driver = driver_initialize()
		self.db = db_controller(db_name)
		self.total_info1 = []
		self.total_info2 = []
		self.total_info3 = []
		self.total_info4 = []
		self.total_info5 = []
		self.total_info6 = []

	def off_clean_bot(self):
		off_clean_bot(self.driver)

	def create_table(self):
		self.db.create_table()

	def crawl(self):
		self.total_info1 = crawl_section(self.driver, "politics")  # 크롤링 결과물 [[범주, 주소, 댓글, 길이],[범주, 주소, 댓글, 길이],[범주, 주소, 댓글, 길이]    ...      [범주, 주소, 댓글, 길이],[범주, 주소, 댓글, 길이]]
		self.total_info2 = crawl_section(self.driver, "economy")
		self.total_info3 = crawl_section(self.driver, "society")
		self.total_info4 = crawl_section(self.driver, "life")
		self.total_info5 = crawl_section(self.driver, "world")
		self.total_info6 = crawl_section(self.driver, "it") 

	def save(self):
		self.db.insert(self.total_info1)
		self.db.insert(self.total_info2)
		self.db.insert(self.total_info3)
		self.db.insert(self.total_info4)
		self.db.insert(self.total_info5)
		self.db.insert(self.total_info6)

	def clear_container(self):
		self.total_info1.clear()
		self.total_info2.clear()
		self.total_info3.clear()
		self.total_info4.clear()
		self.total_info5.clear()
		self.total_info6.clear()

	def Act(self):
		self.crawl()
		self.save()
		self.clear_container()

def naming():
	now = time.localtime()
	name = f'{now.tm_year}0{now.tm_mon}0{now.tm_mday}_0{now.tm_hour}_0{now.tm_min}'
	return name

def Auto_Crawling():
	print('old_main')
	now = time.localtime().tm_mday
	name = naming()
	db_name = f'crawler_{name}.db'
	c = Crawl_Schedule(db_name)
	c.create_table()
	c.off_clean_bot()
	print('db create Success!', name)
	while time.localtime().tm_mday == now:
		c.Act()
	else:
		print("day off!")

def Auto_Crawling_4hour():
	now = time.localtime().tm_hour
	name = naming()
	db_name = f'crawler_{name}_off_cleanbot.db'
	c = Crawl_Schedule(db_name)
	c.create_table()
	c.off_clean_bot()
	print('db create Success!', name)
	if (now == 22):
		while True:
			c.Act()
			if time.localtime().tm_hour == 2:
				break
	else:
		while True:
			c.Act()
			if time.localtime().tm_hour == now+4:
				break

Auto_Crawling()
#schedule.every().day.at("00:10").do(Auto_Crawling)

#while True:
#	schedule.run_pending()



