def menu(stored_password):
    	print("Menu")
    	print("-------------")
    	print("1. Encode")
    	print("2. Decode")
    	print("3. Quit")
    	choice = int(input("Please enter an option: "))
    	match choice:
        	case 1:
            		password = input("Please enter your password to encode: ")
            		encoded_password = encode(password)
            		print("Your password has been encoded and stored! ")
        	case 2:
            		print("The encoded_password is " + stored_password + ", and the original password is " + decode(stored_password) + ".")
        	case 3:
            		quit()


def encode(password):
    	# list of integers to be converted into a single string
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

def decode(encoded_password):
    	decoded_password_list = []
    	decoded_num = 0
    	for num in encoded_password:
        	decoded_num = int(num) - 3
        	if decoded_num < 0:
            		decoded_num += 10
        	decoded_password_list.append(str(decoded_num))
    	return "".join(decoded_password_list)

if __name__ == '__main__':
	stored_password = ""
	while True:
		stored_password = menu(stored_password)
		print("")

