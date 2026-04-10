alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_string = input('Enter string to encrypt: ')
input_key = int(input('Enter key: '))

if input_key < 0 or input_key > 25:
    print('Invalid key value, must be between 0 and 25')
else:
    encrypted_string = ''
    for char in input_string:
        if char in alphabet:
            index = (alphabet.index(char) + input_key) % 26
            encrypted_string += alphabet[index]
        else:
            encrypted_string += char
    print('Encrypted string:', encrypted_string)
