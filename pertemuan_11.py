#Pogram 11.1 Multi keys & Nesting Dictionary

import datetime

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim' :'19022001',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Azan Magrib',
    'nim' :'19022002',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama':'Slamet Dunia Akhirat',
    'nim' :'19022003',
    'sks_lulus':100,
    'beasiswa':True,
    'lahir':datetime.datetime(1977,5,10)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<6} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")


#Pogram 11.2 Latihan Dictionary Bagian 1

    import datetime

    mahasiswa_template = {
        'nama': 'nama',
        'nim' : '0000000',
        'sks_lulus' : 0,
        'lahir' : datetime.datetime (1111,1,11)
        }
data_mahasiswa = {}

print(f'{"SELAMAT DATANG" : ^20}')
print (f"{'DATA MAHASISWA'}")
print ("-"*20)

mahasiswa = dict.fromkeys (mahasiswa_template.keys())
print (mahasiswa)
mahasiswa ['nama'] = input ("nama mahasiswa: ")
mahasiswa ['nim'] = input ("nim mahasiswa")
mahasiswa ['sks_lulus'] = int (input("sks lulus"))
tahun_lahir = int(input("tahun lahir (YYYY): "))
bulan_lahir = int(input("bulan lahir (1-12): "))
tanggal_lahir = int(input("tanggal lahir (1-31): "))
mahasiswa ['lahir']
datetime.datetime (tahun_lahir,bulan_lahir,tanggal_lahir)
print (mahasiswa)


#pogram 11.3 Latihan Dictionary Bagian 2

import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '000000',
    'sks_lulus' : 0,
    'lahir':datetime.datetime (1111,1,11)
}

data_mahasiswa = {}
while True:
    os.system("cls")
    print (f"('selamat datang': ^20)")
    print(f"{'data mahasiswa': ^ 20}")
    print ("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print (mahasiswa)
mahasiswa ['nama'] = input ("nama mahasiswa: ")
mahasiswa ['nim'] = input ("nim mahasiswa: ")
mahasiswa ['sks_lulus'] = (input ("sks lulus" ))
tahun_lahir = int(input("tahun lahir (YYYY)" ))
bulan_lahir = int(input("bulan lahir(1-12): "))
tanggal_lahir = int (input("tanggal_lahir (1-31):"))
mahasiswa ['lahir'] 
datetime.datetime (tahun_lahir,bulan_lahir,tanggal_lahir)

KEY = ''.join ((random.choice(string.ascii_uppercase) for i in range (6)))
data_mahasiswa.update({KEY :mahasiswa})

print (f"\n{'key':<6} {'nama': <17} {'nim': <8} {'sks lulus': <10} {'tanggal_lahir':<10}")
print ("-"*60)

for mahasiswa in data_mahasiswa:
     key = mahasiswa
     nama = data_mahasiswa [key]['nama']
     nim = data_mahasiswa [key]['nim']
     sks = data_mahasiswa [key]['sks_lulus']
lahir = data_mahasiswa [key]['lahir'].strftime("%x")

print (f"{key: <6} {nama:<17} {nim:<8} {sks: ^10 {lahir: ^10}}")

print ("\n")
is_done = input ("mau tambah lagi brow (y/n)? ")
if is_done == "n":
    brea

print ("\nAkhir dari pogram terimakasih")