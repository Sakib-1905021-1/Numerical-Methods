def my_square(x):
    return x*x
def my_division(x,y):
    return int(x/y), x % y
def my_divisiondef(x, y=5):
    return int(x / y), x % y
def info(student_ID, *var):
    print(student_ID)
    if(len(var) > 0):
        print(var[0])
    if len(var) > 1:
        print(var[1])
    return None

print(my_square(89))
print(my_division(50, 25))
print(my_divisiondef(50))
info("1905021", "Sakib Mohammed Sobaha", "104")
