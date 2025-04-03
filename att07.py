litros=float(input("Quantos litros foram abastecidos?"))
tipo=input(" Digite E para etanol e G para gasolina ?")
G=5.80
E=4.90

if tipo == "G" or  tipo == "g":
    valor= litros * G
else:
    if tipo == "E" or tipo == "e":
        valor= litros * E
print(f"voce gastou RS{valor:.2f}")