def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = int(input("Please enter an option:"))
    match choice:
        case 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored! " + encoded_password)
        case 2:
            print("")
        case 3:
            quit()


def encode(password):
    encoded_password_list = []
    for individual_number in password:
        converted_num = int(individual_number)
        for i in range(0, 3, 1):
            if converted_num + 1 >= 10:
                converted_num = 0
            else:
                converted_num += 1
        encoded_password_list.append(str(converted_num))
    return "".join(encoded_password_list)


if __name__ == '__main__':
    menu()
