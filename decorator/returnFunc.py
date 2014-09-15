def surround_with(surrounding):
    import pdb;pdb.set_trace()
    """Return a function that takes a single argument and."""
    def surround_with_value(word):
        return '{0}{1}{2}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    import pdb;pdb.set_trace()
    """Return a string based on *content* but with each occurrence 
    of words in *targets* replaced with
    the result of applying *transform* to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {0}'.format(transform(word))
        else:
            result += ' {0}'.format(word)
    return result
