import datetime
#import datetime, time

now = datetime.datetime.now()
now_time = now.time()
#print now_time.time().strftime('%H:%M:%S')

def isNowInTimePeriod(startTime, endTime, nowTime):
    startTime = startTime.time()
    endTime = endTime.time()

    print startTime
    print endTime
    print nowTime

    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime


print isNowInTimePeriod(datetime.datetime.strptime("20:00",'%H:%M'),datetime.datetime.strptime("23:50",'%H:%M'),now_time)




2016-06-08/20/16 02:06:43
Outside Temperature: 74.948
Inside Temperature: 82.00
Night time mode.


2016-07-08/20/16 02:07:43
Outside Temperature: 74.948
Inside Temperature: 82.45
Night time mode.


Traceback (most recent call last):
  File "main.py", line 251, in <module>
    main()
  File "main.py", line 190, in main
    officeSensor.outsideTemp = getWeather()
  File "main.py", line 104, in getWeather
    kelvin = data['main']['temp']
KeyError: 'main'ap
