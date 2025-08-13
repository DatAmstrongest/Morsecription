from pydub import AudioSegment

CODE = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',

    # Digits
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    # Punctuation (common ITU / widely used)
    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',  "'": '.----.',
    '!': '-.-.--',  '/': '-..-.',   '(': '-.--.',   ')': '-.--.-',
    '&': '.-...',   ':': '---...',  ';': '-.-.-.',  '=': '-...-',
    '+': '.-.-.',   '-': '-....-',  '_': '..--.-',  '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',
}

CODE_REVERSED = {value:key for key,value in CODE.items()}

SHORT_GAP = 300
LONG_GAP = 700

def check_word(word):
    for char in word.upper():
        if char not in CODE: 
            raise Exception(f"{word} is not in valid format")
    return True

class Morse():
    def __init__(self):
        self.long_beep = AudioSegment.from_file("./sounds/morse-long-beep.mp3", format="mp3")
        self.short_beep = AudioSegment.from_file("./sounds/morse-short-beep.mp3", format="mp3")
        self.short_gap = AudioSegment.silent(duration=SHORT_GAP)
        self.long_gap = AudioSegment.silent(duration=LONG_GAP)

    def convert_text_to_morse(self, plaintext):
        if len(plaintext)>200:
            raise Exception("Plaintext cannot be bigger than 200 characters.")
        words = [word for word in plaintext.split(" ") if check_word(word)]
        morse_result = ""
        for word in words:
            for char in word.upper():
                morse_code = CODE[char]
                morse_result += morse_code+"/"
            morse_result += " "
        self.convert_morse_to_sound(plaintext)
        return morse_result

    def convert_morse_to_text(self, cipher):
        if len(cipher)>200:
            raise Exception("Ciphertext cannot be longer than 200 characters.")
        morse_codes = [morse_code for morse_code in cipher.split("/") if morse_code.strip()]
        plaintext = ""
        for morse_code in morse_codes:
            if morse_code[0] == " ":
                morse_code = morse_code[1:]
                plaintext += " "
            plaintext += CODE_REVERSED[morse_code]
        return plaintext
                
    def convert_morse_to_sound(self, cipher):
        morse_codes = [morse_code for morse_code in cipher.split("/") if morse_code.strip()]
        combined = self.short_gap
        for morse_code in morse_codes:
            if morse_code[0] == " ":
                morse_code = morse_code[1:]
                combined += self.long_gap
            for char in morse_code:
                if char == ".":
                    combined += self.short_beep
                else:
                    combined += self.long_beep
            combined += self.short_gap
        combined += self.short_gap
        return combined



