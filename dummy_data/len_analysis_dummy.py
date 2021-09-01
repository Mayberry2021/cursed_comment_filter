#class Total_Data_Length_Analysis(object):
#	def __init__(self, db_name):
#		self.db_name = db_name
#		self.db = db_controller(self.db_name)
#		self.low_len = 0
#		self.mid_len = 0
#		self.high_len = 0

#	def get_criteria(self): # 등분 기준 길이 설정
#		self.mid_len = self.db.get_total_avg_len()
#		self.low_len = self.mid_len-10
#		self.high_len = self.mid_len+10

#	def get_content_data(self, criteria): # 등분 별 댓글 데이터 출력
#		if criteria == 'low':
#			low_len_content = self.db.get_total_data(criteria, self.low_len)
#			return low_len_content 
#		elif criteria == 'mid':
#			mid_len_content = self.db.get_total_data(criteria, self.mid_len)
#			return mid_len_content
#		elif criteria == 'high':
#			high_len_content = self.db.get_total_data(criteria, self.high_len)
#			return high_len_content
#		elif criteria == 'mid-high':
#			mh_len_content = self.db.get_total_data(criteria, self.mid_len)
#			return mh_len_content
#		else:
#			print("wrong criteria!")

#	def __del__(self):
#		pass


#	def asc_order(self):
#		total = self.db.ascend_order(self.section)
#		return total

#	def get_criteria_by_user(self, low, mid, high):
#		self.low_len = low
#		self.mid_len = mid
#		self.high_len = high

#	def show_len(self): # 길이 별 3등분 결과 값 출력
#		print(self.section,'_part 저:',self.low_len, '중:',self.mid_len, '고:',self.high_len)


#	def section_total_comment(self):   # DB 내 섹션별 댓글 수 측정
#		total_comment_len = self.db.get_total_comment_by_part(self.section)
#		return total_comment_len

#	def get_total_length(self, content_list): # 섹션 내 전체 댓글 수 / 어조별 전체 댓글 수
#		count = len(content_list)
#		return count

#	def get_avg_len_by_tone(self, comment_list_by_tone):   # 어조별 댓글 평균 길이
#		avg_len = 0
#		sum = 0
#		for comment in comment_list_by_tone:
#			length = len(comment) - comment.count(' ')
#			sum += length
#		else:
#			avg_len = sum / len(comment_list_by_tone)
#		return avg_len

#	def get_min_len_comment(self, part):  # 섹션별 최소 길이
#		min_len = self.db.get_min_len(part)
#		return min_len

#	def get_min_len_comment_by_tone(self, comment_list_by_tone):  # 어조별 댓글 최소 길이
#		min_len = 0
#		len_set = []
#		for comment in comment_list_by_tone:
#			comment_len = len(comment)-comment.count(' ')
#			len_set.append(comment_len)
#		else:
#			min_len = min(len_set)
#			return min_len


#	def count_all_comment(self):  # DB 내 전체 댓글 수 측정
#		all_comment_count = self.db.count_total_comment()
#		return all_comment_count

#	def total_comment_data_part(self): # DB 내 전체 댓글 불러오기
#		total_comment = self.db.get_total_comment_data_part()
#		return total_comment

#	def section_total_comment(self):   # DB 내 섹션별 댓글 수 측정
#		total_comment_len = self.db.get_total_comment_by_part(self.section)
#		return total_comment_len

#	def get_avg_len_by_part(self):  # 섹션별 댓글 평균 길이 반환
#		avg_len = self.db.get_avg_len(self.section)
#		return avg_len