"""print ('hola mundo')"""

"""
print(2+3)
print("2"+"3")
"""
"""print((2*3)+5)
print (2*(3+5))"""
"""
print ("hola"*3)
print(3*"hola")
"""

#soliciten nombre y edad, y muestre el mensaje que muestre la edad y nombre
"""
nombre=str (input("ingrese su nombre"))
edad=int (input ('ingrese su edad'))
print ("bienvenido ",nombre, 'tienes ',edad )"""

#pedir que se ingrese notas e imprimir el promedio

#solicita las 3 notas
"""
calificacion1=float (input('ingresar primera calificacion'))
calificacion2=float (input('ingresar segunda calificacion'))
calificacion3=float (input('ingresar tercera calificacion'))
#calculo del promedio de notas
calificacion_total=(calificacion1+calificacion2+calificacion3)/3
#mostrar nota total
print(calificacion_total)
"""

#calcular area de un triangulo}
#pedir datos del triangulo 
"""
base=float(input('ingrese base de su triangulo: '))
altura=float(input('ingrese la altural de su triangulo: '))

area=(base*altura)/2

print('el area de su triangulo es ',area)"""

#pedir diametro de un circulo y calcular su area y perimetro

#pedimos datos del circulo

"""
diametro=float(input('ingrese diametro del circulo'))
pi=3.14
radio=diametro/2

print('el perimetro de la circunferencia es: ',(diametro*pi))
print('el area de la circunferencia es: ',(radio*pi))"""

#Ejercicio 3: Diseña un programa que, a partir del valor del lado de un cuadrado
#(3 metros), muestre el valor de su perímetro (en metros) 
# y el de su área (en metros cuadrados). 
# (El perímetro debe darte 12 metros y el área 9 metros cuadrados.)
#PERIMETRO ES LX4, PARA EL ÁREA ES LADO AL CUADRADO.

#Definir variable
"""
ladoC=3
perimetroC=ladoC*4
areaC=ladoC*ladoC
#mostrar a usuario
print('el perimetro del cuadrado es ',perimetroC,'el area es ',areaC)
"""

#hacer un programa que inicialice una tupla con
#los colores calidos luego ingrese un color
#y diga si es calido o no
"""
coloresC=("rojo","amarillo","naranja")
color=input('ingrese un color :')
colores=coloresC[:]
print(color.lower() in colores)
"""
#practicando condicional 
"""
if color in colores:
    print("ingreso un color calido :")
else:
    
     print ("no ingreso un color calido")"""

#escriba un programa para un instituto de enseñansa
#que inicie con una tupla con los cursos que se dictan
#el semestre: cocina, electricidad, gasista y plomeria
#luego ingrese datos de una personas(nombre y apellido)
#y curso que desea realizar, el programa debera imprimir
#el nombre de la persona y si puede cursar 
# o no este semestre

#defino variables
"""
materias=('cocina','electricidad','gasista','plomeria')
nombre=input('ingrese su nombre : ') 
apellido=input('ingrese su apellido : ')
materia=input('que materia le gustaria cursar : ')

#comparo materia y veo si esta disponible

print('hola! ',nombre,apellido," la materia que elegiste esta",materia.lower() in materias)"""

#escriba una lista para una empresa de transporte
#que actualice la lista segun los destinos donde llega
#iniciarla con:bariloche,chilecito,rosario,salta,tilcara.pumamarca
#luego ingrese un lugar y agregarlo a la lista al finalizar
#imprima la lista completa

#creo la lista e ingreso variable
"""
lugares=["bariloche","chilecito","rosario","salta,","tilcara","pumamarca"]
lugar_nuevo=input('ingrese nuevo lugar de destino : ')
#agrego el nuevo lugar a la lista
lugares.append(lugar_nuevo.lower())
#muestro al usuario
print(lugares)
"""

#CREAR UNA LISTA  de 5 productos, agregar 3 productos
#nuevos e imprimir una lista nueva
"""
#defino lista 
productos=["leche","queso","agua","arroz","cafe"]
#pido productos nuevos al usuario
producto_nuevo="carne"
producto_nuevo2="pollo"
producto_nuevo3="huevo"
#agrego a la lista
productos.append(producto_nuevo)
productos.append(producto_nuevo2)
productos.append(producto_nuevo3)
#muestro al usuario
print(productos)"""

#definir variable
#una variable es un contenedor de informacion, existen distintos tipos de variables
#segun la informacion que almacena como puede ser string, boleano, float y int.

