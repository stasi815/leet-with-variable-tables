def roman_to_int(numeral):
    """Translates a roman numeral into an integer"""
    #establish dict of roman numerals and equivalent integer values
    roman_numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    # initiate integer count
    integer_value = 0

    #for each character value in the numeral
    for i in range(len(numeral)):
        # we iterate through the string, get keys from dict
        current_key = numeral[i]
        prev_key = numeral[i-1]
        # get integer values from keys in numerals dict
        current_int = roman_numerals[current_key]
        prev_int = roman_numerals[prev_key]

        twice_prev = 2 * prev_int
        # increment value for when we have an IV, IX, etc... case
        increment = current_int - (twice_prev)
        # first if statement handles when a roman numeral is IV or IX, etc...
        if i > 0 and current_int > prev_int:
            integer_value += increment
        else:
            # otherwise the integer value increments by the value of the next roman numeral character's integer value from string
            integer_value += current_int
    return integer_value

# print(roman_to_int('MMMCMLXXXVI'))
# print(roman_to_int('MMMCMLXXXIV'))
print(roman_to_int('XXIX'))