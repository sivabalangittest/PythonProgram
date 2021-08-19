# Function to validate Password Format
def password_format(input_password):

    # Declaration of variables
    letter = 0
    number = 0
    special_character = 0
    not_allowed_special_character = 0

    if 8 <= len(input_password) <= 20:
        for char in input_password:
            # count letter
            if char.isalpha():
                letter += 1
            # count number
            if char.isnumeric():
                number += 1
            # count allowed special character @ and !
            if char == '@' or char == '!':
                special_character += 1
            # count unallowed special character
            if char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*':
                not_allowed_special_character += 1

    if letter >= 1 and number >= 1 and special_character >= 1 and not_allowed_special_character == 0:
        print('Password is in valid format')

    else:
        print('Password is in invalid format')


password_format('a1@sdeqw')

