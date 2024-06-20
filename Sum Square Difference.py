'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2+... +10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2+... +10) = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
suma_cuadrados = 0
cuadrados_suma = 0

for s in range(1, 101):
  suma_cuadrados = suma_cuadrados + (s**2)

for c in range(1,101):
  cuadrados_suma = cuadrados_suma + c
cuadrados_suma = cuadrados_suma**2

print(cuadrados_suma - suma_cuadrados)

