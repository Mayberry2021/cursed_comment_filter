#	def ascend_order(self, part):
#		sql = 'SELECT content, length FROM comment_set WHERE part == ? ORDER BY length'
#		result = self.curs.execute(sql, [part]).fetchall()
#		total = []
#		for x in result:
#			part1 = []
#			part1.append(x[0])
#			part1.append(x[1])
#			total.append(part1)
#		return total

#	def get_total_avg_len(self):  # DB 내 전체 댓글 평균 길이 반환
#		sql = 'SELECT AVG(length) FROM comment_set'
#		result = self.curs.execute(sql).fetchone()
#		return result[0]

#	def get_avg_len(self, part):  # 섹션별 댓글 평균 길이 반환
#		sql = 'SELECT AVG(length) FROM comment_set WHERE part == ?'
#		result = self.curs.execute(sql, [part]).fetchone()
#		return result[0]

#	def get_total_comment_data_part(self):  # DB 내 모든 댓글 가져오기(파트도 함께)
#		total = []
#		sql = 'SELECT part, content FROM comment_set'
#		result = self.curs.execute(sql).fetchall()
#		for x in result:
#			part1 = []
#			part1.append(x[0])
#			part1.append(x[1])
#			total.append(part1)
#		return total

#	def get_total_comment_by_part(self, part):  # DB 내 섹션별 댓글 데이터 총 개수 가져오기
#		sql = 'SELECT content FROM comment_set WHERE part==?'
#		result = self.curs.execute(sql, [part]).fetchall()
#		total_comment = len(result)
#		return total_comment