#que es un dato
#un dato es la unidad minima de dentro de un programa, suelen almacenarce en variables. 
#un conjunto de datos organizados es lo necesario para crear un programa 

#explique con sus palabras que es listas y tuplas
#las listas y tuplas son informacion agrupada en una variable (datos o variables por ejemplo)
#con la diferencia de que las tuplas son inalterables, al ser creadas no pueden ser modificadas
#y las listas pueden ser modificadas de diversas formas(como agregar y sacar datos de la lista)

#4- Que error hay en el siguiente código sabiendo que vamos a crear una tupla con nombres de personas

#nombres=[jose,martin, robertro, damian]
#Print("nombres")

#""" las tuplas van en parentesis, corchetes son listas"""

#5-Resolver los siguientes codigos:
#realizar la suma de 2 números (2+3) en variables diferentes y mostrar por ptalla

#definir variables
"""
valor1=2
valor2=3
#mostrar suma en pantalla
print(valor1+valor2)"""

#6- solicitar nombre y edad, e imprimir por pantalla tu nombre es xxx y tu es xx anios
#pedir al usuario sus datos
"""
nombre=str(input('ingrese su nombre : '))
edad=int(input('ingrese su edad : '))
print('su nombre es: ',nombre,  '\nsu edad es : ',edad)
"""
#7- Pedir base y altura de un triángulo y mostrar el área del mismo #(base*altura)/2
"""
#pedir datos del triangulo al usuario
base=float(input('ingrese base del triangulo : '))
altura=float(input('ingrese altural del triangulo : '))
#calcular area
area=(base*altura)/2
#mostrar area al usuario
print('el area del triangulo es ',area)"""

#8- Pedir datos de 7 productos comprados, solicitar al usuario también la cantidad 
# y el precio unitario y debemos mostrar cuánto gasta por articulo y en general
"""
#definir productos 
producto=input('ingrese nombre del producto 1 ')
producto1=input('ingrese nombre del producto 2 ')
producto2=input('ingrese nombre del producto 3 ')
producto3=input('ingrese nombre del producto 4 ')
producto4=input('ingrese nombre del producto 5 ')
producto5=input('ingrese nombre del producto 6 ')
producto6=input('ingrese nombre del producto 7 ')
#definir cantidad de de productos
cantidad=int(input('ingrese cantidad del producto 1 '))
cantidad1=int(input('ingrese cantidad del producto 2 '))
cantidad2=int(input('ingrese cantidad del producto 3 '))
cantidad3=int(input('ingrese cantidad del producto 4 '))
cantidad4=int(input('ingrese cantidad del producto 5 '))
cantidad5=int(input('ingrese cantidad del producto 6 '))
cantidad6=int(input('ingrese cantidad del producto 7 '))
#preguntas precio unitario
precio=float(input('ingrese precio del producto 1 '))
precio1=float(input('ingrese precio del producto 2 '))
precio2=float(input('ingrese precio del producto 3 '))
precio3=float(input('ingrese precio del producto 4 '))
precio4=float(input('ingrese precio del producto 5 '))
precio5=float(input('ingrese precio del producto 6 '))
precio6=float(input('ingrese precio del producto 7 '))
#precio de cada unidad
costo=float(cantidad*precio)
costo1=float(cantidad1*precio1)
costo2=float(cantidad2*precio2)
costo3=float(cantidad3*precio3)
costo4=float(cantidad4*precio4)
costo5=float(cantidad5*precio5)
costo6=float(cantidad6*precio6)
total=(costo+costo1+costo2+costo3+costo4+costo5+costo6)
#mostrar al usuario costo individual del producto y total
print('el costo de cada producto es \n ',producto,"\t" ,costo,'\n',producto1,"\t" ,'\n\t ',costo1,'\n',producto2,"\t" ,'\n\t',costo2,'\n',producto3,"\t" ,'\n\t',costo3,'\n',producto4,"\t" ,'\n\t',
costo4,'\n',producto5,"\t" ,'\n\t',costo5,'\n',producto6,"\t" ,'\n\t',costo6,'\n y su total a pagar es: ',total)
"""

