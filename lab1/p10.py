def main():
    str = input("Enter a string: ")
    str_array = str.split(" ")
    str_array_len = len(str_array)
    sol = 0
    for i in range(str_array_len):
        if len(str_array[i].split(" ")) == 1 and str_array[i] != "":
            sol += 1
    print(sol)

main()