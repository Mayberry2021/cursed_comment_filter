from konlpy.tag import *

class Cursed_Analysis(object):   # 댓글 데이터 내 비속어 댓글 분석
	def __init__(self, section, content_list):
		self.section = section
		self.out_list = []   # 비속어 제외 댓글 데이터
		self.cursed_list = []
		self.malword_set = []
		self.okt = Okt()
		self.content_list = content_list

	def get_cursed_list(self): # 비속어 댓글 모음 반환
		return self.cursed_list

	def get_out_list(self):
		return self.out_list

	def get_malword_set(self):  # 비속어 목록 로드
		print('slang_malword 데이터 반환!')
		return self.malword_set

	def malword_loader(self):   # 비속어 목록 불러오기 / 비속어 목록 파일 이름은 malword.txt로 고정해놓아야 함
		with open("malword.txt", "r", encoding="UTF-8") as file:
			while True:
				mal = file.readline()
				if not mal:
					break
				text = mal.rstrip('\n')
				self.malword_set.append(text)

	def check_cursed(self):  # 댓글 데이터 내 비속어 댓글 수 체크
		cursed_comment_count = 0
		for comment in self.content_list:
			cursed_word_count = 0
			text = self.okt.pos(comment)
			for morphs in text:
				if morphs[0] in self.malword_set:
					cursed_word_count += 1
			if(cursed_word_count):
				cursed_comment_count += 1
			else:
				pass
		else:
			return cursed_comment_count

	def make_cursed_list(self):   # 댓글 데이터 내 비속어 댓글 추출하기
		for comment in self.content_list:
			cursed_word_count = 0
			text = self.okt.pos(comment)
			for morphs in text:
				if morphs[0] in self.malword_set:
					cursed_word_count += 1
			if(cursed_word_count):
				self.cursed_list.append(comment)

	def make_out_list(self):
		for comment in self.content_list:
			if comment not in self.cursed_list:
				self.out_list.append(comment)

	def cursed_text_out(self):  # 비속어 댓글 텍스트 파일로 출력
		with open(f'./cursed_of_{self.section}.txt','w', encoding='utf-8') as file:
			for comment in self.cursed_list:
				comments = str(comment) + '\n'
				file.write(comments)

	def out_text_out(self):  # 아웃 리스트 댓글 텍스트 파일로 출력
		with open(f'./outlist_of_{self.section}.txt','w', encoding='utf-8') as file:
			for comment in self.out_list:
				comments = str(comment) + '\n'
				file.write(comments)

	def __del__(self):
		pass

class Polite_Analysis(object):   # 존대어 분석
	def __init__(self, section, content_list):
		self.section = section
		self.content_list = content_list
		self.out_list = []	# 존대어 제외하고 남은 데이터
		self.polite_list = []
		self.rpct_xr = [ "습니","ㅂ니","요","ㅂ시"]
		self.rpct_nng_list = ["진지","성함","연세","댁","부인","생신","따님","말씀"]
		self.rpct_vv_list = ["계시","드","모시","뵙","뵈","여쭈"] 
		self.kkma = Kkma()

	def get_polite_list(self):
		return self.polite_list

	def get_out_list(self):
		return self.out_list

	def rmEmoji(self, comment):
		return comment.encode('euc-kr', 'ignore').decode('euc-kr')

	def check_polite(self):      # 댓글 데이터 내 존대어 댓글 개수 체크
		polite_count = 0
		for comment in self.content_list:
			polite_word_count = 0
			cleaned_comment = self.rmEmoji(comment)
			text = self.kkma.pos(cleaned_comment)
			for corpus in text:
				if corpus[1] in ["EPH", "EPP", "EFR"]:
					polite_word_count += 1
				elif ((corpus[1] in ["ECD", "EFN", "EFQ", "EFI"]) and (corpus[0] in self.rpct_xr)):
					polite_word_count += 1
				elif ((corpus[1] in ["JKS", "JKM"]) and (corpus[0] in ["께","께서"])):
					polite_word_count += 1
				elif ((corpus[1] in ["NP"]) and (corpus[0] in ["저", "저희"])):
					polite_word_count += 1
				elif ((corpus[1] in ["VV"]) and (corpus[0] in self.rpct_vv_list)):
					polite_word_count += 1
				elif ((corpus[1] in ["NNG", "XR"]) and (corpus[0] in self.rpct_nng_list)):
					polite_word_count += 1
				else:
					pass
			if(polite_word_count):
				polite_count += 1
			else:
				pass
		else:
			return polite_count
			
	def make_polite_list(self):		# 댓글 데이터 내 존대어 댓글 추출
		for comment in self.content_list:
			polite_word_count = 0
			cleaned_comment = self.rmEmoji(comment)
			text = self.kkma.pos(cleaned_comment)
			for corpus in text:
				if corpus[1] in ["EPH", "EPP", "EFR"]:
					polite_word_count += 1
				elif ((corpus[1] in ["ECD", "EFN", "EFQ", "EFI"]) and (corpus[0] in self.rpct_xr)):
					polite_word_count += 1
				elif ((corpus[1] in ["JKS", "JKM"]) and (corpus[0] in ["께","께서"])):
					polite_word_count += 1
				elif ((corpus[1] in ["NP"]) and (corpus[0] in ["저", "저희"])):
					polite_word_count += 1
				elif ((corpus[1] in ["VV"]) and (corpus[0] in self.rpct_vv_list)):
					polite_word_count += 1
				elif ((corpus[1] in ["NNG", "XR"]) and (corpus[0] in self.rpct_nng_list)):
					polite_word_count += 1
				else:
					pass
			if(polite_word_count):
				self.polite_list.append(comment)
			else:
				pass

	def make_out_list(self):   # 존대어 제외 댓글 파일 생성
		for comment in self.content_list:
			if comment not in self.polite_list:
				self.out_list.append(comment)

	def text_out(self):  # 존대어 댓글 텍스트 파일로 출력
		with open(f'./respect_of_{self.section}.txt','w', encoding='utf-8') as file:
			for comment in self.polite_list:
				comments = str(comment) + '\n'
				file.write(comments)

	def __del__(self):
		pass

