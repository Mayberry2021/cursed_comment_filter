from konlpy.tag import *
import os

class Morpheme_Count(object):
	def __init__(self):
		self.kkma = Kkma()
		self.okt = Okt()
		self.valued_pos = ["NNB","NNG","NP","VV","VA","MAG","IC","JKS","JKM","ECD","EPH","EPT","EPP","EFN","EFQ","EFO","EFA","EFI","EFR","XSN","XR"]
		self.rpct_xr = [ "습니","ㅂ니","요","ㅂ시"]
		self.rpct_nng_list = ["진지","성함","연세","댁","부인","생신","따님","말씀"]
		self.rpct_vv_list = ["계시","드","모시","뵙","뵈","여쭈"] 
		self.etc_pos = ['SF','SE','SS','SP','SO','SW','OH','OL','UN','EMO']
		with open("malword.txt", "r", encoding='utf-8') as file:
			self.malword_set = []
			while True:
				mal = file.readline()
				if not mal:
					break
				text = mal.rstrip('\n')
				self.malword_set.append(text)

	def rmEmoji(self, comment):  
		return comment.encode('euc-kr', 'ignore').decode('euc-kr')

	def t_analysis(self, comment):
		try:
			result = self.kkma.pos(comment)
			return len(result)
		except:
			return 20

	def v_analysis(self, comment):  
		vpos = 0
		try:
			result = self.kkma.pos(comment)
			for corpus in result:
				if corpus[1] in self.valued_pos:
					vpos += 1
			else:
				return vpos
		except:
			return 20

	def emoti_analysis(self, comment):
		epos = 0
		try:
			result = self.kkma.pos(comment)
			for corpus in result:
				if corpus[1] in self.etc_pos:
					epos += 1
			else:
				return epos
		except:
			return 20

	def p_analysis(self, comment):  # 댓글 내 존대어 형태소 개수 계산
		ppos = 0
		try:
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
		except:
			return 0

	def c_analysis(self, comment):
		cpos = 0
		result = self.okt.pos(comment)
		for morphs in result:
			if morphs[0] in self.malword_set:
				cpos += 1
		else:
			return cpos

	def text_out(self, total):
		with open('morpheme_data.txt', 'w', encoding='utf-8') as file:
			for tag_count_list in total:
				text = str(tag_count_list[2]) + '\t' + str(tag_count_list[3]) + '\t' + str(tag_count_list[4]) +'\n'
				file.write(text)

	def m_analysis(self, content_list):
		total = []
		for comment in content_list:
			tag_count_list = []
			r_comment = self.rmEmoji(comment)
			tag_count_list.append(comment)  # 0
			length = len(comment) - comment.count(' ')
			tag_count_list.append(length)	# 1 
			vpos = self.v_analysis(r_comment)
			tag_count_list.append(vpos)		# 2
			ppos = self.p_analysis(r_comment)
			tag_count_list.append(ppos)		# 3
			cpos = self.c_analysis(r_comment)
			tag_count_list.append(cpos)		# 4
			tpos = self.t_analysis(r_comment)
			tag_count_list.append(tpos)		# 5
			epos = self.emoti_analysis(r_comment)
			tag_count_list.append(epos)		# 6
			npos = tpos-vpos
			tag_count_list.append(npos)		# 7
			t_c_pos = tpos - cpos
			tag_count_list.append(t_c_pos)	# 8
			v_c_pos = vpos - cpos
			tag_count_list.append(v_c_pos)	# 9
			c1 = cpos * (vpos - cpos) * npos
			tag_count_list.append(c1)		# 10
			c2 = cpos * (vpos - cpos) * epos
			tag_count_list.append(c2)		# 11
			total.append(tag_count_list)
		else:
			self.text_out(total)
			return total

	def soundness_analysis(self, name, total, wr, wc):
#		wr, wc = 1, 1		# (1, 1/2) and (1/2, 1)
		with open('morpheme_data.txt','r',encoding='utf-8') as file, open(f'./{name}.csv', 'w',encoding='utf-8-sig') as file2:
			morpheme_data = file.readlines()
			for x in range(0, len(morpheme_data)):
				data = list(map(int, morpheme_data[x].rstrip('\t').rstrip('\n').split('\t')))
				try:
					sound_rate = wr*(data[1]/data[0])-wc*(data[2]/data[0])
					text = str(total[x][0]) + '\t' + str(total[x][1]) + '\t' + str(sound_rate) + '\t' + str(total[x][1] * sound_rate) + '\t' + str(total[x][5]) + '\t' + str(total[x][2]) + '\t' + str(total[x][7]) + '\t' + str(total[x][8]) + '\t' + str(total[x][9]) + '\t' + str(total[x][4]) + '\t' + str(total[x][6]) + '\t' + str(total[x][3]) + '\t'+ str(total[x][10]) + '\t' + str(total[x][11]) + '\n'
					file2.write(text)
				except ZeroDivisionError:
					with open('abnormal_analysis.csv', 'a', encoding='utf-8-sig') as file3:
						text = str(total[x][0]) + '\t' + str(total[x][1]) + '\t' + str(sound_rate) + '\t' + str(total[x][1] * sound_rate) + '\t' + str(total[x][5]) + '\t' + str(total[x][2]) + '\t' + str(total[x][7]) + '\t' + str(total[x][8]) + '\t' + str(total[x][9]) + '\t' + str(total[x][4]) + '\t' + str(total[x][6]) + '\t'+ str(total[x][3]) + '\t'+ str(total[x][2]-(total[x][3]+total[x][4])) + '\t' + str(total[x][10]) + '\t' + str(total[x][11]) + '\n'
						file3.write(str(text))
					pass
			else:
				print("댓글 건전도1 산출 완료!")

	def __del__(self):
		pass