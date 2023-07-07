# Create a function that will express Hello World in ascii art
def hello_world():
    helloworld = "H     H  EEEEE  L       L       OOO   \n" \
                 "H     H  E      L       L      O   O  \n" \
                 "HHHHHHH  EEE    L       L      O   O  \n" \
                 "H     H  E      L       L      O   O  \n" \
                 "H     H  EEEEE  LLLLL   LLLLL   OOO   \n" \
                 "\n" \
                 "W       W    OOO    RRRRR   L       DDDDD   \n" \
                 "W       W  O     O  R    R  L       D    D  \n" \
                 "W   W   W  O     O  RRRRR   L       D     D \n" \
                 "W   W   W  O     O  R   R   L       D    D  \n" \
                 " W W W W    OOOOO   R    R  LLLLL   DDDDD   "
    print(helloworld)


# Prompts the user for a yes/no response to say hello world, goodbye world, or check for error conditions
# There is likely a better way to express this logic, probably with dictionaries or key:value, to be revised in next version

loop = True                 #boolean condition for the main outer while loop
error_loop = True           #boolean condition for the outer (error) inner while loop

while loop:
    answer = input("Would you like to say hello to the world? (Y/N): ").lower()
    if answer == "yes" or answer == "y":
        hello_world()
        loop = False
    elif answer == "no" or answer == "n":
        print("Goodbye World!")
        loop = False
    else:
        while error_loop:
            print("Yes (Y) or No (N) only: ")
            error_answer = input().lower()
            if error_answer == "yes" or error_answer == "y":
                hello_world()
                loop = False
                error_loop = False
            elif error_answer == "no" or error_answer == "n":
                print("Goodbye World!")
                loop = False
                error_loop = False
            else:
                error_loop





    


    

