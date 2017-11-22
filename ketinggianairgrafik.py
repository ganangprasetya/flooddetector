import time
import datetime
import MySQLdb
import serial #import the serial library
from visual import * # import all the vPython library
import numpy #import numpy
import matplotlib.pyplot as plt #import matplotlib
from drawnow import *

host="localhost"
user="root"
password=""
database="dataair"
konek = MySQLdb.connect(host,user,password,database)
cur = konek.cursor()

tinggi= []
arduinodata = serial.Serial('com13', 9600)
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
def makeFig(): #Create a function that makes our desires plot
    plt.ylim(-30,30)
    plt.title('Grafik Ketinggian Air Realtime')
    plt.grid(True)
    plt.ylabel('Ketinggian Air')
    plt.plot(tinggi, 'ro', label='cm')
    plt.plot(tinggi, 'b-')
    plt.legend(loc='upper left')

while True: #while loop that loops forever
    while (arduinodata.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinodata.readline()
    dataArray = arduinoString.split(',')
    ketinggian = int(dataArray[0])
    tinggi.append(ketinggian)
    now = datetime.datetime.now()
    hariini = str(now)
    plt.hold(True)
    drawnow(makeFig)
    plt.pause(.00001)
    cnt=cnt+1
    if (cnt>50):
        tinggi.pop(0)
    if (ketinggian >= 29):
        datasiaga1 = "INSERT INTO ketinggian_air (tanggal, tinggi, keterangan) VALUES ('%s','%d','%s')" % (hariini, ketinggian,'SIAGA I')
        cur.execute(datasiaga1)
        konek.commit()
        print hariini, ketinggian, ("SIAGA I")
    elif (ketinggian >= 25):
        datasiaga1 = "INSERT INTO ketinggian_air (tanggal, tinggi, keterangan) VALUES ('%s','%d','%s')" % (hariini, ketinggian,'SIAGA II')
        cur.execute(datasiaga1)
        konek.commit()
        print hariini, ketinggian, ("SIAGA II")
    elif (ketinggian >= 22):
        datasiaga1 = "INSERT INTO ketinggian_air (tanggal, tinggi, keterangan) VALUES ('%s','%d','%s')" % (hariini, ketinggian,'SIAGA III')
        cur.execute(datasiaga1)
        konek.commit()
        print hariini, ketinggian, ("SIAGA III")
    elif (ketinggian >= 0):
        datasiaga1 = "INSERT INTO ketinggian_air (tanggal, tinggi, keterangan) VALUES ('%s','%d','%s')" % (hariini, ketinggian,'NORMAL')
        cur.execute(datasiaga1)
        konek.commit()
        print hariini, ketinggian, ("NORMAL")
    else:
        datasiaga1 = "INSERT INTO ketinggian_air (tanggal, tinggi, keterangan) VALUES ('%s','%d','%s')" % (hariini, ketinggian,'SURUT')
        cur.execute(datasiaga1)
        konek.commit()
        print hariini, ketinggian, ("SURUT")
        
    
    