#9- Hacer un programa con variantes en 2 print donde muestre a un profesor el promedio de 5 notas de sus alumnos 1 variante será con nota decimal 
# y la otra con nota redondeada.
"""
#pedir notas del alumno al profesor
nota=float(input('ingrese valor de nota 1 '))
nota1=float(input('ingrese valor de nota 2 '))
nota2=float(input('ingrese valor de nota 3 '))
nota3=float(input('ingrese valor de nota 4 '))
nota4=float(input('ingrese valor de nota 5 '))
nota_total=(nota+nota1+nota2+nota3+nota4)/5
#mostras notas con decimal y redondeada

print('la nota con decimales es ',float(nota_total),'la nota redondeada es ',int(nota_total))
"""
#10- Crea una lista de tuplas con la siguiente información de empleados:
#Juan, 28, Ingeniero
#Ana, 32, Diseñadora
#Pedro, 45, Gerente
#Luisa, 29, Analista de Datos#
# accede y muestra la tupla completa del segundo empleado (Ana).#
# accede y muestra solo el nombre y el puesto del tercer empleado (Pedro).

#ingresa tupla sobre informacion de los empleados
"""
empleado="Juan", 28,"Ingeniero"
empleado1="Ana", 32,"Diseñadora"
empleado2="Pedro", 45, "Gerente"
empleado3="Luisa", 29,"Analista de Datos"

print(empleado1[:])
print(empleado2[0::2])
"""

#11- Escribir un programa que solicite al usuario su nombre y apellido, su edad. 
# Luego genere la variable z con el valor "Un gran día" e imprima por pantalla
#  con la leyenda: "Hola xxx xxx, tenes xxx años, te deseamos que tengas un gran día"
#pedimos datos al usuario
"""
nombre=input('inserte su nombre : ')
apellido=input('ingrese su apellido : ')
edad=input('ingrese su edad : ')
z="un gran dia"

#mostrar mensaje al usuario
print("hola ",nombre , apellido,' tenes ',edad ,' años, te deseamos que tengas ',z,)
"""

#hacer un programa que inicialice una valiable con 1ro de enero de ser asi diga
#feliz año 
"""
primerdia=[1,1]
mes=(int(input("que mes (en numero) estamos")))
dia=mes=(int(input("que dia (en numero) estamos")))
if mes and dia ==1 :
    print("Feliz año nuevo")
else:
    print("feliz dia") 
"""

#hacer una variable que inicialice con una variable que diga 2 de enero y preguntale 
# #si es primero de enero , al ser correcto devolvera feliz año nuevo si no, hoy no es año nuevo
"""
fecha="2 de enero"

if fecha=="1 de enero":
    print("FELIZ AÑO")
else :
    print ("no es año nuevo")

"""

#hacer un programa que averigue cuantas ruedas tiene un vehiculo
#si tiene una rueda sera un monociclo,2 sera moto, 3 triciclo, 4 sera auto, 5 muchas ruedas
#y numero negativo =muchas ruedas
"""
#determina numero de ruedas
ruedas=int(input('ingrese numero de ruedas : '))

#averiguar cuantas ruedas tiene
if ruedas==1:
    print("es un monociclo")
elif ruedas==2:
    print("es una moto")
elif ruedas==3:
    print("es un triciclo")
elif ruedas==4:
    print("es un auto")
elif ruedas==5:
    print("muchas ruedas")    
else:
    "no me chamuyes"            
"""

#WEscribir un programa que pregunte al usuario su edad y muestre por
#  pantalla si es mayor de edad o no
"""
#preguntas edad al usuario
edad=(int(input('ingrese su edad : ')))
#verificar edad
if edad>=18:
    print("felicidades puedes ir a la carcel")
else:
    print("aun no puedes ir a la carcel :C ")
"""
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. 

#pedir contrasena
"""
contrasena="contraseña"
print
#comprobar contrasena
contrasena2=input("ingrese su contrasena para logear : ")
if contrasena.lower==contrasena2.lower:
    print("bienvenido")
else:
    print("contraseña equivocada")    """

#Ejercicio
#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario 
#no introduce números debe devolver un aviso de error y si el divisor es cero también.
"""
#pedir numeros al usuario
numero=int (input("ingrese un numero 1 : "))
numero1=int(input("ingrese un numero 2 : "))

#calculo de numeros
operacion=numero/numero1 
                
if type(operacion)!= type(1):
    print("error")
elif operacion<=0:
    print("error")
else:
    print(operacion)
    """

    #Escribir un programa que pida al usuario un número entero 
    # y muestre por pantalla si es par o impar.
"""
numero=int(input('inserte numero'))
if numero%2==0:
    print('su valor es par')
else:
    print('su numero no es par')    
    """

    #Para tributar un determinado impuesto se debe ser mayor de 16 años y 
    # tener unos ingresos superiores a 1000 € mensuales. Escribir 
    # un programa que pregunte al usuario su edad 
    # y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

