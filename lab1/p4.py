def main():
    str = input("Enter string: ")
    str_sol = ""
    str_len = len(str)

    for i in range(str_len):
        if not str[i].isalpha():
            continue
        if str[i].islower():
            str_sol += str[i]
        elif i != 0:
            str_sol += f"_{str[i].lower()}"
        else:
            str_sol += f"{str[i].lower()}"
    print(str_sol)


main()

