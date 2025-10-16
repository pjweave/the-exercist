def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if starts_with_vowel(word) or starts_with_xr_yt(word):
            translated_words.append(word + 'ay')
        elif starts_with_consonant_then_qu(word):
            translated_words.append(transform_qu_word(word))
        elif word.startswith('qu'):
            translated_words.append(transform_qu_word(word))
        elif starts_with_consonants_then_y(word):
            translated_words.append(transform_y_word(word))
        elif not starts_with_vowel(word):
            translated_words.append(move_consonants_to_end(word) + 'ay')
        else:
            translated_words.append(word + 'ay')

    return ' '.join(translated_words)

def starts_with_consonants_then_y(word):
    word = word.lower()
    index = word.find('y')
    return index > 0 and all(c not in 'aeiou' for c in word[:index])

def starts_with_consonant_then_qu(word):
    word = word.lower()
    return word.find('qu') == 1 and word[0] not in 'aeiou'

def starts_with_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return text.lower().startswith(tuple(vowels))

def starts_with_xr_yt(text):    
    return text.lower().startswith('xr') or text.lower().startswith('yt')

def move_consonants_to_end(word):
    vowels = 'aeiouAEIOU'
    index = 0

    # Find the index of the first vowel
    while index < len(word) and word[index] not in vowels:
        index += 1

    # Rearrange the word
    return word[index:] + word[:index]

def transform_qu_word(word):
    word = word.lower()
    vowels = 'aeiou'
    index = 0

    # Find the index of the first vowel or 'qu' sequence
    while index < len(word):
        if word[index] in vowels:
            # Check if 'qu' follows the vowel
            if word[index:index+2] == 'qu':
                index += 2
            break
        elif word[index:index+2] == 'qu':
            index += 2
            break
        index += 1

    # Rearrange the word
    return word[index:] + word[:index] + 'ay'
    
def transform_y_word(word):
    word = word.lower()
    index = word.find('y')

    # Check if 'y' is present and not at the start
    if index > 0:
        return word[index:] + word[:index] + 'ay'
    else:
        # If 'y' is at the start or not found, return the word unchanged with 'ay'
        return word + 'ay'


