from pygame import mixer
import time

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

SHORT_GAP = 0.3
LONG_GAP = 0.7

class Morse():
    def __init__(self):
        self.mixer = mixer.init()

    def convert_text_to_morse(self, plaintext):
        words = [word for word in plaintext.split(" ") if word.isalpha()]
        morse_result = ""
        for word in words:
            for char in word.upper():
                morse_code = CODE[char]
                morse_result += morse_code+"/"
            morse_result += " "
        return morse_result

    def convert_morse_to_text(self, cipher):
        morse_codes = [morse_code for morse_code in cipher.split("/") if morse_code.strip()]
        plaintext = ""
        for morse_code in morse_codes:
            if morse_code[0] == " ":
                morse_code = morse_code[1:]
                plaintext += " "
            plaintext += CODE_REVERSED[morse_code]
        return plaintext
                
    def convert_morse_to_sound(self):
        return 


