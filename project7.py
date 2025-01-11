alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount = -shift_amount
    
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted = (index + shift_amount) % len(alphabet)
            output_text += alphabet[shifted]
        else:
            output_text += letter
    print(f"Here is the result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
