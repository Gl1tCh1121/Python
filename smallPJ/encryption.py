alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("""
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[   "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88   
""")

# def encryption():
#     enc_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:")

#     if enc_dec == "encode":
#         message = input("Type your message:")
#         shift = int(input("Type the shift number:"))
#         enc_message = ""
#         shift %= 26

#         for i in range(len(message)):
#             if alphabet.index(message[i]) + shift > 25:
#                 letter = alphabet[alphabet.index(message[i]) + shift - 26] 
#             else:
#                 letter = alphabet[alphabet.index(message[i]) + shift] 
#             enc_message += letter

#         print(f"Here's the encoded result: {enc_message}")
#         yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
#         if yes_no == "yes":
#             encryption()
#         else:
#             print("GoodBye")

#     else:
#         message = input("Type your message:")
#         shift = int(input("Type the shift number:"))
#         enc_message = ""
#         shift %= 26

#         for i in range(len(message)):
#             if alphabet.index(message[i]) - shift < 0:
#                 letter = alphabet[alphabet.index(message[i]) - shift + 26] 
#             else:
#                 letter = alphabet[alphabet.index(message[i]) - shift] 
#             enc_message +=  letter

#         print(f"Here's the decoded result: {enc_message}")

#         yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
#         if yes_no == "yes":
#             encryption()
#         else:
#             print("GoodBye")

# encryption()


def encryption():
    enc_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:")

    
    message = input("Type your message:")
    shift = int(input("Type the shift number:"))
    enc_message = ""

    if enc_dec == "decode":
        shift *= -1

    for char in message:
        if char not in alphabet:
            enc_message += char
        else:
            index = alphabet.index(char) + shift
            index %= len(alphabet) 
            enc_message += alphabet[index]

    print(f"Here's the encoded result: {enc_message}")
    yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if yes_no == "yes":
        encryption()
    else:
        print("GoodBye")

    
encryption()