#identificar variables
"""
edad=int(input('ingrese su edad'))
ingreso=int(input('ingrese su ingreso mensual en euros'))

#verificacion de datos
if edad>=16 and ingreso>=1000:
    print('debe tributar : ')
else:
    print("no debe tributar : ")
    """

## Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo 
# y el nombre. El grupo A esta formado por las mujeres
# con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B
#  por el resto. Escribir un programa que pregunte 
# al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.     

"""
name= input("Ingrese su nombre: ")
gender= input ("Ingrese su sexo (M o H): ")

if gender== "M":
    if name.lower() < "m":
        group= "A"
    else:
        group= "B"

else:
    if name.lower > "n":
        group= "A"
    else:
        group= "B"
print ("Tu grupo es ", group)"""

#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte
#al usuario su renta anual y muestre por pantalla lo que tiene que pagar.
#determinar variable
"""
renta=float(input('ingrese su ingreso anual : '))

#creacion de condicional segun renta
if renta<10000:
    pago=renta*0.05
elif renta>10000 and renta<20000:
    pago=renta*0.15
elif renta>20000 and renta<35000:
    pago=renta*0.2
elif renta>35000 and renta<60000:
    pago=renta*0.3
elif renta>60000:
    pago=renta*0.45
else:
    print('no ingreso un valor valido')

# resultado
print("su monto a pagar es: ",pago)"""

#En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
#  traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
#  pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
#  mencionadas. A continuación se muestra una tabla con los niveles correspondientes 
# a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ 
# multiplicada por la puntuación del nivel.

#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
#  así como la cantidad de dinero que recibirá el usuario.
"""
#variables
nombre=input('ingrese nombre del empleado : ')
calificacion=(float(input('califique del 1 al 10 al empleado : '))/10)

#rendimiento y calificacion
if calificacion >=0 and calificacion<=0.3:
    rendimiento='su rendimiento es inaceptable y su bono es : '
elif calificacion >=0.4 and calificacion<=0.6:
    rendimiento='su rendimiento es aceptable y su bono es : '
elif calificacion<=0.6 and calificacion<=1:
       rendimiento='su rendimiento es meritorio y su bono es : '
else:
    print("nadie es tan bueno")

print(rendimiento,calificacion*2400)
"""
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes
# por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar
#  el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€

"""
#identificamos la edad del usuario
edad=int(input('ingrese edad del usuario'))
#evaluamos su edad y si es valida
if edad<4:
    monto='ingrese gratis porfavor!'
elif edad>=4 and edad<18:
    monto='su monto a pagar son 5€' 
elif edad>18:
    monto="pague 10€ luquitas sr"
else:
    print('eso no existe sr')
#mostramos monto a pagar
print(monto)
"""
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
#  y en función de su respuesta le muestre un menú con los ingredientes disponibles
#  para que elija. Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla 
# si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
#primero separo e identifico los ingredientes
ingredientes_vegetarianos=["tofu","pimiento"]
ingredientes_no_vegetarianos=["peperoni","jamon","salmon"]
#pido los ingredientes y lo agrego en una lista
ingredientes=[]
pedido=input("le gustaria tofu,pimenton,peperoni,jamon o salmon en su pizza : ")
ingredientes.append(pedido.lower())
pedido=input("le gustaria tofu,pimenton,peperoni,jamon o salmon en su pizza : ")
ingredientes.append(pedido.lower())

#verifico si los ingredientes son o no de una pizza vegetariana
if ingredientes in ingredientes_no_vegetarianos:
    print("su pizza no es vegetariana")
else:
     print("su pizza es vegetariana")  
     """

#Escribir un programa que solicite al usuario una letra y, 
# si es una vocal, muestre el mensaje “es vocal”.
#  Se debe validar que el usuario ingrese sólo un carácter.
#  Si ingresa un string de más de un carácter, informarle que no se puede procesar 
# el dato.
"""
#definir variables
vocales='aeiou'
letra=input('ingrese una letra : ').lower()

#verificar las codiciones
if letra in vocales:
    print('imprimio una vocal')
elif letra!= letra[0]:
    print ('escribio mas de una letra')
else:
    print('no escribio una vocal')
    """
#Hacer un programa que permita saber si un año es bisiesto. 
# Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
# excepto que también sea divisible por 400.
"""

