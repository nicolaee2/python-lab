print("Hello World")
x = 10 # 10
s = "a string" # "a string"
b = True # True
x = 10 # 10
x = "a string" # "a string"
x = 10 # 10, <class 'int'>
x = 9999999999999999999999999 # 9999999999999999999999999, <class 'int'>
x = 1.123 # 1.123, <class 'float'>
x = 1.2j # 1.2j, <class 'complex'>
x = True # True, <class 'bool'>
x = None # None, <class 'NoneType'>
x = 10 < 20 > 15 # True
x = 10.123 # 10.123
y = int(x) # y = 10
y = float(y) # y = 10.0
y = str(y) # y = "10.0"
# y = int("10.0") # will throw an error because "10.0" is not an integer
y = int("10") # y = 10
y = float("10") # y = 10.0
x = 10 + 20 * 3 # 70, <class 'int'>
x = 10 + 20 * 3.0 # 70.0, <class 'float'>
x = 2**8 # 256
x = 2**8.1 # 274.374
x = int(10.123) # 10
x = float(10) # 10.0
x = 10.0 / 3 # 3.3333333333333335
x = 10.0 % 3 # 1.0
x = 10.0 // 3 # 3.0
x = 11.9 // 3 # 3.0
x = 0xFFFFFFFF # 4294967295
x = (x + x) & 0xFFFFFFFF # 4294967294
y = 123
y = (y + y) & 0xFF # 246
s = "a string\nwith lines" # "a string\nwith lines"
s = 'a string\nwith lines' # "a string\nwith lines"
s = r"a string\nwith lines" # "a string\\nwith lines"
s = r'a string\nwith lines' # "a string\\nwith lines"
s = """a string
with lines""" # "a string\nwith lines"
s = '''a string
with lines''' # "a string\nwith lines"
s = "Name: %8s Grade: %d" % ("Ion", 10) # "Name:      Ion Grade: 10"
s = "Grade: %d"%10 # "Grade: 10"
s = str(10) # "10"
s = repr(10) # "10"
s = "Name: %(name)8s Grade: %(grade)d" % {"name": "Ion", "grade": 10} # "Name:      Ion Grade: 10"
s = "Python"\
"exam" # "Pythonexam"
a = 100
s = f"Python {a}" # "Python 100"
s = f"Python {a + 1}" # "Python 101"
s = f"Python {a + 1:08}" # "Python 00000101"
s = f"Python {a + 1:08.2f}" # "Python 00000101.00"
s = f"Python {a + 1:8}" # "Python      101"
s = f"Python {float(a)}" # "Python 100.0"
s = f"Python {a:#0x}" # "Python 0x64"
s = "PythonExam"
s[1] # "y"
s[-1] # "m"
s[-2] # "a"
s[:3] # "Pyt"
s[4:] # "onExam"
s[3:5] # "ho"
s[2:-4] # "thon"
s = "Python" + "Exam" # "PythonExam"
s = "A" + "12" * 3 # "A121212"
"A" in "Python" # False
"A" not in "Python" # True
len(s) # 7
s = "PythonExam"
s[1:7:2] # "yhn"
