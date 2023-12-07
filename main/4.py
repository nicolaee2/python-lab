import sys
import os

folder = sys.argv[1]
extension_count = {}
longest = ""
shortest = ""
second_c = ""

# use os.walk to get all files in the folder
for _, _, files in os.walk(folder):
    print(files)

    # get longest name, shortes, first file with seond letter c
    longest = files[0]
    shortest = files[0]
    for file in files:
        if len(file) > len(longest):
            longest = file
        if len(file) < len(shortest):
            shortest = file
        if file[1] == "c" and second_c == "":
            second_c = file

    # get list of extensions
    for file in files:
        extension = file.split(".")[-1]
        if extension in extension_count:
            extension_count[extension] += 1
        else:
            extension_count[extension] = 1

# sort extensions by count descending
sorted_extensions = sorted(extension_count.items(), key=lambda item: (item[1], item[0][1]), reverse=True)
print(sorted_extensions)

# write to file
try:
    f = open("output.txt", "w")
    f.write(f"Longest: {longest}\n")
    f.write(f"Shortest: {shortest}\n")
    f.write(f"Second c: {second_c}\n")
    f.write(f"Extensions: {sorted_extensions}\n")
    f.close()
except:
    print("Error opening the file")


