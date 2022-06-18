# a = 10 adalah variabel dengan nilai 10

#tipe data : angka satuan (integer)
#string = kumpulan karakter berupa angka dan huruf
data_int = 1
print(type(data_int))
print("data:", data_int, ", bertipe : ", type(data_int))

#type data int
data_int = 8 
print("data:", data_int, ", bertipe : ", type(data_int))

#type data boolean
data_apa = True #menentukan type data dengan menggunakan (type)
print("data:", data_apa, ", bertipe: ", type(data_apa))

#type data float
data_opo = 1.5
print("data:", data_opo,", bertipe: ", type(data_opo))

#type data string
type_string = "ucup 123"
print("data:", type_string,", bertipe: ", type(type_string))

#type data khusus
#bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("-bertipe : ",type(data_complex))

#type data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data :", data_c_double)
print("-bertipe: ", type(data_c_double))