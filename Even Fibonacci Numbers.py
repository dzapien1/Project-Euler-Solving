'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10
terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...
By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued
terms.
'''
suma_num_pares = 0
a0 = 0 
a1 = 1
print(a0)
print(a1)
a2 = a0 + a1
print(a2)
for f in range(1, 32):
    f = a1 + a2
    a1 = a2
    a2 = f
    if f%2 == 0:
        suma_num_pares = suma_num_pares + f
print(f) 
print(suma_num_pares)
    
    