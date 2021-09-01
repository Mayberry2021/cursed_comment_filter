# cursed_comment_filter
# 비속어 필터링 분석 시 필요한 모듈 (2021.09.01. Wend.)

 네이버 뉴스의 여섯가지 섹션(정치, 경제, 사회, 생활, 세계, IT/과학)에 존재하는 기사들의 댓글들을 크롤링하여 길이와 어조분석을 통해 악성댓글을 필터링하는 프로젝트
 프로젝트 수행을 위한 모듈들의 기능과 간단한 사용법을 소개

## Readme 순서
 1. 모듈개요
 2. 모듈 사용법
 3. 기타

## 모듈 개요

 - 모듈
    - crawler.py    		-> 네이버 뉴스 기사 댓글을 크롤링(정치, 경제, 사회, 생활, 세계, IT/과학 총 6개의 섹션 대상 크롤링)하는 모듈
    - db_controller.py	-> 크롤링 결과물들을 저장할 DB를 생성, 관리하는 모듈
    - main.py		-> 매일 자정을 기준으로 24시간 동안 자동으로 네이버 기사를 크롤링하는 모듈(24시간 이외에도 사용자가 원하는 시간 설정 가능)
    - len_analysis.py		-> DB에 저장된 섹션별 댓글들을 길이별로 나누거나 원하는 섹션별로 추출할 수 있는 모듈
    - morpheme_analysis.py  -> 어조(예사어, 비속어, 존대어) 분석을 진행하는 모듈
    - soundness_analysis.py   -> 댓글 건전도를 분석하는 모듈


## 모듈 사용법

 - 크롤링을 직접적으로 담당하는 모듈은 crawler와 db_controller이나 사용자 입장에서 편리하게 실행 가능한 코드 소개를 위해 main.py의 사용법만 소개

### main.py

 -  사용된 라이브러리 : schedule / time
 -  연관된 모듈 : crawler.py / db_controller.py
  
 
 #### 크롤링을 위한 메인 코드 작성 예

	// 
		def Auto_Crawling():
			now = time.localtime().tm_mday
			name = naming()
			db_name = '사용자가 직접 설정'
			c = Crawl_Schedule(db_name)
			c.create_table()
			c.off_clean_bot()	-> 네이버 기사 댓글의 클린봇을 자동으로 해제해주는 메소드.(클린봇을 작동시킨 채 크롤링 하고 싶다면 이 부분의 코드는 삭제하면 됨)
			while time.localtime().tm_mday == now:	-> 크롤링을 시작한 날짜가 변경되면 크롤링 중단. 만일 시간대를 바꾸고 싶다면 while 문의 탈출조건을 수정하면 됨.
				c.Act()
	//	


 #### 코드 사용 예시(매일 자정 12시 10분마다 크롤링)

	//
		 schedule.every().day.at("00:10").do(Auto_Crawling)  

	//


### len_analysis.py

 - 사용된 라이브러리 : konlpy
 - 연관된 모듈 : db_controller.py

 - 구성
	- DB 전체 댓글을 불러오는 기능(Total_Data_Analysis 클래스)과 섹션별로 댓글을 불러오는 기능(Length_Analysis 클래스) 존재


 #### DB에 저장된 모든 댓글 가져오기 

	//
		total = Total_Data_Analysis(db_name)
		total.get_criteria()	-> DB 내 댓글들의 평균길이를 기준으로 저/중/고를 설정함
		data_set = total.get_comment('all') -> 이전에 설정했던 길이를 기준으로 댓글 데이터 반환 메소드. 인자로써 'all'(모든 댓글 반환), 'low'(평균 이하값), 'mid'(중간값), 'high'(평균 이상 값)'
	//

 #### 섹션 내 댓글 가져오기

	//
		section = Length_Analysis(db_name, 'politics')    -> DB 이름과 섹션이름(politics, economy, society, life, world, it)을 인자로 받음
		section.get_criteria()
		section_data = section.section_comment()	-> 섹션 내 전체 댓글 반환
	//
	

### morpheme_analysis.py

 - 사용된 라이브러리 : konlpy

 - 구성
	- 댓글을 대상으로 어조(비속어, 존대어, 예사어)분석을 진행할 수 있음
	- 향후 댓글 건전도 측정을 위해 댓글 내 비속어, 존대어, 예사어 품사를 분석할 수 있음

 #### 비속어 분석

	//
		cursed = Cursed_Analysis('politics', section_data)	-> 분석하고자 하는 섹션의 이름과 실제 댓글 데이터들을 인자로 받음
		cursed.malword_loader()	-> 비속어 목록 불러오기
		cursed.make_cursed_list()	-> 비속어 분석
		cursed_set = cursed.get_cursed_list()	-> 비속어가 포함된 댓글(악성댓글)들을 반환
		cursed.make_out_list()	-> 인자로 받은 댓글 데이터들 중 악성 댓글이 아닌 리스트들을 생성
		out_list = cursed.get_out_list()	-> 악성 댓글이 아닌 댓글 리스트 반환
	//

 #### 존대어 분석

	//
		polite = Polite_Analysis('politics', out_list)	-> 실제 댓글 데이터(예시에서는 악성 댓글을 제외한 댓글 목록들을 인자로 주었지만 일반 댓글 목록도 인자로 줄 수 있음)
		polite.make_polite_list()
		polite_set = polite.get_polite_list()
		polite.make_out_list()	-> 인자로 받은 댓글 데이터들 중 존대어로 분석되지 않은 나머지 댓글들을 생성
		out_list2 = polite.get_out_list()	-> 존대어로 분석되지 않은 댓글 리스트 반환
	//

 #### 예사어 분석
	
	// 
		ordinary = Ordinary_Analysis("politics", out_list2)
		ordinary.text_out()		-> 예사어 댓글들을 텍스트로 출력

	//

### soundness_analysis.py

 - 사용한 라이브러리 : konlpy

 - 구성
	- 댓글을 형태소 분석하여 21개의 유효품사와 비속어를 계산하여 댓글 건전도를 포함한 다양한 데이터를 csv 파일로 출력
	
 #### 댓글 건전도 분석

	//
		analysis = Morpheme_Count()
		all_data = analysis.m_analysis(section_data)   -> 댓글들을 분석하고 결과로 나온 데이터를 리스트 형태로 반환
		analysis.soundness_analysis('csv로 저장할 파일이름', all_data) 	-> 분석 결과 데이터를 csv로 저장
	//	

## 기타

 - 코드 사용 주의점
	- 소개된 모듈을 사용할 때  'malword.txt'파일이 모듈이 위치한 경로와 같은 곳에 위치해야 함
	- malword.txt는 비속어 분석 시 사용되는 비속어 목록집
 - 기타
	- readme에 작성된 것 이외에도 기타 기능들도 존재하니 실제 코드들을 살펴보면 이해할 수 있을 것으로 생각됨.
	- 모듈에 있는 기존 코드 몇 개를 삭제하였음. 논문 실험 진행 시 추가적으로 필요한 기능이 있어 구현하였으나 일회성으로 판단되어 모두 제거하고, readme 작성 시 에는 모듈이 수행하는 기본적 기능만을 남겨놓았음. 삭제한 코드들은 dummy 폴더에 정리해놓았으니 필요 시 열람 
