from db_controller import *
from konlpy.tag import *

class Total_Data_Analysis(object):
	def __init__(self, db_name):
		self.db_name = db_name
		self.db = db_controller(self.db_name)
		self.low_len = 0
		self.mid_len = 0
		self.high_len = 0

	def get_criteria(self): # 길이 설정
		self.mid_len = self.db.get_total_avg_len()
		self.low_len = self.mid_len-10
		self.high_len = self.mid_len+10

	def get_comment(self, criteria): # 길이 별 댓글 데이터 출력
		if criteria == 'all':
			all_content = self.db.get_total_data(criteria, self.low_len)
			return all_content
		elif criteria == 'low':
			low_len_content = self.db.get_total_data(criteria, self.low_len)
			return low_len_content 
		elif criteria == 'mid':
			mid_len_content = self.db.get_total_data(criteria, self.mid_len)
			return mid_len_content
		elif criteria == 'high':
			high_len_content = self.db.get_total_data(criteria, self.high_len)
			return high_len_content
		elif criteria == 'mid-high':
			mh_len_content = self.db.get_total_data(criteria, self.mid_len)
			return mh_len_content
		else:
			print("wrong criteria!")

	def __del__(self):
		pass

class Length_Analysis(object):
	def __init__(self, db_name, section):
		self.db_name = db_name
		self.db = db_controller(self.db_name)
		self.section = section
		self.low_len = 0
		self.mid_len = 0
		self.high_len = 0
	
	def get_criteria(self): # 길이 설정
		self.mid_len = self.db.get_avg_len(self.section)
		self.low_len = self.mid_len-10
		self.high_len = self.mid_len+10

	def get_section_comment(self, criteria): # 등분 별 댓글 데이터 출력
		if criteria == 'all':
			total_content = self.db.get_data(criteria, self.section, self.low_len)
			return total_content
		elif criteria == 'low':
			low_len_content = self.db.get_data(criteria, self.section, self.low_len)
			return low_len_content 
		elif criteria == 'mid':
			mid_len_content = self.db.get_data(criteria, self.section, self.mid_len)
			return mid_len_content
		elif criteria == 'high':
			high_len_content = self.db.get_data(criteria, self.section, self.high_len)
			return high_len_content
		elif criteria == 'mid-high':
			mh_len_content = self.db.get_data(criteria, self.section, self.mid_len)
			return mh_len_content
		else:
			print("wrong criteria!")

	def total_comment(self): # DB 내 모든 댓글 가져오기
		total_comment = self.db.get_total_comment()
		return total_comment		

	def section_comment(self): # 섹션 내 전체 댓글 불러오기
		section_comment = self.db.get_section_comment(self.section)
		return section_comment