def somar(num1, num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    if num2 == 0:
        return("Não se pode dividir por 0")
    return num1 / num2

def porcentagem(num1, num2):
    if num2 == 0:
        return("Indefinido")
    return num1 * num2 / 100