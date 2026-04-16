# 1. Pokébola → $1000
# 2. Poción → $1500
# 3. Revivir → $3000
# 4. Baya → $500
# 5. Finalizar compra
#probando fusiones
contador_productos = 0
acumulador_precio = 0
flag = True
while flag:
    print("1. Pokébola → $1000")
    print("2. Poción → $1500")
    print("3. Revivir → $3000")
    print("4. Baya → $500")
    print("5. Finalizar compra")
    try:
        opcion = int(input("ingrese opcion\n"))
        
        if opcion == 1:
            cantidad = int(input("Ingrese cantidad: "))
            
            if cantidad > 0:
                precio = 1000
                acumulador_precio = acumulador_precio + 1000
                contador_productos = contador_productos + 1
                print("has comprado pokebola")
            else:
                print("Cantidad inválida")
                
        elif opcion == 2:
            cantidad = int(input("Ingrese cantidad: "))
            
            if cantidad >0:
                precio = 1500
                acumulador_precio = acumulador_precio + 1500
                contador_productos = contador_productos + 1
                print("has comprado pocion")
            else:
                print("Cantidad inválida")
                
        elif opcion == 3:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >0:
                precio = 3000
                acumulador_precio = acumulador_precio + 3000
                contador_productos = contador_productos + 1
                print("has comprado revivir")
            else:
                print("Cantidad inválida")
                
        elif opcion == 4:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >0:
                precio = 500
                acumulador_precio = acumulador_precio + 500
                contador_productos = contador_productos + 1
                print("has comprado baya")
            else:
                print("Cantidad inválida")
                
        elif opcion == 5:
            flag = False
        else:
            print("ingrese opcion valida")
        continuar = int(input("desea seguir comprando? 1.SI   2.No\n"))
        if continuar == 2:
            flag = False
    except:
        print("opcion debe ser numerico")

cantidad_revivir = 0

    
print(f"Cantidad de productos vendidos: {contador_productos}")
print(f"Valor Bruto: ${acumulador_precio}")
print(f"")