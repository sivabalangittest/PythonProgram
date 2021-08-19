# countAs
# Write a function that takes 2 inputs:
# string - number of characters to observe Return the number of 'a' in the string up to the number of characters.
# Example 1: countAs('ababczzzzzzzaaa', 3) -> 2 a's
# Example 2: abaa has 3 input 2: 7 countAs('abaa', 7) --> return 5 abaaaba -> 5 a's


def count_as(input_string, input_length):
    count = 0
    for index in range(input_length):
        if input_string[index] == 'a':
            count += 1
    print("The no.of 'a' in given string is " + str(count))


count_as('aaabczzzzzzzaaa', 3)


def count_as(input_string1, input_string2, input_length):
    count = 0
    string1_length = len(input_string1)

    if string1_length >= input_length:
        for index in range(input_length):
            if input_string1[index] == 'a':
                count += 1
    else:
        concatenate_string = input_string1 + input_string2
        concatenate_string_length = len(concatenate_string)
        for index in range(concatenate_string_length):
            if concatenate_string[index] == 'a':
                count += 1

    print("The no.of 'a' in given string is " + str(count))


count_as('a', 'aabczaz', 7)