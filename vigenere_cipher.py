# 2:Pseudocode
import pyfiglet

# Define variables
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font="digital")
no_option = ("No", "no", "NO", "n", "N")
yes_option = ("Yes", "yes", "YES", "y", "Y")
gratitude = "\033[42m" + "(: Thank you for using this program! :)" + "\033[0m"

# Display a welcome message
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
# Print the output
# Asking the user if they want to try it again
# If the user want to try it again 
# If the user do not want to try it again
# If the user did not input a valid answer
# Exit the loop if they do not want to try it again
# Go back to the start of the loop