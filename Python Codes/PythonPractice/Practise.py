# print
''' x = 2
y = 3
z = 4.2
print(x, y, z)
print(x, y, z, sep=',')
print(x, end='')
print("hello")
print(f'hello {z} bye {x}')
# Print Curly brace
print(f'hello {z} {{ good }} bye {x}') '''

# s = '100'
# a = int(s)
#
# print(a, type(a))
# print(s, type(s))
# x = 100
# print(bin(x))

# a = 1
# b = 2.1
# c = "hello"
# d = 'another hello'
# e = False
#
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(e, type(e))


L = [1, 2, 3, 4]
print(L)
length = len(L)
print(L[length - 1])
print(L[-1])

L = [5, 6, 7, 8, 9]
print(L[2:4])
sublist = L[1:-1]
print(sublist)
print(L)

print(L[1:])
print(L[:4])
print(L[:])
print(L[::-1])