dictionary_morse_code = {
      'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',


    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}



def clear_sentence(sentence):
    return ''.join(c for c in sentence.lower() if c in dictionary_morse_code or c == ' ')

def to_morse(sentence):
    return [' '.join(dictionary_morse_code[char] for char in word) for word in sentence.split()]

def format_morse(list):
    return '  '.join(list)

def main():
    sentence = input("Enter a sentence: ")
    argument = argument(sentence)
    morse_list = to_morse(argument)
    m_formatted = format_morse(morse_list)
    print("\nMorse Code Equivalent:")
    print(m_formatted)

if __name__ == "_main_":
    main()fiNL








    





