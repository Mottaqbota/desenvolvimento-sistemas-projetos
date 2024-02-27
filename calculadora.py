def soma(x, y):
  resultado = x + y
  return resultado

def subtracao(x, y):
  resultado = x - y
  return resultado

def multiplicacao(x, y):
  resultado = x * y
  return resultado

def divisao(x, y):
  resultado = x / y
  return resultado

def calcular(x, operacao, y):
  if operacao == '+':
    return soma(x, y)
  elif operacao == '-':
    return subtracao(x, y)
  elif operacao == '*':
    return multiplicacao(x, y)
  elif operacao == '/':
    return divisao(x, y)
  else:
    return 'Operação inválida'

def main():
  x = int(input('Digite o primeiro número: '))
  operacao = input('Digite a operação (+, -, *, /): ')
  y = int(input('Digite o segundo número: '))
  resultado = calcular(x, operacao, y)
  print('========================')
  print(f'| {x} {operacao} {y} = {resultado} |')
  print('========================')

main()
