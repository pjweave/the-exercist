"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
    by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    # Apply prefix to each word in the list (excluding the prefix itself)
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    # Combine prefix and prefixed words into a single string
    return ' :: '.join([prefix] + prefixed_words)  


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - word to remove suffix from.
    :return: str - word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word.endswith("ness"):
        root = word[:-4]  # remove 'ness'
        # Handle spelling adjustment: if root ends in 'i', replace with 'y'
        if root.endswith("i"):
            root = root[:-1] + "y"
        return root
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    word = words[index].strip('.,!?')  # Remove punctuation
    return word + 'en'
