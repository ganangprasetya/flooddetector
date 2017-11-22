import cv2
import MySQLdb
from visual import * # import all the vPython library
import time
import datetime

host="localhost"
user="root"
password=""
database="dataair"
konek = MySQLdb.connect(host,user,password,database)
cur = konek.cursor()
while(1==1):
        now = datetime.datetime.now()
        hariini = str(now)
        bacacarsatu = "Select substring(TextDecoded, 1, 10) from inbox ORDER BY ReceivingDateTime DESC LIMIT 1"; #baca karakter pertama registrasi
        cur.execute(bacacarsatu)
        konek.commit()
        hasilcarsatu = cur.fetchone()
        printing = "%s" % hasilcarsatu
        hasilcar1 = str(printing)
        print hasilcar1
        if (hasilcar1 == 'REGISTRASI'):
                bacacardua = "Select substring(TextDecoded, 12, 20) from inbox ORDER BY ReceivingDateTime DESC LIMIT 1"; #baca karakter ke dua registrasi
                cur.execute(bacacardua)
                konek.commit()
                hasilcardua = cur.fetchone()
                printing = "%s" % hasilcardua
                hasilcar2 = str(printing)
                print hasilcar2
                bacano = "Select SenderNumber from inbox ORDER BY ReceivingDateTime DESC LIMIT 1"; #baca nomor terakhir registrasi
                cur.execute(bacano)
                konek.commit()
                hasilnomor = cur.fetchone()
                nomorsender = "%s" % hasilnomor
                nomor1 = str(nomorsender)
                print nomor1 
                time.sleep(1)
        else:
                bacadb = "Select TextDecoded from inbox ORDER BY ReceivingDateTime DESC LIMIT 1"; #baca sms terakhir umum
                cur.execute(bacadb)
                konek.commit()
                hasil = cur.fetchone()
                printing = "%s" % hasil
                hasil = str(printing)
                print hasil
                time.sleep(1)
                bacanomor = "Select SenderNumber from inbox ORDER BY ReceivingDateTime DESC LIMIT 1"; #baca nomor terakhir umum
                cur.execute(bacanomor)
                konek.commit()
                hasilnomor = cur.fetchone()
                nomorsender = "%s" % hasilnomor
                nomor = str(nomorsender)
                print nomor 
                time.sleep(1)
        if (hasilcar1=='REGISTRASI'):
                print "PROSES REGISTRASI...."
                simpannomor = "INSERT INTO buku_telepon (Nomor_HP, Nama) VALUES ('%s','%s')" % (nomor1,hasilcar2)
                cur.execute(simpannomor)
                konek.commit
                kirimpesan = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor1,'TERIMA KASIH SUDAH REGISTRASI KE MONITORING KETINGGIAN AIR KAMI Mr./Mrs. '+hasilcar2,'GAMMU')
                cur.execute(kirimpesan)
                konek.commit
                time.sleep(8)
                print "REGISTRASI BERHASIL", "Mr./Mrs. ",hasilcar2
                hapus="delete from inbox where substring(TextDecoded,1 , 10) = 'REGISTRASI'"
                cur.execute(hapus)
                konek.commit()
        elif (hasil=='CEK'):
                bacatinggi = "Select tinggi from ketinggian_air ORDER BY tanggal DESC LIMIT 1"; #liat ketinggian dari DB
                cur.execute(bacatinggi)
                konek.commit()
                tinggi = cur.fetchone()
                printing = "%s" % tinggi
                hasil1 = str(printing)
                bacastatus = "Select keterangan from ketinggian_air ORDER BY tanggal DESC LIMIT 1"; #liat keterangan dari DB
                cur.execute(bacastatus)
                konek.commit()
                status = cur.fetchone()
                printing = "%s" % status
                hasil2 = str(printing)
                kirimpesan = "INSERT INTO outbox (DestinationNumber, TextDecoded, CreatorID) values ('%s','%s','%s')" % (nomor,'Ketinggian Air : '+hasil1+' cm, Status : '+hasil2,'GAMMU')
                cur.execute(kirimpesan)
                konek.commit()
                print "PENGECEKAN BERHASIL"
                hapus="delete from inbox where (TextDecoded) = 'CEK'"
                cur.execute(hapus)
                konek.commit()
        else :
                hapuspesan="delete from inbox where (TextDecoded) = ('%s') " % (hasil) #PERINTAH SELAIN SMS DI ATAS DIHAPUS
                cur.execute(hapuspesan)
                konek.commit()
