
def trim_text(text):
    modified_text = text.replace('\n', '')
    trimmed_text = modified_text.strip()

    return trimmed_text

def get_text_value(element, options=[], replace=None):
    if element != None:

        value = element.text

        encode_values = {
            '\u2013': '-',
            '\u2019': "'"
        }

        for code,char in encode_values.items():
            value = value.replace(code, char)

        if "strip" in options:
            replace_values = [
                '\u21e7',
                '\u00b7\u00a0',
                '\u2026see more',
            ]
            
            for string in replace_values:
                value = value.replace(string, '')

            if replace != None:
                value = value.replace(replace, '')

        value = trim_text(value)

        return value
    else:
        return element

def get_attribute_value(element, attribute):
    if element != None:
        return element[attribute]
    else:
        return element
    
def parse_address(unparsed_address):
    if unparsed_address != None:
        parsed_address = unparsed_address.split(', ')
    else:
        parsed_address = []

    country = None
    state = None
    city = None

    for i in range(len(parsed_address)):
        if i == 0:
            city = parsed_address[i]
        if i == 1:
            state = parsed_address[i]
        if i == 2:
            country = parsed_address[i]

    return city, state, country

def get_digits(string):
    import re

    digits_string = re.findall(r'\d', string)

    digits = ''.join(digits_string)

    return digits
