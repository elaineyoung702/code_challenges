"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    #if length of word is odd number (mod% == 1)
    #dict shoudl have values of 2 for all keys except 1

    #if length of word is even mod%==0
    #dict should have values of 2 for all keys return True

    letter_dict = {}

    if not word:
        return False

    if len(word) % 2 == 1:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                del letter_dict[letter]
        if len(letter_dict) > 1:
            return False
        else:
            return True

    else:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                del letter_dict[letter]
        if len(letter_dict) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
