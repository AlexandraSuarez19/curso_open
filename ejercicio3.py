peso = float(input("Dígame su peso en kg: "))
estatura = float(input("Dígame su estatura en metros: "))

masa_corporal = round((peso / (estatura**2)),2)

indice = (f"Tu índice de masa corporal es {masa_corporal} donde es el índice de masa corporal calculado redondeado con dos decimales. ")

print(indice)
