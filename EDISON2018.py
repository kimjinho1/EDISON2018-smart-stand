import os
import sys
import time
import requests
import re
from bs4 import BeautifulSoup
from pyowm import OWM
API_key = 'b19cc0c64f569ba9eefd6b3e9ff1b2eb'
train_time_week_12 = [07, 14, 26, 38, 50]
train_time_weekend_7 = [17, 29, 41, 53, 59]
train_time_week_11 = [01, 12, 23, 34, 45, 56]
train_time_weekend_11 = [05, 17, 29, 41, 53]
bus_time = [00, 10, 20, 30, 40, 50]
length_bus = len(bus_time)
length_week_12 = len(train_time_week_12)
length_weekend_7 = len(train_time_weekend_7)
length_week_11 = len(train_time_week_11)
length_weekend_11 = len(train_time_weekend_11)

while True:
    brk = 0
    print('Good morning master')
    os.system('echo "' + 'Good  \t   morning \t       master' + '" | festival --tts')
    os.system('bash record.sh 2')
    os.system('python transcribe.py test.wav>janghee.txt')
    with open('janghee.txt', 'r')as myfile:
        message=myfile.read()
    print(message)
    if message ==(' hi\n'):
        print("start")
        os.system('echo "' + 'hi \t what can \t i \t do?' + '" | festival --tts')
        while True:#functions
            os.system('bash record.sh 3')
            os.system('python transcribe.py test.wav>janghee.txt')
            with open('janghee.txt', 'r')as myfile:
                message=myfile.read()
                print(message)

            if message == (' alarm\n'):#alarm
                print("What time do you want?")
                os.system('echo "' + ' What    time    do     you   want? ' + '" | festival --tts')
                os.system('bash record.sh 3')
                os.system('python transcribe.py test.wav>time4.txt')
                with open('time4.txt', 'r')as myfile:
                    message=myfile.read()
                print(message)
                key = 0
                print('Really?')
                os.system('echo "' +'do you want'+  message + ' ?? ' + '" | festival --tts')
                os.system('bash record.sh 3')
                os.system('python transcribe.py test.wav>yesorno.txt')
                with open('yesorno.txt', 'r')as myfile:
                    yesorno=myfile.read()

                if yesorno != ' yes\n':
                    print("no")

                if yesorno == ' yes\n':
                    print ("yes")
                    print ("alarm mode")
                    while True:
                        os.system("python time.py>time.txt")
                        with open('time.txt', 'r') as myfile:
                            time = myfile.read()
                        hour = time[11:13]
                        minute = time[14:16]
                        day = time[0:3]
                        time4 = ' ' + hour + minute
                        realtime = time4 + '\n'
                        if realtime == message:
                            print ("alarm on")
                            while True:
                                os.system('omxplayer -o local alarmtest.mp3')
                                os.system('python 3.py>1.txt')
                                with open('1.txt', 'r')as myfile:
                                    face=myfile.read()
                                jjjj = face[0:2]

                                if jjjj == 'ye':
                                    print("Good morning")
                                    key = 1
                                    break
                        if key == 1:
                            break

            if message ==(' weather\n'):#weather
                owm = OWM(API_key)
                obs=owm.weather_at_id(1843564)
                w=obs.get_weather()
                os.system('python wea.py>janghee.txt')
                with open('janghee.txt', 'r')as myfile:
                    message=myfile.read()
                print(message[3:10] + ' ' + message[9:13])
                os.system('echo "' + message[3:10] + '\n    and     \n ' +  message[9:13] + '' + '" | festival --tts')
            elif message ==(' bus\n'):#bus
                os.system("python time.py>time.txt")
                with open('time.txt', 'r') as myfile:
                    time = myfile.read()
                hour = time[11:13]
                minute = time[14:16]
                day = time[0:3]
                os.system('echo "' + '  wait   please  ' + '" | festival --tts')
                for i in range(0, length_bus):
                    if int(minute) < int(bus_time[i]):
                        print(bus_time[i])
                        t_time = str(bus_time[i])
                        os.system('echo "' + t_time + '" | festival --tts')

            elif message ==(' Subway\n'):#train
                os.system("python time.py>time.txt")
                with open('time.txt', 'r') as myfile:
                    time = myfile.read()
                hour = time[11:13]
                minute = time[14:16]
                day = time[0:3]
                os.system('echo "' + 'wait,  please' + '" | festival --tts')
                if (day == 'Sun' or day == 'Sat'):
                    if hour == '09':
                        for i in range (0, length_weekend_7):
                            if int(minute) < int(train_time_weekend_7[i]):
                                print (train_time_weekend_7[i])
                                t_time = str(train_time_weekend_7[i])
                                os.system('echo "' + t_time + '" | festival --tts')

                    if hour == '11':
                        for i in range (0, length_weekend_11):
                            if int(minute) < int(train_time_weekend_11[i]):
                                print (train_time_weekend_11[i])
                                t_time = str(train_time_weekend_11[i])
                                os.system(' echo \t "' + t_time + '" | festival --tts')
                else:
                    if hour == '12':
                        for i in range (0, length_week_7):
                            if int(minute) < int(train_time_week_7[i]):
                                print (train_time_week_7[i])
                                t_time = str(train_time_week_7[i])
                                os.system('echo "' + t_time + '" | festival --tts')

            elif message ==(' music\n'):#music
                print('what kinds of music do you want?')
                os.system('echo "' + 'okay what kinds of music?' + '" | festival --tts')
                for i in range(0,2):
                    os.system('bash record.sh 2')
                    os.system('python transcribe.py test.wav>janghee.txt')
                    with open('janghee.txt', 'r')as myfile:
                        message=myfile.read()
                        print(message)
                    if message ==(' music\n'):
                        print("turn on music")
                        os.system('omxplayer -o local music.wav')
                    if message ==(' Rock\n'):
                        print("turn on rock music")
                        os.system('omxplayer -o local Rock.mp3')
                    if message ==(' fun\n'):
                        print("turn on fun music")
                        os.system('omxplayer -o local peace_tttt.mp3')
                    if message ==(' love\n'):
                        print("turn on ballade music")
                        os.system('omxplayer -o local ballade.wav')
                    if message ==(' Hip Hop\n'):
                        print("turn on hip hop music")
                        os.system('omxplayer -o local hiphop_sicha.mp3')
            elif message ==(' menu\n'):#train!
                print("wait please")
                os.system('echo "' + 'wait \n please' + '" | festival --tts')
                os.system('python3 MENU.py')
  
            elif message ==(' start\n'):
                os.system('echo "' + 'okay   record  start!!' + '" | festival --tts')
                os.system('arecord -D hw:1,0 -f S16_LE --duration=20 -r 44100 record.wav')
                os.system('echo "' + 'okay   thank  you!!' + '" | festival --tts')
            elif message ==(' play\n'):
                os.system('echo "' + '   wait    please!!  ' + '" | festival --tts')
                os.system('aplay record.wav')
            elif message ==(' sleep\n'):
                print("Goodbye")
                os.system('echo "' + ' Good    bye  ' + '" | festival --tts')
                brk = 1
                break
    if brk == 1:
        break
