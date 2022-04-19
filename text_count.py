import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
punct = string.punctuation

while True:
    print()
    ch = input("Do you want to get the counts of all the characters in the text : Y/N --- ")
    
    print()
    print("---------------------------------------------------------------------------------")
    print()
    

    if ch.upper() == 'Y':
        
        s = input("Enter the text : ")

        print()
        print("---------------------------------------------------------------------------------")
        print()

        upper_char = 0
        lower_char = 0
        digit_char = 0
        punct_char = 0
        space = 0
        length = len(s)

        for i in s:
            if i in upper:
                upper_char += 1

            elif i in lower:
                lower_char += 1

            elif i in num :
                digit_char += 1

            elif i in punct:
                punct_char += 1
            else:
                space += 1

                

    elif ch.upper() == 'N':
        
        print("Thank You")
        print()
        print("---------------------------------------------------------------------------------")
        print()
        break

    else:
        print("Invalid choice")
        print()
        print("---------------------------------------------------------------------------------")
        print()



    
    print("Length : ",length)
    print("Upper Characters : ",upper_char)
    print("Lower Characters : ",lower_char)
    print("Lower Characters : ",punct_char)
    print("Digits : ",digit_char)
    print("Space : ", space)

    print()
    print("---------------------------------------------------------------------------------")
    print()