class Ordinary_Analysis(object):    # 예사어 분석
	def __init__(self, section, content_list):
		self.section = section
		self.content_list = content_list

	def get_ordinary_list(self):   # 예사어 리스트 반환
		return self.content_list

	def check_ordinary(self):		# 예사어 댓글 수 체크
		ordinary_comment_count = len(self.content_list)
		return ordinary_comment_count

	def text_out(self):  # 예사어 댓글 텍스트 파일로 출력
		with open(f'./ordinary/ordinary_of_{self.section}.txt','w', encoding='utf-8') as file:
			for comment in self.content_list:
				comments = str(comment) + '\n'
				file.write(comments)

	def __del__(self):
		pass

class Before_Soundness(object):
	def __init__(self):
		self.kkma = Kkma()
		self.okt = Okt()
		self.valued_pos = ["NNB","NNG","NP","VV","VA","MAG","IC","JKS","JKM","ECD","EPH","EPT","EPP","EFN","EFQ","EFO","EFA","EFI","EFR","XSN","XR"]
		self.rpct_xr = [ "습니","ㅂ니","요","ㅂ시"]
		self.rpct_nng_list = ["진지","성함","연세","댁","부인","생신","따님","말씀"]
		self.rpct_vv_list = ["계시","드","모시","뵙","뵈","여쭈"] 
		self.malword_set = []
			
	def malword_loader(self):
		with open("malword.txt", "r", encoding="UTF-8") as file:
			while True:
				mal = file.readline()
				if not mal:
					break
				text = mal.rstrip('\n')
				self.malword_set.append(text)
			else:
				print('malword load 완료!')		

	def rmEmoji(self, comment):  
		return comment.encode('euc-kr', 'ignore').decode('euc-kr')

	def t_analysis(self, comment):  
		tpos = 0
		result = self.kkma.pos(comment)
		for corpus in result:
			if corpus[1] in self.valued_pos:
				tpos += 1
		else:
			return tpos

	def p_analysis(self, comment):  # 댓글 내 존대어 형태소 개수 계산
		ppos = 0
		result = self.kkma.pos(comment)
		for corpus in result:
			if corpus[1] in ["EPH", "EPP", "EFR"]:
				ppos += 1
			elif ((corpus[1] in ["ECD", "EFN", "EFQ", "EFI"]) and (corpus[0] in self.rpct_xr)):
				ppos += 1
			elif ((corpus[1] in ["JKS", "JKM"]) and (corpus[0] in ["께"])):
				ppos += 1
			elif ((corpus[1] in ["NP"]) and (corpus[0] in ["저", "저희"])):
				ppos += 1
			elif ((corpus[1] in ["VV"]) and (corpus[0] in self.rpct_vv_list)):
				ppos += 1
			elif ((corpus[1] in ["NNG", "XR"]) and (corpus[0] in self.rpct_nng_list)):
				ppos += 1
			else:
				pass
		else:
			return ppos

	def c_analysis(self, comment):
		cpos = 0
		result = self.okt.pos(comment)
		for morphs in result:
			if morphs[0] in self.malword_set:
				cpos += 1
		else:
			return cpos

	def text_out(self, morpheme_data):
		with open('morpheme_data.txt', 'w', encoding='utf-8') as file:
			for tag_count_list in morpheme_data:
				text = str(tag_count_list[0]) + '\t' + str(tag_count_list[1]) + '\t' + str(tag_count_list[2]) + '\n'
				file.write(text)

	def m_analysis(self, content_list):
		total = []
		for comment in content_list:
			tag_count_list = []
			r_comment = self.rmEmoji(comment)
			tpos = self.t_analysis(r_comment)
			tag_count_list.append(tpos)
			ppos = self.p_analysis(r_comment)
			tag_count_list.append(ppos)
			cpos = self.c_analysis(r_comment)
			tag_count_list.append(cpos)
			total.append(tag_count_list)
		else:
			self.text_out(total)

	def __del__(self):
		pass