def reassign(lst):
    lst = [0, 1]


def append(lst):
    lst.append(2)


lst = [0]
reassign(lst)
print(lst)
append(lst)
print(lst)


def gen_f():
    i = 0;
    for j in range(10):
        yield i
        i += 1
        print("calling", i)


obj = gen_f()
for i in range(12):
    print(next(obj))