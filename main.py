from time import time

a = 102
a = 101
start = time()
while True:
    a -= 1
    if a:
        b = a**3211 * a
    else:
        break
print(time() - start)


start_2 = time()
for i in range(10):
    b = i**3211 * i
print(time() - start_2)


start_3 = time()
b = [i**3211 * i for i in range(10)]
print(time() - start_3)

print('Завершено')
