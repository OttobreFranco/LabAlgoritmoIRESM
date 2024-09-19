# 1 Declara dos variables, llamadas nombre y edad.
#   Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

print("Ejercicio 1:")

nombre = 0
edad = 0
nombre = "Tony Soprano"
edad = 51

# 2 Crea tres variables:
    #nombre
    #apellido
    #nombrecompleto
# A nombre, asígnale el valor "Julia", y en apellido, 
#asigna el valor "Roberts". Finalmente, 
#construye la variable nombrecompleto concatenando 
#las variables (recuerda sumar un espacio intermedio).
print("Ejercicio 2:")
nombre = 0
apellido = 0
nombrecompleto = 0
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = (nombre + " " + apellido)
print(nombrecompleto)

# 3) Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
#Estás tomando un curso de curso
#Para ello deberás concatenar la primera parte de la 
# frase con el valor que asumirá la variable. 
# Recuerda agregar un espacio antes de concatenar la 
# variable al resto del texto.
print("Ejercicio 3:")

curso = "Python"
print("Estás tomando un curso de " + curso)

# 4)Práctica con Integers
# Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

# Imprime el tipo de dato de dicha variable.
print("Ejercicio 4:")
num_entero = 26
print("El tipo de dato es: " , type(num_entero))

# 5)Práctica con Floats
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

# Imprime el tipo de dato de dicha variable.
print("Ejercicio 5:")
num_decimal = 26.05

print("El tipo de dato es: " ,type(num_decimal))


# 6)Práctica con Tipos de Datos Numéricos
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

# Para ello, crea dos variables:

# num1 = 7.5

# num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.
print("Ejercicio 6:")
num1 = 7.5
num2 = 2.5

print("El tipo de dato es: " ,type(num1+num2))

#Es una variable de tipo float


# 7) Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
# num1 = 7.5

print("Ejercicio 7:")
num1 = 7.5
print("El tipo de dato es: " ,type(int(num1)))


# 8)Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
# num2 = 10
print("Ejercicio 8:")

num2 = 10
print("El tipo de dato es: " ,type(float(num2)))


# 9) Práctica con Conversiones 3
# Suma los valores de num1 y num2.
# No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().

print("Ejercicio 9:")
num1 = "7.5"
num2 = "10"

print("El resultado de la suma es: " , float(num1) + int(num2))



# 10) Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

print("Ejercicio 10:")
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")


# 11) Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto

print("Ejercicio 11:")
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


# 12)Práctica Formatear Cadenas 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos
print("Ejercicio 12: ")
puntos_totales = 0
puntos_anteriores = 500
puntos_nuevos =  1000
puntos_totales = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# 13)Práctica Operadores Matemáticos 1
# Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.

# Debes mostrar solo el valor numérico que resulta de esta operación.

print("Ejercicio 13: ")
print(874//27)

# 14) Práctica Operadores Matemáticos 2
# Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.

# Debes mostrar solo el valor numérico que resulta de esta operación.
print("Ejercicio 14: ")
print(456%33)

# 15)Práctica Operadores Matemáticos 3
# Calcula y muestra en pantalla la raíz cuadrada de 783.

# Debes mostrar solo el valor numérico que resulta de esta operación.

print("Ejercicio 15: ")
print(783**0.5)

# 16) Práctica Redondeo 1
# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.

print("Ejercicio 16: ")
print("El valor de 10/3 redondeado es: " , round(10/3,2))


# 17) Práctica Redondeo 2
# Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

print("Ejercicio 17: ")
print("El numero 10.676767 redondeado es: " , round(10.676767))

# 18) Práctica Redondeo 3
# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
print("Ejercicio 18: ") 
print(round(5**0.5,2))