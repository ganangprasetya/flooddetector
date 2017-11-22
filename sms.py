import MySQLdb
from visual import * # import all the vPython library
import time
import datetime

host="localhost" #
user="root"
password=""
database="dataair"
konek = MySQLdb.connect(host,user,password,database)
cur = konek.cursor()

while (1==1):
    bacatinggi = "Select tinggi from ketinggian_air ORDER BY tanggal DESC LIMIT 1"; #liat ketinggian dari DB
    cur.execute(bacatinggi)
    konek.commit()
    hasil = cur.fetchone()
    printing = "%s" % hasil
    hasil = int(printing)
    print hasil #print hasilnya
    time.sleep(0.5)
    bacacarsatu = "Select substring(TextDecoded, 18, 2) from outbox ORDER BY SendingDateTime DESC LIMIT 1"; #pembanding ketinggian di sms dan real time
    cur.execute(bacacarsatu)
    konek.commit()
    hasilcarsatu = cur.fetchone()
    printing = "%s" % hasilcarsatu
    hasilcar1 = str(printing)
    time.sleep(0.5)
    bacacardua = "Select Status from sentitems ORDER BY SendingDateTime DESC LIMIT 1"; #pembanding ketinggian di sms dan real time
    cur.execute(bacacardua)
    konek.commit()
    hasilcardua = cur.fetchone()
    printing2 = "%s" % hasilcardua
    hasilcar2 = str(printing2)
    time.sleep(0.5)
    bacanohp = "Select * from buku_telepon"; #liat nomor hp
    cur.execute(bacanohp)
    hasil1 = cur.fetchall()
    for row in hasil1:
        no_hp = '%s' %(row[1])
        nomor = str(no_hp) #KIRIM BROADCAST
        if (hasilcar1 == '29'): #KIRIM PESAN BANJIR
            if (hasilcar2 == 'SendingOKNoReport'):
                print "SIAGA I"
                time.sleep(1)
                break
        elif (hasil == 29):
            while True:
                kirimpesan1 = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor,'Ketinggian Air : %s' % hasil+' cm, Status SIAGA I','GAMMU')
                cur.execute(kirimpesan1)
                konek.commit
                print "BERHASIL MENGIRIM KE ", nomor
                time.sleep(1)
                break
        elif(hasilcar1 == '25'): #KIRIM PESAN BANJIR
            if (hasilcar2 == 'SendingOKNoReport'):
                print "SIAGA II"
                time.sleep(1)
                break
        elif (hasil == 25):
            while True:
                kirimpesan2 = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor,'Ketinggian Air : %s' % hasil+' cm, Status SIAGA II','GAMMU')
                cur.execute(kirimpesan2)
                konek.commit
                print "BERHASIL MENGIRIM KE ", nomor
                time.sleep(1)
                break
        elif(hasilcar1 == '22'): #KIRIM PESAN BANJIR
            if (hasilcar2 == 'SendingOKNoReport'):
                print "SIAGA III"
                time.sleep(1)
                break
        elif (hasil == 21):
            while True:
                kirimpesan3 = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor,'Ketinggian Air : %s' % hasil+' cm, Status SIAGA III','GAMMU')
                cur.execute(kirimpesan3)
                konek.commit
                print "BERHASIL MENGIRIM KE ", nomor
                time.sleep(1)
                break
        elif(hasilcar1 == '-2'): #KIRIM PESAN BANJIR
            if (hasilcar2 == 'SendingOKNoReport'):
                print "SURUT"
                time.sleep(1)
                break
        elif (hasil == -2):
            while True:
                kirimpesan = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor,'Ketinggian Air : %s' % hasil+' cm, Status SURUT','GAMMU')
                cur.execute(kirimpesan)
                konek.commit
                print "BERHASIL MENGIRIM KE ", nomor
                time.sleep(1)
                break
