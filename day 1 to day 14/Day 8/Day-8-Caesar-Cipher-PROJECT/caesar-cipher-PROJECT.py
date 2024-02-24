from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text, shift, direction):
    final_text = ""
    for letter in text:
        # Only do the shift for the letters in the alphabet
        if (letter in alphabet):
            index = alphabet.index(letter)
            if (direction == "encode"):
                index += shift
                while index >= len(alphabet):
                    if index >= len(alphabet):
                        index = index - len(alphabet)
            elif (direction == "decode"):
                index -= shift
                while index < 0:
                    if index < 0:
                        index = index + len(alphabet)

            final_text += alphabet[index]
        else:
            final_text += letter
    print(f"Here's the {direction}d result: {final_text}")


print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    continue_the_game = input(
        "\nShould we continue the game? Type 'yes' or 'no'.\n").lower()
    if (continue_the_game != "yes"):
        print("\nGoodbye")
        break