ano=int(input('ingrese año para saber si es biciesto : '))
if ano%4==0 or ano%400==0:
    print('el año es biciesto')
else:
    print('el año no es biciesto')    
    """

#Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, 
# procesar observaciones sobre las clases de ese día. 
# El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases
#  en un día de la semana diferente: los lunes se dicta el nivel inicial, 
# los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para
#  práctica hablada y los viernes se dicta inglés para viajeros.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato
#"día, DD/MM", donde [día] es un día de la semana, DD es el número de día 
#y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente
#o una fecha cuyo día supere el número 31 o el mes supere el número 12,
#finalizar el programa indicando que se produjo un error. Debe permitirse 
#que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. 
#Como precondición se tiene que lo ingresado por el usuario tendrá la forma 
#<[alfanumérico], [numérico]/[numérico]>.
#Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron 
#exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado,
#ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. 
#Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, 
#y el programa le mostrará el porcentaje de aprobados.
#Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar
#el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" 
#en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
#Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1
#o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario 
#que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, 
#para luego imprimir el ingreso total en $.
"""
dia=str(input("ingrese la inicial del dia de la semana : \n\tlunes\n\t martes\n\tmiercoles\n\tjueves\n\tviernes\n\tsabado\n\tdomingo: \n  ")).lower()
fecha=int(input("ingrese dia del mes en numero :"))
mes=int(input("ingrese mes del año en numero :"))
if dia!="lunes"and"martes"and"miercoles"and"jueves"and"viernes"and"sabado"and"domingo":
    print("no ingreso un dia valido")
elif dia=="lunes"or "martes" or "miercoles":
    alumnos=int(input("ingrese la cantidad de alumnos totales : "))
    aprobados=int(input("ingrese cantidad de alumnos aprobados"))
    print("la cantidad de alumnos aprobados fueron: ", alumnos/aprobados)
elif dia=="jueves":
    alumnos=int(input("ingrese cantidad de alumnos : "))
    asistencia=input("ingrese la cantidad de presentes : ")
    if alumnos/asistencia*10<=50:
        print("la mayoria no se presento")
    else:
        print("la mayoria se presento")
elif dia=="viernes" or fecha==1 and mes==1 or mes==7:
    print("feliz comienzo de ciclo ") 
    alumnos=int(input("ingrese cantidad de alumnos : "))
    valor=int(input("ingrese valor del arancel : "))
    print("el ingreso total es igual= ",alumnos*valor)
elif dia>=32 or mes>=13:
    print("ingreso una fecha inexistente")
else:
    print("ese dia no laburamos")    
"""

#Escribir un programa que pida al usuario un número entero positivo
#  y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
numero=int(input("ingrese un numero entero positivo :"))
for i in range (numero,0-1,-1 ):
    print(i, end=(","))
    """
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#  el interés anual y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión cada año que dura la inversión.
"""
inversion=float(input("Cuanto dinero desea invertir; "))
interes=(float(input("Cuanto interes mereces en % :")))
tiempo=int(input("cuantos años estara tu dinero en inversion : "))

for i in range (tiempo):
    ganancia=(inversion*interes*0.1)+inversion
    print ("tu ganancia este año es :", ganancia)
    inversion=ganancia
       """


# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
"""
n=int(input("Número entero: "))
for i in range (1,n+1,2):
    for j in range(i,0,-2):
        print (j, end=" ")
    print("")
"""

#tabla de multiplicar
"""
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("")
   """
   #imprimir todos los numeros decimales del 0 al 9
"""
for i in range(0,11):
    print((i*0.1),((i*0.1)+1),((i*0.1)+2),((i*0.1)+3),((i*0.1)+4),((i*0.1)+5),((i*0.1)+6),((i*0.1)+7),((i*0.1)+8),9) 
"""
#imprimir todos los numeros del 100 al 199
"""
for i in range (100,200):
    print(i)
"""
"""
#imprimir todos los numeros entre el 5 y el 20 saltando de 3 en 3
for i in range(5,21,3):
    print(i)
"""
#pedir al usuario que ingrese una palabra y hacer que se muestre en pantalla la cantidad
#de vocales que tiene
"""
palabra=input("ingrese una palabra :").lower()
vocales="aeiou"
contador=0
for letra in palabra:
    if letra in vocales:
        contador+=1
        print(contador)
"""
#ingresar un programa que ingrese la sumatoria de todos los numeros entre 0 y 100
"""
suma=0
for i in range(0,101):
    suma=suma+i
print(suma)"""

