import os
os.system("cls")


productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


marcas_cantidad = {'HP': [31],
                   'LENOVO': [43],
                   'ASUS': [3],
                   'DELL': [1],
                   }


stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}


def stock_marca():
    
    marca = input("ingrese marca a consultar: ").upper()

    if marca in marcas_cantidad:
        print(f"el stock es de: {marcas_cantidad[marca]}")
    else:
        print("ingrese una de las marcas")


def busqueda_precio(p_min,p_max):
    
    p_min = int(input("ingrese un precio minimo: "))
    p_max = int(input("ingrese un precio maximo: "))

    if p_min > 240000 and p_max >= 749990:
        print(productos)



def menu():
    while True:

        print("---MENU DE PYBOOKS---")
        print("1. STOCK MARCA")
        print("2. BUSQUEDA POR PRECIO")
        print("3. ACTUALIZAR PRECIO")
        print("4. SALIR")

        opcion = (input("ingrese una opcione: "))

        if opcion == "1":
            stock_marca()
        elif opcion == "2":
            busqueda_precio()
        elif opcion == "3":
            print("3")
        elif opcion == "4":
            print("programa terminado..")
            break



menu()