from pygame import mixer
from morse import Morse
import time

SHORT_GAP = 0.3
LONG_GAP = 0.7


def make_short_beep():
    mixer.init()
    mixer.music.load("./sounds/morse-short-beep.mp3")
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    
def make_long_beep():
    mixer.init()
    mixer.music.load("./sounds/morse-long-beep.mp3")
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue

def make_short_gap():
    time.sleep(SHORT_GAP)

def make_long_gap():
    time.sleep(LONG_GAP)


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

print("\n**************************\nWelcome to the Text to Morse Code Converter\nThis program is used to convert given input to morse code and play corresponding sound\n**************************\n")
plaintext = input("Please enter the text which you want to convert to morse code: ")

morse = Morse()
morse_result= morse.convert_morse_to_text(plaintext)

print(f"Your message in morse code is {morse_result}")
