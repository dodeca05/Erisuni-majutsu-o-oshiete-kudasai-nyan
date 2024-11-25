# Erisuni-majutsu-o-oshiete-kudasai-nyan

본 repository에서는 저작권 관련된 데이터 및 파일을 공유하지 않습니다.

# 음성인식 (optional)
- open ai whisper
# ai 제작
## 데이터 준비
### 캐릭터 정보
주로 나무위키에서 가져온다.
### 대사나 주요 성격
텍스트 본을 구해서 에리스 부분만 파싱한다.

# 음성 출력
- XTTS
  - fine tuning 필요
  - 대사를 ultimate vocal remover로 추출
 

----

# 참고 자료

https://www.ncloud-forums.com/topic/382/

https://velog.io/@injokim/%EC%BA%90%EB%A6%AD%ED%84%B0%EC%9D%98-%ED%8E%98%EB%A5%B4%EC%86%8C%EB%82%98%EB%A5%BC-%EB%8B%B4%EC%9D%80-%EC%B1%97%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0

https://youtu.be/oB8C4FcZDD0?si=ISAiTrXhtGT4xncS

# TODO List

- [X] 일본어 웹 소설 크롤링
- [ ] 에리스 대사만 따로 분리
- [ ] 크롤링한 데이터 중 에리스 나온 부분만 RAG 제작
- [ ] 프롬프트 작성
  - [ ] 말 투 구현
  - [ ] 일반적인 지식에 대한 답하지 않기
- [ ] 챗봇 구성
  - [ ] RAG 연결
  - [ ] (optional) 추가 학습 
- [ ] 애니속 에리스 대사 음성만 추출
