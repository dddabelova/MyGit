# -*- coding: utf-8 -*-
"""tasks.ipynb

#задание1
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

#задание2
A = int(input('Число А:'))
B = int(input('Число B: '))
for i in range(A, B + 1):
if (i // 1000) == i % 10 and (i // 100) % 10 == (i // 10) % 10:
print(i)

#задание3
A = int(input('Число A:'))
A = str(A)

A_reverse = A[::-1]
if A_reverse == A:
print('Число ' + A + ' - палиндром')
else:
print('Число ' + A + ' не палиндром')
