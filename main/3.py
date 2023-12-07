import sys

# read from command the path of the file using os python3 3.py file.txt
file = sys.argv[1]
arr = []

# open the file
try:
    f = open(file, "r")
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            # check number
            if word.isdigit() or word[1:-1].isdigit():
                arr.append(int(word))
    f.close()
except:
    print("Error opening the file")

print(arr)
# print sum
print(sum(arr))
# print avg
print(sum(arr) / len(arr))
print(min(arr))
print(max(arr))

arr.sort(key=lambda x: (len(str(abs(x))), x), reverse=True)

try:
    f = open("output.txt", "w")
    f.write(f"Sum: {sum(arr)}\n")
    f.write(f"Avg: {sum(arr) / len(arr)}\n")
    f.write(f"Min: {min(arr)}\n")
    f.write(f"Max: {max(arr)}\n")
    f.write(f"Sorted: {arr}\n")
    f.close()
except:
    print("Error opening the file")