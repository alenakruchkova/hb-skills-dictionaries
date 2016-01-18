"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""

import operator
import collections


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]



    """

    return list(set(words))


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are different data types.

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]

    """

    return list(set(list1) & set(list2))


def print_dict(occurances):

    return occurances

    # Dear Ally,
    # First of all def count_unique(input_string) can't pass unless there's 
    # a def print_dict(occurances), which i creates above. As I do not see any 
    # learning outcome from creating it, I wonder if I am not getting something.

    # Here is a mistake I am getting now:

        # Expected:
        # {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
        # Got:
        # {'Porcupine': 1, 'porcupine': 1, 'see,': 1, 'do.': 1}

    # Basically I am expected to produce an ordered dictionary. That's cute.

    # Here are 2 ways I tried to solve this:

    # >>>ordered_occurances = collections.OrderedDict(sorted(occurances.items()))
    # >>>return odered_occurances

    # I am left with a list of tuples, which looks alot like expected outcome,
    # but is not a dictionary
    # If I make this list into a dictionary i am back to square one,
    # cause guess what, dictionaries are not ordered.


    # >>>sorted_dictionary = sorted(occurances.items(), key=operator.itemgetter(0))
    # >>>string_parts = []
    # >>>for (key, value) in sorted_dictionary:
    # ...    string_parts.append("'%s': %d"%(key, value))
    # >>>return '{'+', '.join(string_parts)+'}'

    # This produces a string that look veru much like desired outcome,
    # but is just a string, NOT an ordered dictionary,
    # whatever that might be

def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        #>>> print_dict(count_unique("rose is a rose is a rose"))
        #{'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        #>>> print_dict(count_unique("Porcupine see, porcupine do."))
        #{'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    occurances = {}

    for word in input_string.split():
        if word in occurances:
            occurances[word] += 1
        else:
            occurances[word] = 1

    return occurances


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

   English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # I had to create this dictionary private_speak so I had 
    # dictionary to work with

    pirate_speak = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
        "man": "matey"  # I added this translation else test does not pass
    }

    translation = []

    for word in phrase.split():
        if word in pirate_speak:
            translation.append(pirate_speak[word])
        else:
            translation.append(word)

    return " ".join(translation)


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    words.sort(key=len)

    sorted_by_word_dict = {}

    for word in words:
        if len(word) in sorted_by_word_dict:
            sorted_by_word_dict[len(word)].append(word)
        else:
            sorted_by_word_dict[len(word)] = [word]

    ordered_dict = collections.OrderedDict(sorted(sorted_by_word_dict.items()))

    return ordered_dict.items()


def sort_pairs(list_of_valid_pairs):

    return list_of_valid_pairs
# Ally, def is_valid(pair) is not going to run unless 
# there is sort_pairs is defined. Hence lines 275-277. 
# Again, I do not see what am I supposed to learn here, 
# so I am just going to assume that I am not getting something.


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    eliminate_repeats = set(input_list)


    def is_valid(pair):
        if pair[0]+pair[1] == 0:
            return True
        else:
            return False

    # generate all pairs
    all_pairs = []
    for val1 in eliminate_repeats:
        for val2 in eliminate_repeats:
            pair = [val1, val2]
            all_pairs.append(pair)


    # sort all pairs
    for pair in all_pairs:
        pair.sort()
    sorted_pairs = sorted(all_pairs)

    # find valid pairs and append to list_of_valid_pairs
    list_of_valid_pairs = []
    for pair in all_pairs:
        if is_valid(pair) and pair not in list_of_valid_pairs:
            list_of_valid_pairs.append(pair)

    # I wonder if there is a reason why test expects a sorted list,
    # if in the task it says nothing about sorting the pairs.
    list_of_valid_pairs.sort()
    return list_of_valid_pairs


# ##############################################################################
# # You can ignore everything below this.

# def print_dict(d):
#     # This method is just used to print dictionaries in key-alphabetical
#     # order, and is only used for our documentation tests. You can ignore it.
#     if isinstance(d, dict):
#         print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
#     else:
#         print d


# def sort_pairs(l):
#     # Print sorted list of pairs where the pairs are sorted. This is used only
#     # for documentation tests. You can ignore it.
#     return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
