from num2words import num2words


def decorator_result(input_val):
    converted_val = num2words(float(input_val), lang='ar')
    first_section = converted_val.split(' ', 1)[0]
    if first_section == 'واحد':
        converted_val = converted_val.partition(' ')[2]
    return converted_val