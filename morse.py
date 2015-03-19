
def encode_morze(text):

    morse_code = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--.."
    }

    def get_words(text):
        text = str(text).upper()
        words = []
        buffer = ''

        for i in text:
            if i in morse_code:
                buffer += i
            elif i == '-':
                None
            else:
                if len(buffer) > 0:
                    words.append(buffer)
                    buffer = ''

        if len(buffer) > 0:
            words.append(buffer)
            buffer = ''

        return words

    def sign_to_morse(sign):
        result = ''
        len_sign = len(sign)

        for i in range(len_sign):
            if i > 0:
                result += '_'

            if sign[i] == '.':
                result += '^'
            elif sign[i] == '-':
                result += '^^^'

        return result

    def word_to_morse(word):
        result = ''
        len_word = len(word)

        for i in range(len_word):
            if i > 0:
                result += '___'

            sign = morse_code.get(word[i])
            result += sign_to_morse(sign)

        return result

    def sentence_to_morse(sent):
        result = ''
        len_sent = len(sent)

        for i in range(len_sent):
            if i > 0:
                result += '_______'

            result += word_to_morse(sent[i])

        return result

    words = get_words(text)
    morse = sentence_to_morse(words)
    return morse

print(encode_morze('Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'))