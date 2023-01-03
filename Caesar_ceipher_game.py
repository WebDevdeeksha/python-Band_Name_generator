alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
end_of_game = True

def caesar(text, shift_no, cipher_dr):
    new_msg = ""
    if(cipher_dr=='decoding'):
        shift_no *= -1

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_no
        new_msg += alphabet[new_position]
    print(new_msg)

while end_of_game:
    msg = input("Enter message to perform the operation: \n")
    shift_amount = int(input("Enter shift number: "))
    shift_amount = shift_amount%26
    operation = input("Which operation u want to perform 'ENCODE' or 'DECODE' type 'encoding' or 'decoding': ").lower()
    caesar(text=msg, shift_no=shift_amount, cipher_dr=operation)

    choice = input("do u want to continue type 'yes' or 'no'.")
    if(choice=='no'):
        end_of_game = False
        print("Good Bye! :)")
