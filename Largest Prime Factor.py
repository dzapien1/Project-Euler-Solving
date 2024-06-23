'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

factores = []
def fact_primos(numero): 
  div = 2
  while numero > 1:
    while numero % div == 0:
      factores.append(div)
      numero = numero // div
    div = div + 1
  return factores
  
fact_primos(600851475143)

