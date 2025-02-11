def to_camel_case(text):
    values = text.replace('-', ' ').replace('_', ' ').split()
    for i in range(1, len(values)):
        values[i] = values[i].capitalize()
    return ''.join(values)


print(to_camel_case("the-stealth-warrior"))