# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Example input: 'read'
# Example output: 'reading'
def verbing(s):
    if len(s) < 3:
        return s
    if s[-3:] == 'ing':
        return s + 'ly'
    return s + 'ing'


# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
#
# Example input: 'This dinner is not that bad!'
# Example output: 'This dinner is good!'
def not_bad(s):
    not_pos = s.find('not')
    bad_pos = s.find('bad')
    if  not_pos != -1  and bad_pos != -1 and not_pos < bad_pos:
        return s[:not_pos] + 'good' + s[bad_pos + 3:]
    return s


# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
#
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Example input: 'abcd', 'xy'
# Example output: 'abxcdy'
def str_divider(s):
    half_len = (len(s) + 1) // 2
    return (s[:half_len], s[half_len:])

def front_back(a, b):
    a_halves = str_divider(a)
    b_halves = str_divider(b)
    return a_halves[0] + b_halves[0] + a_halves[1] + b_halves[1]
