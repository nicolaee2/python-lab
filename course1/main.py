print("Hello World")
x = 10
s = "a string"
b = True
x = 10
x = "a string"
x = 10
print(x, type(x))

x = 9999999999999999999999999
print(x, type(x))

x = 1.123
print(x, type(x))

x = 1.2j
print(x, type(x))

x = True
print(x, type(x))

x = None
print(x, type(x))

x = 10 < 20 > 15
print(x, type(x))

x = 10.123
y = int(x) # y = 10
y = float(y) # y = 10.0
y = str(y) # y = "10.0"

# y = int("10.0") # va da eroare pentru ca numarul din string este un float
y = int("10") # y = 10
y = float("10") # y = 10.0
