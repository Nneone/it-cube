print("Стартовое кол-во организмов?")
m = int(input())
print("Среднесуточное увелечение в %")
p = int(input())
print('Кол-во дней для размножения?')
n = int(input())
for i in range(n):
    if i == 0:
        i += 1
        print( m)
    m = m + p / 100 * m 
    print(i, m)


