#############################################################################
INSTRUCCION
#Crear una función:
def func(parámetro, parámetro):
    #código de la función <-- Identación
    return

    return (expresion)
    
#Llamar la función:
func(argumento, argumento)
#Almacenar el retorno de la función (si tiene uno):
variable = func(argumento, argumento)

Al incluir un “return” le estamos diciendo a python que retorne inmediatamente
 el valor de resultado de la función y use la siguiente expresión como un valor de retorno”
#############################################################################


def nota_quices(codigo:str, nota1:int, nota2:int, nota3:int, nota4:int, nota5:int)->str:
    promedium=[nota1, nota2, nota3, nota4, nota5]
    promedium.remove(min(promedium))
    promedium=round((((sum(promedium))/len(promedium))*0.05),2)
    return (f"El promedio ajustado del estudiante {codigo} es: {promedium}")
    
print(nota_quices("Judas Priest", 24, 56, 78, 23, 80))


#############################################################################




def repetir_funciones():
    imprime_Cosas()
    imprime_Cosas()
    
def imprime_Cosas():
    print("La clase esta genial")   
    print('Python es lo maximo')
    
repetir_funciones()


#############################################################################

# def nota_quices(codigo:str, nota1:int, nota2:int, nota3:int, nota4:int, nota5:int)->str:
#     promedium=[nota1, nota2, nota3, nota4, nota5]
#     promedium.remove(min(promedium))
#     promedium=round((((sum(promedium))/len(promedium))*0.05),2)
#     print (f"El promedio ajustado del estudiante {codigo} es: {promedium}")
#     return 

# codigo="Judas Priest"
# nota1=24
# nota2=56
# nota3=78
# nota4=23
# nota5=80
