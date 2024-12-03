import time
import board
import neopixel

morse_code = {
      'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',


    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

def clear_sentence(sentence):
    return ''.join(c for c in sentence.lower() if c in morse_code or c == ' ')

def to_morse(sentence):
    return [' '.join(morse_code[char] for char in word) for word in sentence.split()]

def display_signal(color, duration):
    pixels.fill(color)
    time.sleep(duration)
    pixels.fill((0, 0, 0))
    time.sleep(duration)

def display_morse(morse_list, unit):
    for word in morse_list:
        for char in word.split():
            for symbol in char:
                display_signal((0, 0, 255) if symbol == '.' else (0, 255, 0), unit if symbol == '.' else 3 * unit)
            time.sleep(2 * unit)
        time.sleep(4 * unit)

def main():
    while True:
        try:
            unit = float(input("Enter unit length (0 < unit ≤ 1): "))
            if 0 < unit <= 1:
                break
        except ValueError:
            print("try again")
    sentence = clear_sentence(input("Enter a sentence: "))
    morse_list = to_morse(sentence)
    print("\nDisplaying Morse code...")
    display_morse(morse_list, unit)
    print("Done!")

if __name__ == "__main__":
    main()
