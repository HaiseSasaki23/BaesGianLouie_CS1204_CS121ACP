def caesar_decrypt(shift,text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base )
        else:
            decrypted_text += char
    return decrypted_text

input_data = input("Enter cipher: ").split()

for item in input_data:
    shift = int(item[0])
    text = item[1:]
    print (caesar_decrypt(shift, text), end = " ")