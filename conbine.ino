/*
 LCD 연결해서 글자 출력하기
 
 이 스케치는 KocoaFab에서 만들었습니다.
 이 스케치는 누구든 무료로 사용할 수 있습니다.
*/

#include <LiquidCrystal.h>
#include <core_build_options.h>
#include <swRTC.h>
#include <Adafruit_NeoPixel.h>

#define PIN 3
#define PIN2 7
#define PIN3 8
#define LIGHT_PIN 1
#define BRIGHT 64
Adafruit_NeoPixel px = Adafruit_NeoPixel(4, PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel px2 = Adafruit_NeoPixel(4, PIN2, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel px3 = Adafruit_NeoPixel(4, PIN3, NEO_GRB + NEO_KHZ800);
int brightness = 0;
LiquidCrystal lcd(12,11,5,4,3,2);        //RS 핀, E핀, 데이터 핀 4개
String lcdString = "";                   //객체 선언 : 출력 할 글자 저장

swRTC rtc; 

int piezo = 2;
int switchPin = 9;
int temp;

//AM PM을 구분해 주는 함수
void Set_AMPM(int hour) {
  if(hour >=12) 
    lcd.print("PM");
  else 
    lcd.print("AM");

  lcd.print(hour%12, DEC);     //시간 출력
}

//10보다 작은수를 출력할때 앞에 0을 출력하게 하는 함수
void Set_lowThanTen(int time) {
  if(time < 10) {
    lcd.print("0");
    lcd.print(time%10);
  }
  else
    lcd.print(time);
}

//유효한 알람시간인지 체크하는 함수
int checkTheAlarmClock(int time) {
  if(time/100 < 24 && time %100 < 60) {
    Serial.println("Success");
    return time;
  }
  else {
    Serial.println("Failed");
    return 0;
  }  
}

//알람이 울릴시간인지 체크하는 함수
void checkTheAlarmTime(int alarmHour, int alarmMinute) {
  if(alarmHour == rtc.getHours() && alarmMinute == rtc.getMinutes()) {
        digitalWrite(piezo, 1);
        Serial.println("buzzzzzzz");
        tone(piezo, 500);
    }
}

void setup() {                   
  lcd.begin(16,2);         //LCD 크기 지정, 2줄 16칸
  lcd.clear();             //화면 초기화
  
  rtc.stopRTC();           //정지
  rtc.setTime(14,05,55);    //시간, 분, 초 초기화
  rtc.setDate(24, 8, 2014);  //일, 월, 년 초기화 
  rtc.startRTC();          //시작
  
  pinMode(piezo, OUTPUT);
  pinMode(switchPin, INPUT_PULLUP); 
  Serial.begin(9600);      //시리얼 포트 초기화 
  Serial.begin(9600);                    //시리얼 통신 초기화
  pinMode(LIGHT_PIN, INPUT);
  px.begin();
  px.show();
  px2.begin();
  px2.show();
  px3.begin();
  px3.show();
}

void turnOn(int on, int off) { 
  for (int i = 0; i < on; i++)
    px.setPixelColor(i, BRIGHT, BRIGHT, BRIGHT);
  for (int i = on; i < off; i++)
    px.setPixelColor(i, 0, 0, 0);
}

void turnOn2(int on, int off) {
  for (int i = 0; i < on; i++)
    px2.setPixelColor(i, BRIGHT, BRIGHT, BRIGHT);
  for (int i = on; i < off; i++)
    px2.setPixelColor(i, 0, 0, 0);
}

void turnOn3(int on, int off) {
  for (int i = 0; i < on; i++)
    px3.setPixelColor(i, BRIGHT, BRIGHT, BRIGHT);
  for (int i = on; i < off; i++)
    px3.setPixelColor(i, 0, 0, 0);
}

void loop() {
  brightness = analogRead(LIGHT_PIN);
  if (brightness <= 79)
      turnOn(0, 4);
  else if (brightness > 80 && brightness <= 159) {
      turnOn(1, 4);
      turnOn2(0, 4); 
  } else if (brightness > 160 && brightness <= 239) {
      turnOn(2, 4);
      turnOn2(0, 4); 
  } else if (brightness > 240 && brightness <= 319) {
      turnOn(3, 4);
      turnOn2(0, 4); 
  } else if (brightness > 320 && brightness <= 399) {
      turnOn(4, 4);
      turnOn2(0, 4); 
  } else if (brightness > 400 && brightness <= 479) {
      turnOn2(1, 4);
  }else if (brightness > 480 && brightness <= 559) {
      turnOn2(2, 4);
  } else if (brightness > 560 && brightness <= 639) {
      turnOn2(3, 4);
  }else if (brightness > 640 && brightness <= 719) {
      turnOn2(4, 4); 
      turnOn3(0, 4); 
  } else if (brightness > 720 && brightness <= 799) {
      turnOn3(1, 4);
  }else if (brightness > 800 && brightness <= 879) {
      turnOn3(2, 4);
  }else if (brightness > 880 && brightness <= 959) {
      turnOn3(3, 4);
  }else if (brightness > 960) {
      turnOn3(4, 4); 
  }else {}
  delay(275);
  px.show();
  px2.show();
  px3.show();
  int day;
  lcd.setCursor(0,1);                    //커서를 0,0에 지정 
  
  //1초 단위로 갱신하며 현재시간을 LCD에 출력
  Set_AMPM(rtc.getHours()); 
  lcd.print(":");
  Set_lowThanTen(rtc.getMinutes());
  lcd.print(":");
  Set_lowThanTen(rtc.getSeconds());
  //날짜를 LCD에 출력
  lcd.setCursor(0,0);
  Set_lowThanTen(rtc.getYear());
  lcd.print(".");
  //lcd.print("[");
  Set_lowThanTen(rtc.getMonth());
  lcd.print(".");
  Set_lowThanTen(rtc.getDay());
  //lcd.print("]");
  //세팅된 알람시간을 LCD에 출력
 // lcd.setCursor(0,1);
  //lcd.print("Alarm ");
  //Set_AMPM(temp/100);
  //lcd.print(":");
  //Set_lowThanTen(temp%100); 
  
  //1초마다 LCD갱신
  lcdString = "";                      //문자열 초기화
  lcd.print("               ");        //전 글씨 삭제
  delay(1000);
  
  //알람이 울릴 시간인지 체크
  //checkTheAlarmTime(temp/100, temp%100);

  //스위치버튼이 눌렸을 경우 피에조센서의 소리를 0으로 하고 알람시간을 초기화 한다 
  if(!digitalRead(switchPin)) {
    temp = 0;
    day = 0;
    digitalWrite(piezo, 0);
    Serial.println("Alarm clock initialize");
    Serial.println("AM0:00");
    noTone(piezo);
  }
  //시리얼 통신을 통해 알람시간을 입력받고 시리얼 모니터에 출력 
  char theDay[4];
  int i = 0;
  if(Serial.available()) {
    while(Serial.available()) {
      theDay[i] = Serial.read();
      i++;
  }
    day = atoi(theDay);
    if(day/100 >= 12) {
      Serial.print("PM");
      Serial.print((day/100)-12);
    }
    else {
      Serial.print("AM");
      Serial.print(day/100);
    }
    Serial.print(":");
    if(day%100 < 10)
      Serial.print("0");
    Serial.println(day%100);
    temp = checkTheAlarmClock(day);
  }
}
