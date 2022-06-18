#casting = merubah satu type data ke type yang lain
#type data = string, int, float, boolean

#Merubah INT
print("====integer====")
data_int = 9
print("data:", data_int,",bertipe: ", type(data_int))

data_float = float(data_int)#sumber data type yg ingin diubah
print("data: ", data_float,",bertipe: ", type(data_float))

data_str = str(data_int)
print("data: ", data_str,",bertipe: ", type(data_str))

data_bool = bool(data_int)#akan false jika nilai int = 0
print("data: ", data_bool,",bertipe: ", type(data_bool))

#Merubah Float
print("====float====")
data_float = 9.5
print("data:", data_float,",bertipe: ", type(data_float))

data_int = int(data_float)#sumber data type yg ingin diubah
print("data: ", data_int,",bertipe: ", type(data_int))

data_str = str(data_float)
print("data: ", data_str,",bertipe: ", type(data_str))

data_bool = bool(data_float)#akan false jika nilai float = 0
print("data: ", data_bool,",bertipe: ", type(data_bool))


#Merubah Boolean
print("====boolean====")
data_bool = True
print("data:", data_bool,",bertipe: ", type(data_bool))

data_int = int(data_bool)#sumber data type yg ingin diubah
print("data: ", data_int,",bertipe: ", type(data_int))

data_str = str(data_bool)
print("data: ", data_str,",bertipe: ", type(data_str))

data_float = float(data_bool)#akan false jika nilai float = 0
print("data: ", data_float,",bertipe: ", type(data_float))


#Merubah string
print("====string====")
data_str = "123"#jika pada type string diisi dengan char maka pada data yg lain akan error
print("data:", data_str,",bertipe: ", type(data_str))

data_int = int(data_str)#sumber data type yg ingin diubah
print("data: ", data_int,",bertipe: ", type(data_int))

data_bool = bool(data_str)
print("data: ", data_bool,",bertipe: ", type(data_bool))

data_float = float(data_str)#akan false jika nilai float = 0
print("data: ", data_float,",bertipe: ", type(data_float))