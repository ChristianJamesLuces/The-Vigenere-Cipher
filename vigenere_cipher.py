# 2:Pseudocode
import pyfiglet

# Define variables
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font="digital")
no_option = ("No", "no", "NO", "n", "N")
yes_option = ("Yes", "yes", "YES", "y", "Y")
gratitude = "\033[42m" + "(: Thank you for using this program! :)" + "\033[0m"

# Display a welcome message
while True:
    print(intro)
    print("\033[45;1m" + "This program will show you the Add, Mod, and the Ciphertext of base from your Message and Key.\n" + "\033[0m")
    print("\033[7;1m" + "REMINDER:" + "\033[0m" + " The 'Message' and 'Key' should be all in uppercase letters and no space....\n\n")

    # Ask for user input in message and key
    while True:
            message = input("\033[1m"+"Message: " + "\033[0m").replace(" ", "").upper()
            # Translate the letters in message to its corresponding numbers (0-25)
            if message.isalpha():
                message_numbers = [(ord(char) - 65) % 26 for char in message]
                break
            else:
                print("Invalid input. Please enter letters only.\n")
                continue

    while True:
            key = input("\033[1m" + "Key: " + "\033[0m").replace(" ", "").upper()
            # Translate the letters in key to its corresponding numbers (0-25)
            if key.isalpha():
                key_numbers = [(ord(char) - 65) % 26 for char in key]  
                break
            else:
                print("Invalid input. Please enter letters only.\n")
                continue

    # Calculate Add, Mod, and Ciphertext
    add_numbers = []
    key_set = []
    for i in range(len(message_numbers)):
        key_list = key_numbers[i % len(key_numbers)]
        add_numbers.append((message_numbers[i] + key_list))
        key_set += [key_list]

    mod_numbers = [(num % 26) for num in add_numbers]
    ciphertext = "".join([chr(num + 65) for num in mod_numbers])

    # Print the output
    print("\033[93;1m" + "\nMessage: " + "\033[0m" + "\033[91;1m" + f"{message} {message_numbers}" + "\033[0m") 
    print("\033[93;1m" + "Key:     " + "\033[0m" + "\033[91;1m" + f"{key} {' ' * (len(message) - len(key))} {key_set}" + "\033[0m") 
    print("\033[93;1m" + "Add:     " + "\033[0m" + "\033[91;1m" + f"{add_numbers}" + "\033[0m") 
    print("\033[93;1m" + "Mod:     " + "\033[0m" + "\033[91;1m" + f"{mod_numbers}" + "\033[0m") 
    print("\033[93;1;4m" + "Ciphertext:" + "\033[0m" + "\033[94;1m" + f" {ciphertext}" + "\033[0m")

    # Asking the user if they want to try it again
    answer = str(input("\nDo you want to try it again? (Yes or No): "))
    # If the user want to try it again 
    if answer in yes_option: 
        print("\n\n")
    # If the user do not want to try it again
    elif answer in no_option:
        print("\n" + "<" * 100) 
        print(gratitude.center(100))
        print(">" * 100)
        break
    # If the user did not input a valid answer
    while answer not in no_option+yes_option:
        print ("Invalid Input")
        answer = str(input("\nDo you want to try it again? (Yes or No): "))
    # Exit the loop if they do not want to try it again
    # Go back to the start of the loop