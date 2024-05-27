#Варіант №16 Напишіть програму, яка реалізує алгоритм підрахунку суми значень елементів головної 
#та побічної діагоналі двовимірного масиву. Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.
#Автор Савченко Валентина 31І

import random

n = random.randint(0, 15)
print(f'Розмірність масиву: {n}')
m=n

arr = [[random.randint(0, 15) for j in range(n)] for i in range(m)]

print("Масив:")
for row in arr:
    print(row)

sum_main_diag = 0
for i in range(n):
    sum_main_diag += arr[i][i]

sum_side_diag = 0
for i in range(n):
    sum_side_diag += arr[i][n - i - 1]

print(f"Сума елементів головної діагоналі: {sum_main_diag}")
print(f"Сума елементів побічної діагоналі: {sum_side_diag}")