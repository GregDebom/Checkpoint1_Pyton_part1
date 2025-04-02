real = float(input("Quantos Reais tu tens? :\n"))
dolar = 0.18
Euro = 0.16
Peso_argentino = 188.76
Libra_Esterlina = 0.14
Iene = 26

#Colocar money
caldol = dolar * real
caleur = Euro * real
calpa = Peso_argentino * real
calLE = Libra_Esterlina * real
calie = Iene * real

print(f"Tu tens em dolar {caldol:.2f}")
print(f"Tu tens em euro {caleur:.2f}")
print(f"Tu tens em Peso argentino {calpa:.2f}")
print(f"Tu tens em Libra Esterlina {calLE:.2f}")
print(f"Tu tens em Iene {calie:.2f}")

