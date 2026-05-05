### EXCEPTIONS

numberOne, numberTwo = 5, 1

numberTwo = "1"

# try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce un error
    print("Se ha producido un error")
    
# try except else
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # opcional
    # se ejecuta si no se produce un error
    print("la ejecucion continua correctamente")
finally: # opcional
    # se ejecuta siempre
    print("la ejecucion continua")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un error de tipo ValueError")
except TypeError:
    print("Se ha producido un error de tipo TypeError")
    
# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)

