##--------------ejercicio 2------------
##--------------serie de fibonacci------

#impresion en consola
def fibonacci(n):
    sequence=[0,1]
    while len(sequence)<n:
        sequence.append(sequence[-1]+sequence[-2])
        return sequence
    
    while True:
            n=int(input("enter the value of n(enter 0 to exit):"))
            if n<0:
                 print("error:n must be a non-negative integer.")
            else:
                 break
except ValueError:
print("error:n must be a valid integer.")

while any!=0:
     sequence=fibonacci(n)
     print(sequence)
     while True:
          n=int(input("enter the value of n(0 to exit):"))
          if n<0:
               print("error:n must be a non-negative integer.")
          else:
               break
     except ValueError:
print("error:n must be a valid integer.")







    
    
    

