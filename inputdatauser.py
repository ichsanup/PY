#episode input user

#data yg dimasukan sudah pasti string 
data = input ("Masukan Data: ")
print("data: ", data,",type data: ", type(data))

#jika kita ingin mengambil int, maka 
data_int = int(input("Masukan angka: "))
print("data: ", data_int,",type data: ", type(data_int))

#jika kita ingin mengambil boolean, namun hasil dari running program akan menghasilkan 
#bernilai true walaupu nilainya 0 
data_boolean = bool(input("Masukan hasil: "))
print("data: ", data_boolean,",type data: ", type(data_boolean))

#jika inigin mengambil data boolean, dan memberikan hasil false maka casting dulu ke (INT)
data_boolean = bool(int(input("Masukan hasil: ")))
print("data: ", data_boolean,",type data: ", type(data_boolean))


#jika kita ingin mengambil float, maka 
data_float = float(input("Masukan angka: "))
print("data: ", data_float,",type data: ", type(data_float))