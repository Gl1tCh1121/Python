alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def get_shift_key():
    while True:
        shift = input("Type the shift key: ").lower()
        if all(char in alphabet for char in shift):
            return shift
        print("Invalid shift key. Please enter letters only.")
def encryption():
    enc_dec = ""
    while enc_dec != "encode" and enc_dec != 'decode':
        enc_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if enc_dec != "encode" and enc_dec != 'decode':
            print("Type 'encode' to encrypt, type 'decode' to decrypt correctly")    
    
    message = input("Type your message: ")
    shift = get_shift_key()
    enc_message = ""
    shift_int = []
    
    for key in shift:
        if key in alphabet:  
            shift_int.append(alphabet.index(key))
        else:
            print(f"Invalid character in shift key: {key}. Only letters allowed.")
            return
        
    shift_length = len(shift_int)
    shift_index = 0

    for msg in message:
        char = msg.lower()
        if char not in alphabet:  
            enc_message += msg 
        else:
            index = alphabet.index(char)

            if enc_dec == "encode":
                new_index = (index + shift_int[shift_index]) % len(alphabet)
            else:
                new_index = (index - shift_int[shift_index]) % len(alphabet)

            if msg.isupper():
                enc_message += alphabet[new_index].upper()
            else:
                enc_message += alphabet[new_index]

            shift_index = (shift_index + 1) % shift_length


    print(f"Here's the {enc_dec}d result: {enc_message}")
    yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if yes_no == "yes":
        encryption()
    else:
        print("GoodBye")

    
encryption()


