import time
start_time = time.time()
print('hello world') 
#merupakan bentuk comment yg tidak akan dieksekusi pada python

#atau comment ygn tidak akan dieksekusi dengan menggunakan kutip 3 atau multiple comment
"""haii semuanya apa kabar"""
print("hello semua")
a = 10
print(a)
#atas merupakan source code
#kita bisa mengcompile python ke dalam bytecode yg berfungsi sebagai mempercepat program dieksekusi
#dengan cara masuk ke terminal ketikan python -m py_compile 'nama file'
#untuk menampilkan hasil melalui terminal dapat mengetikan (python namafile.py)
#ls berfungsi untuk melihat data file yg ada pada directory tersebut

print(time.time() - start_time, 'detik')