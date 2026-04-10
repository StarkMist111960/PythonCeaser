input_string = input('Enter string to decrypt: ')
input_key = int(input('Enter key: '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

if input_key < 0 or input_key > 25:
    print('Invalid key value, must be between 0 and 25')    
else:    decrypted_string = ''
for char in input_string:           
        if char in alphabet:
            index = (alphabet.index(char) - input_key) % 26
            decrypted_string += alphabet[index]
        else:
            decrypted_string += char
print('Decrypted string:', decrypted_string)
