def next_number(number: str):
    """Helper function that is called in count_and_say function to generate the next number"""

    result = []
    num_len = len(number)
    start = number[0]
    count = 0
    for i in range(num_len):
        if number[i] == start:
            count += 1
        if number[i] != start:
            result.append(str(count))
            result.append(start)
            start = number[i]
            count = 1
    result.append(str(count))
    result.append(start)
    return ''.join(result)

def count_and_say(num: int):
    """If the number is greater than 1, we call the next_number function to create the count and say string and keep iterating"""
    i = 0
    number = '1'
    if num == 1:
        return '1'
    while i < num-1:
        number = next_number(number)
        i = i + 1
    return number

print(count_and_say(3))