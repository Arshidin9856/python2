
lst = list(map(int, input().split()))
print(lst[-1:])
print(lst[:-1])

lst = lst[-1:] + lst[:-1]
print(lst)