#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números ingresados.
"""
#pido numero enteros al usuario:
num=int(input("ingrese algun numero entero "))
total=0
while num!=0:
    total+=num
    num=int(input("ingrese algun numero entero "))
   """ 
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números ingresados
#  y los numeros ingresados.

"""
num=int(input("ingrese algun numero entero "))
total=0
lista=[]
while num!=0:
    total+=num
    lista.append(num)
    num=int(input("ingrese algun numero entero "))
print(total,"\n",lista)
 """    
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
#  Informar cuál fue el mayor número ingresado.
"""
num=int(input("ingrese algun numero entero "))
total=0
while num!=0:
    if num>total:
        total=num
    else:    
        num=int(input("ingrese algun numero entero "))
print(total)        """

# Crear un programa que permita al usuario ingresar los montos de las compras 
# de un cliente (se desconoce la cantidad de datos que cargará, 
# la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando 
# el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese 
# un nuevo monto. Al finalizar, informar el total 
# a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

#ingresar monto ingresado por usuario
"""
monto=float(input("ingresar monto del producto a comprar"))
total=0
while monto!=0:
    
    if monto<=-1:
        monto=float(input("ingresar monto del producto a comprar"))
    else:
        total+=monto
        monto=float(input("ingresar monto del producto a comprar"))

if total>1000:
    print("su total es :", total*0.9)
else:
    print  ("su total es :", total)      
"""
#Solicitar al usuario que ingrese su dirección email.
#Imprimir un mensaje indicando si la dirección es válida o no, 
#valiéndose de una función para decidirlo.
#Una dirección se considerará válida si contiene el símbolo "@".
"""
email=input("ingrese su direccion de email")
def valido (correo):
    if "@" in correo:
        print("su direccion de correo es valida")
    else:
        print("su direccion de correo es invalida")

valido (email)
"""
#Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos
#  (utilizando una función que realice dicha suma).
"""
numero=0

def suma(numero,guardar):
    numero=float(input("ingrese numeros a sumar"))
    guardar=[]
    total=0
    while numero!=0:
        numero=float(input("ingrese numeros a sumar"))
        guardar.append(numero)
        total+=numero
    print(guardar)    

suma(1,1)    

"""
#1
"""
#datos del circulo
radio=float(input("ingrese radio del circulo :"))
#se realiza la funcion
def circulo(radio):
    area=3.14*radio**2
    perimetro=2*3.14*radio
    print("el area del circulo es: ",area," y su perimetro es : ",perimetro)
#se llama la funcion con la variable
circulo(radio)  """

#2"""
#definimos la palabra a repetir
"""
palabra=input("ingrese una palabra a repetir : ")
contador=0
#hacemos bucle y terminamos funcion
while contador<=25:
    print(palabra)
    contador+=1
"""
#3
"""
for tabla in range(2,11):
    for m in range(1,10):
        print(tabla*m,"\t", end="")
    print("")
"""
#4
"""
#ingreso de variables
numero=float(input("ingrese un valor de numero positivo :"))
mayor=0
#while que determina el bucle  
while numero!=-8:
      
    if numero<0:
        numero=int(input("dije: ingrese un valor de numero positivo :"))
    elif numero>0:
        if numero>mayor:
            mayor=numero
            numero=float(input("ingrese un valor de numero positivo :"))
            
        else:
            numero=float(input("ingrese un valor de numero positivo :"))
       
    else:
        print("no ingreso un numero")  
        numero=float(input("ingrese un valor de numero positivo :"))  
#ruptura del bucle y muestra del numero mayor                  
print("el mayor valor ingresado es : ",mayor)     
    """

#5
# parametros formales:lan, an, per
# parametros reales:largo, ancho 
#el nombre de la funcion es perimetro_rectangulo
# la funcion se llama dentro del print en la linea 12 luego del string y la coma

#6
#listas dadas
"""
jugadores=["messi",91],["bape",86],["cristiano ronaldo",89]
arqueros=[["dibu",35],["bounou,30"],["lloris",7] ]
#lista del nuevo arquero
nuevoarquero=[]
nombre=input("ingrese el nombre del arquero : ")
goles=int(input("ingrese cantidad de goles : "))
#se agregan y combinan las listas
nuevoarquero.append(nombre)
nuevoarquero.append(goles)
arqueros.append(nuevoarquero)
#para confirmar mostramos
print(arqueros)
"""

