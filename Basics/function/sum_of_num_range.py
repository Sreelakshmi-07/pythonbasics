n1 = int(input("Enter inital:"))
n2 = int(input("Enter final: "))
def sum_range (n1, n2):
    s=0
    while n1 <= n2:
        if n1 % 2 == 0:
          s = s + n1
        n1 = n1 + 1
    return s
print(sum_range(n1, n2))

