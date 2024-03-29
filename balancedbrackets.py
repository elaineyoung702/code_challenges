"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    open_brackets = set("([{<")
    close_brackets = set(")}]>")

    # Creating a dict for fast searching.
    # Key is closing bracket to look up open bracket
    bracket_pairs = {
      ")" : "(",
      "}" : "{",
      "]" : "[",
      ">" : "<",
    }

    # Creating a stack/Python list to track
    seen_brackets = []

    for char in phrase:

      if char in open_brackets:
        seen_brackets.append(char)

      elif char in close_brackets:
        if not seen_brackets:
          return False

        else:
          if seen_brackets[-1] == bracket_pairs[char]:
            seen_brackets.pop()

          else:
            return False

    if not seen_brackets:
      return True

    else:
      return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
