import json

data = {"Fruteria": [  {"Fruta":   [    {"Nombre":"Manzana","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ]}

#Nos imprime en pantalla data como un tipo de dato nativo.
print ("DATA:", repr(data))

#Nos devuelve el String con el JSON
data_string = json.dumps(data)
print ('JSON:', data_string)
