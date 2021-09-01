from morpheme_analysis import *
from len_analysis import *
from math import *

class Sound_Analysis(object):
	def __init__(self, section, content_list):
		self.section = section
		self.content_list = content_list
		self.soundness = Before_Soundness()
		self.soundness.malword_loader()
		self.analysis_list = []

	def analysis1(self, name):
		self.soundness.m_analysis(self.content_list)
		with open('morpheme_data.txt','r',encoding='utf-8') as file, open(f'./sound/{name}.csv', 'w',encoding='utf-8') as file2:
			total = file.readlines()
			for x in range(0, len(total)):
				data = list(map(int, total[x].rstrip('\t').rstrip('\n').split('\t')))
				try:
					sound_rate = 1*(data[1]/data[0])-1*(data[2]/data[0])
					self.analysis_list.append(sound_rate)
					text = str(self.content_list[x]) + '\t' + str(sound_rate) + '\n'
					file2.write(text)
				except ZeroDivisionError:
					pass
			else:
				print("댓글 건전도1 산출 완료!")

	def analysis2(self, name):
		self.soundness.m_analysis(self.content_list)
		with open('morpheme_data.txt','r',encoding='utf-8') as file, open(f'./sound/{name}.csv', 'w',encoding='utf-8') as file2:
			total = file.readlines()
			for x in range(0, len(total)):
				data = list(map(int, total[x].rstrip('\t').rstrip('\n').split('\t')))
				try:
					sound_rate = 1*(data[1]/data[0])-1*(pow(data[2],2)/data[0])
					text = str(sound_rate) + '\n'
					file2.write(text)
				except ZeroDivisionError:
					pass
			else:
				print("댓글 건전도2 산출 완료!")

	def analysis3(self, name):
		self.soundness.m_analysis(self.content_list)
		with open('morpheme_data.txt','r',encoding='utf-8') as file, open(f'./sound/{name}.csv', 'w',encoding='utf-8') as file2:
			total = file.readlines()
			for x in range(0, len(total)):
				data = list(map(int, total[x].rstrip('\t').rstrip('\n').split('\t')))
				try:
					sound_rate = 1/2*(data[1]/data[0])-1*(data[2]/data[0])
					text = str(sound_rate) + '\n'
					file2.write(text)
				except ZeroDivisionError:
					pass
			else:
				print("댓글 건전도3 산출 완료!")

	def analysis4(self, name):
		self.soundness.m_analysis(self.content_list)
		with open('morpheme_data.txt','r',encoding='utf-8') as file, open(f'./sound/{name}.csv', 'w',encoding='utf-8') as file2:
			total = file.readlines()
			for x in range(0, len(total)):
				data = list(map(int, total[x].rstrip('\t').rstrip('\n').split('\t')))
				try:
					sound_rate = 1/2*(data[1]/data[0])-1*(pow(data[2],2)/data[0])
					text = str(sound_rate) + '\n'
					file2.write(text)
				except ZeroDivisionError:
					pass
			else:
				print("댓글 건전도4 산출 완료!")

	def text_out_with_comment_analysis(self, name):
		with open(f'./sound/{name}.txt','w', encoding='utf-8') as file:
			for x in range(0, len(self.content_list)):
				text = str(self.content_list[x]) + '\t' + str(self.analysis_list[x]) + '\n'
				file.write(text)

	def __del__(self):
		pass