
def find_most_frequent(text):

    abc = 'abcdefghijklmnopqrstuvwxyz'

    def get_words(text):
        text = str(text).lower()
        words = []
        buffer = ''

        for i in text:
            if i in abc:
                buffer += i
            else:
                if len(buffer) > 0:
                    words.append(buffer)
                    buffer = ''

        if len(buffer) > 0:
            words.append(buffer)
            buffer = ''

        return words

    words = get_words(text)
    dc_words = {}
    most_words = []
    max_value = 0

    for word in words:
        value = dc_words.get(word)

        if value is None:
            value = 1
        else:
            value += 1

        dc_words.__setitem__(word, value)
        max_value = max(max_value, value)

    for dc_key in dc_words:
        if dc_words[dc_key] == max_value:
            most_words.append(dc_key)

    most_words.sort()
    return most_words

print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))
