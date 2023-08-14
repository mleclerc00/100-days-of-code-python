alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(input, shift_amount, cipher_direction):
  output = ""
  if direction == "decode":
      shift_amount *= -1
  for letter in input:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    output += alphabet[new_position]
  print(f"The {cipher_direction}d text is {output}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(input=text, shift_amount=shift, cipher_direction=direction)