"""
def linea():
    print("2")
    print("2")
    print("2")
    print("2")
    print("2")
    print("2")


def linea2():
    linea()
    linea()
    linea()
linea2()    

linea()
"""
"""

def imprimedoble(paso):
    print (paso,paso)

imprimedoble ("a")

#primer uso de condicionales y boleanos
#comparar 2 valores y ver si son numeros a la vez
"""
"""
valor1=float(input('inserte el primer valor  :'))
valor2=float(input('inserte el segundo valor  :'))
def comparar (x,y):
    if x>y:
        print('el primer valor es mayor que el segundo')
    elif x<y:
        print ('el primer valor es menos que el segundo')
    elif x==y:
        print('los valores son iguales')
    else:
        print('no ingresaste valores validos3')    

comparar(valor1,valor2)
"""
"""
def nlinea(n):
    if n>0:
        print (n)
        nlinea(n-1)
    else:
        print("boom")
dias=int(input('inserte dias antes de la explocion'))  
nlinea(dias)

#ESCRIBIR  funcion comparar que devuelva 1 si x>y 
# 0 si x==y, -1 si x<y 
"""
""""
valor1=float(input('inserte un valor: '))
valor2= float(input('inserte un segundo valor valor: '))

def comparar(x,y):
    if x>y:
        print (1) 
        return
    elif x==y:
        print(0) 
        return
    else: 
        print(-1) 
        return
comparar(valor1,valor2)    """

#describa una funcion que diga 1 si x<=y<=z y 0 en cualquier otra situacion
"""
def estaentre(x,y,z):
        print(x<=y<=z) 

x1=1
y1=1
z1=2
estaentre(x1,y1,z1)"""

#primer uso del comando while
"""
def nlineas(n):
    while n>0:
        print(n)
        n=n-1
    return ("listo")
variable=14
nlineas(variable)"""

#secuencia de retorno string donde use \n y \t
"""
print('presente', '\n', '\t', 'esta', '\n', '\t', '\t' 'salida')
"""

#mostrar el exponente a la 16 de 2
"""
y=1
x=2
while y!=17:
    print (2,'**',y,' =',"\t", x)
    x=x*2
    y=y+1"""

#practica del comando while con una tabla de multiplicar
#defino funcion

"""
def tablamultiplicar(e,mayor):
    i=1
    while i<=mayor:
        print (e*i,'\t',end="")
        i=i+1
    print()
def tabla(valor,cantidad):
    e=1
    while e<=cantidad:
        tablamultiplicar(e,valor)
        e=e+1

tabla(5,9)"""

#primera practica del for:
"""
fruta="banana"
for teta in fruta:
    print(teta)
"""
#primera tarea con for:
"""
prefijos = "JKLMNOPQ"
sufijo = "ack"
for letra in prefijos:
    if letra=="o" or "q":
        print (letra+"u"+sufijo)
    else:   
        print (letra + sufijo)
 """

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
"""
def    encuentra(cad,c,j):
    indice=j
    while indice < len(cad): 
        if cad[indice] == c:
            return indice 
        indice=indice+1
        return-1
"""

#Como ejercicio, encapsule este c´odigo en una funci´on l lamada 
#cuentaLetras, y generalıc´ ela de forma que acepte la cadena y la 
#letra como par´ametros.

"""
fruta="banana" 
cuenta=0
for car in fruta:
    if car =="a": 
        cuenta = cuenta + 1
    print  (cuenta)"""

"""
def busqueda (palabra,letra):
    contador=0
    for recorrido in palabra:
        if recorrido ==letra: 
            contador = contador + 1
    print  (contador)

busqueda("palabra","a")"""

#Como ejercicio, escriba un bucle que recorra la lista anterior e im- 
#prima la longitud de cada elemento. ¿que´ ocurre si envıa´ un entero 
#a len?

lista=["spam!",1,["Brie","Roquefort","Pol le Veq"],[1,2,3]]
for recorrido in lista:
    print (recorrido[3])