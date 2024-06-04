from morse import Morse

print("\n**************************\nWelcome to the Text to Morse Code Converter\nThis program is used to convert given input to morse code and play corresponding sound\n**************************\n")
plaintext = input("Please enter the text which you want to convert to morse code: ")

morse = Morse()
morse_result= morse.convert_morse_to_sound(plaintext)

print(f"Your message in morse code is {morse_result}")
