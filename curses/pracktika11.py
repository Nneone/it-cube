z = int(input())
x = int(input())
c = int(input())
if x > z > c or x < z < c:
    print(x)
elif z > x > c or z < x < c:
    print(z)
elif c > x > z or c < x < z:
    print(c)
else:
    print("Нет среднего числа")

    
