n, n1, n2 = int(input()), int(input()), int(input())
mx =max(n, n1, n2)
mn = min(n, n1, n2)
summ = n + n1 + n2
num2 = mx + mn 
nums = summ - num2
print(mx, nums, mn)