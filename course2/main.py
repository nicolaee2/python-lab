a = 31
print(f"{a:#0x}")

# lambda function = function without a name
# role: pointer to a function, functions that expect a callback
# lambda <list_of_parameters>: return_value

addition = lambda x, y: x + y
print(addition(3, 5))

# lambdas are bind at run-time
# can create dynamic lambdas
# this programming paradigm is called closure
def CreateDivizibleCheckFunction(n):
    return lambda x: x % n == 0


fnDiv2 = CreateDivizibleCheckFunction(2)
fnDiv7 = CreateDivizibleCheckFunction(7)
x = 14
print(x, fnDiv2(x), x, fnDiv7(7))

# a sequence is a ds represented by a vector of elements
# list -> mutable vector
# tuple -> immutable vector
x = list()
x = []
x = [10, 20, "test"]
x = [10,]
x = [1, 2] * 5
x, y = [1, 2]

x = tuple()
x = ()
x = (10, 20, "test")
x = 10, 20, "test"
x = (10, )
x = (1, 2) * 5
x = 1, 2 * 5
x, y = (1, 2)

x = ('A', 'B', 2, 3, 'C')
y = list(x)

x = ['A', 'B', 2, 3, 'C']
y = tuple(x)

# both lists and tuples can be concatenated, but not with each other
# tuples are used to return multiple values from a function

def ComputeSmt(*list_of_numbers):
    s = 0
    p = 1
    for i in list_of_numbers:
        s += i
        p *= i
    return s, p


suma, produs = ComputeSmt(1, 2, 3, 4, 5)
print(suma, produs)

for i in [1, 2, 3, 4]:
    print(i)

for i in (1, 2, 3, 4):
    print(i)

# can use len

for index, name in enumerate(["Dragos", "Mihai", "Nicu", "Vlad"]):
    print("Index:%d => %s" % (index, name))

for index, name in enumerate(("Dragos", "Mihai", "Nicu", "Vlad")):
    print("Index:%d => %s" % (index, name))

for index, name in enumerate(["Dragos", "Mihai", "Nicu", "Vlad"], 2):
    print("Index:%d => %s" % (index, name))

x = [i for i in range(1, 10)]
print(x)

x = [i for i in range(1, 10) if i % 3 == 0]
print(x)

x = [i*i for i in range(1, 6)]
print(x)

x = [x for x in range(2, 100) if len([y for y in range(2, x // 2 + 1) if x % y == 0]) == 0]
print(x)

# adding new elements in the list, use append or +=
x = [1, 2, 3]
x.append(4)
x += [5]
x += [6, 7]
x += (8, 9, 10)
x[len(x):] = [11]
x.extend([12, 13])
print(x)

# can use list += tuple, but can't list + tuple
x = [1, 2, 3]
x.insert(-1, "A")
print(x)

x = [1, 2, 3]
x.remove(2)
print(x)

x = [1, 2, 3, 4, 5]
del x[2]
del x[-1]
print(x)

x = [1, 2, 3, 4, 5]
x.pop(2)
y = x.pop()
print(x, y)

x = [1, 2, 3, 4, 5]
del x[:]
print(x)

x = [1, 2, 3, 4, 5]
x.clear()
print(x)

# to copy a list, use list(x) or use x.copy() or x[:]
# to find an element use x.index(smt) or use smt in x

x = [1, 2, 3]
y = [4, 5, 6]
print(list(map(lambda a,b: a + b,x,y)))

x = [2, 1, 4, 3]
y = reversed(x)
z = sorted(x)
print(z)
print(y)

x = [1, 2, 3]
y = [10, 11, 12]
print(list(zip(x, y)))
x = [(1, 2), (3, 4)]
a, b = zip(*x)
print(a, b)
x = [[3, 4], [3, 4]]
a, b = zip(*x)
print(a, b)