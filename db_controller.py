import sqlite3
import time

class db_controller(object):
	def __init__(self, db_name):
		self.db = sqlite3.connect(db_name)
		self.curs = self.db.cursor()

	def checking_duplicate(self, content): # 댓글 중복 검사
		sql = 'SELECT content FROM comment_set WHERE content==?'
		result = self.curs.execute(sql, [content])
		if (not result.fetchone()):
			return True
		else:
			return False

	def create_table(self):   # 테이블 생성
		self.curs.execute('CREATE TABLE comment_set (part, src, content, length, date)')

	def insert(self,total_info):   # 댓글 데이터 삽입
		sql = f"INSERT INTO comment_set (part, src, content, length, date) values (?,?,?,?,?)"
		for x in total_info:
			if (self.checking_duplicate(x[2])):
				self.curs.execute(sql,(x[0], x[1], x[2], x[3],x[4]))
		self.db.commit()

	def get_total_avg_len(self):  # DB 내 전체 댓글 평균 길이 반환
		sql = 'SELECT AVG(length) FROM comment_set'
		result = self.curs.execute(sql).fetchone()
		return result[0]

	def get_avg_len(self, part):  # 섹션 내 댓글 평균 길이 반환
		sql = 'SELECT AVG(length) FROM comment_set WHERE part == ?'
		result = self.curs.execute(sql, [part]).fetchone()
		return result[0]

	def get_total_comment(self):  # DB 내 모든 댓글 가져오기
		total = []
		sql = 'SELECT content FROM comment_set'
		result = self.curs.execute(sql).fetchall()
		for x in result:
			total.append(x[0])
		return total

	def get_section_comment(self, part):  # 섹션 내 모든 댓글 가져오기
		total = []
		sql = 'SELECT content FROM comment_set WHERE part == ?'
		result = self.curs.execute(sql, [part]).fetchall()
		for x in result:
			total.append(x[0])
		return total

	def get_data(self, criteria, part, length):  # 섹션 및 등분별 댓글 데이터 가지고 오기 
		if criteria == 'all':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE part==?'
			result = self.curs.execute(sql, [part]).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'low':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE part==? AND length <= {length}'
			result = self.curs.execute(sql,[part]).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'mid':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE part==? AND length > {length}-10 AND length < {length}+10'
			result = self.curs.execute(sql,[part]).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'high':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE part==? AND length >= {length}'
			result = self.curs.execute(sql,[part]).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'mid-high':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE part==? AND length >= {length}'
			result = self.curs.execute(sql,[part]).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set

	def get_total_data(self, criteria, length):  # DB내 전체 댓글 데이터 등분별로 구분하여 가지고 오기 
		if criteria == 'all':
			text_set = []
			sql = f'SELECT content, length FROM comment_set'
			result = self.curs.execute(sql).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'low':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE length <= {length}'
			result = self.curs.execute(sql).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'mid':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE length > {length}-10 AND length < {length}+10'
			result = self.curs.execute(sql).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'high':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE length >= {length}'
			result = self.curs.execute(sql).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set
		elif criteria == 'mid-high':
			text_set = []
			sql = f'SELECT content, length FROM comment_set WHERE length >= {length}'
			result = self.curs.execute(sql).fetchall()
			for data in result:
				text_set.append(data[0])
			return text_set