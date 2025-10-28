#asignacion
#numero = 3 # es una variable que almacena un nuemro entero y se ocupa int

#comparacion
#if numero == 5:
    #print("es numero es igual a 5")
#else:
     #print("es numero no es igual a 5")


     # while es mientras

     #contador = 1

#while contador < 6:
  #print(contador)
  #contador += 1 #es lo mismo que contador incremento + 1


#for i in range(0,10):
  #print(i)

for num in range(1,16):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)