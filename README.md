__팀명: 동서가구__

__조원: 이장희, 김진호, 이규승__

__주제: 홈 IOT 기반으로 삶의 편리를 높여주는 스마트 스탠드__

완성

)https://user-images.githubusercontent.com/29765855/42629844-489a7b2c-85c4-11e8-9b35-1c25c4eb5296.jpg)

내부

![20180712_123334](https://user-images.githubusercontent.com/29765855/42611198-ec5a656e-85cf-11e8-83a3-eaf96049e0cc.jpg)

__1. 사용한 장비__

라즈베리파이, 아두이노, 카메라 모듈, 16x2Lcd, NEO pixel LED 3개, 가변저항, 마이크, 잭 스피커 

![raspberrt](https://user-images.githubusercontent.com/29765855/42580089-b5863204-8564-11e8-80e3-e3d4b1562bc6.jpg)
![default](https://user-images.githubusercontent.com/29765855/42580211-009f1be8-8565-11e8-8514-8cc2877a6890.png)
![default](https://user-images.githubusercontent.com/29765855/42580303-27b97f84-8565-11e8-954d-a45ae3e0c73b.jpg)
![default](https://user-images.githubusercontent.com/29765855/42580631-f13a2ade-8565-11e8-9296-d97f184e5b77.jpg)
![default](https://user-images.githubusercontent.com/29765855/42580646-f94b15ee-8565-11e8-8f29-9ff2d4fde2b1.jpg)
![default](https://user-images.githubusercontent.com/29765855/42580658-fecdd006-8565-11e8-91eb-3e0e8bc1b647.jpg)

__2. 사용 기술__

음성인식 --> STT(Speech to text, Google API key 사용) 

음성출력 --> TTS(Text to speech, Festival 과 espeak 사용)

크롤링(무수히 많은 컴퓨터에 분산 저장되어 있는 문서를 수집하여 검색 대상의 색인으로 포함시키는 기술)

파싱(beautifulSoup4)

얼굴인식(OpenCV)

![20180712_002901](https://user-images.githubusercontent.com/29765855/42582655-b231be1a-856a-11e8-9ad1-deaa5100a9b7.jpg)

![opencv](https://user-images.githubusercontent.com/29765855/42582391-ec0349b6-8569-11e8-8fe0-163004abd48d.jpg)

__3. 실현 기능__

___(라즈베리파이)___

1. 음성인식 기반 인공지능 비서: 현재 날씨 출력,지하철 시간 출력,노래 재생,학식 메뉴 출력,녹음기능과 녹음한 음성 틀기

__날씨__: 명령어 "weather" --> 현재 닐씨와 온도를 출력. 

ex) 날씨 clouds 와 온도 21이 출력됨. 

__지하철__: 명령어 "subway" --> 현재 시간 이후에 오는 지하철 시간을 출력. 

ex) 평일 12시 16분에 실행시 26, 38, 50이 출력됨.

__노래__: 명령어 "music" --> 분위기와 장르별로 노래를 재생 시킬 수 있습니다. 

ex) 명령어 "Rock" --> 김경호의 Shout를 재생.

__학식__: 명령어 "menu" --> 오늘 학식메뉴가 출력됨. 

ex) 현재 7월 12일 생활원식당일 떄 --> 닭볶음탕, 모듬햄찌개, 간장불고기가 출력됨.

__녹음__: 명령어 "start" --> 30초 동안 녹음.

__녹음파일 재생__: 명령어 "play" --> 녹음 파일 재생.

![20180712_120723](https://user-images.githubusercontent.com/29765855/42610664-91f9be28-85cd-11e8-9680-bc58cebe7631.jpg)

![20180712_121517](https://user-images.githubusercontent.com/29765855/42610780-f950d1e2-85cd-11e8-81b2-3150dd95f241.jpg)

![20180712_122701](https://user-images.githubusercontent.com/29765855/42611028-0b2c5fe8-85cf-11e8-83bd-dc6832061d2b.jpg)

2. 영상인식 기반 스마트 알람

__스마트 알람__: 명령어 "alarm" --> 시간 설정 --> 알람 ON --> 얼굴 인식을 못하면 알람을 반복재생 --> 얼굴 인식시 일림 꺼짐.

___(아두이노)___

3. 스탠드: 가변저항으로 빛 밝기 조절.

4. 시계: 16x2 LCD로 현재 날짜와 시긴을 출력.

__4. 기대 효과__

![20180712_124412](https://user-images.githubusercontent.com/29765855/42611502-72688a7c-85d1-11e8-84ae-89362ef4a6d6.png)
