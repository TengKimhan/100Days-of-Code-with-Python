from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if (encode_or_decode == "decode"):
            shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"The output text is {output_text}")

run = True
while run:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % 26

  caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
  
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ").lower()
  if choice == 'no':
    run = False
    print("Goodbye.")

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift_amount) % 26
#             cipher_text += alphabet[new_position]
#         else:
#             cipher_text += letter
#     return cipher_text

# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#     for letter in cipher_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift_amount) % 26
#             original_text += alphabet[new_position]
#         else:
#             original_text += letter
#     return original_text