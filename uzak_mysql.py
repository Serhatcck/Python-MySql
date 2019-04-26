import MySQLdb

host_adresi= "www.net"
sifre="sfr"
veri_tabanı_uzerindeki_kullanıcı="kullanıcı"
veri_tabanı="db"

deneme = MySQLdb.connect(host_adresi,sifre,veri_tabanı_uzerindeki_kullanıcı, veri_tabanı)
if(deneme):
    print("Basarili")

else:
    print("basarisiz")

cursor = deneme.cursor()

"""sql = "SELECT * FROM bilgiler"
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      ep = row[2]
      no = row[3]
      print("First name : {} , Last name : {} , E_posta : {} , No :{}".format(fname,lname,ep,no))
except:
   print("Error: unable to fecth data")
"""


deneme.commit()
deneme.close()
