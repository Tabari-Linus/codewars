def is_valid_IP(strng):
    
    number_dots = strng.count('.')
    number_list = strng.split('.')
    if number_dots != 3 and len(number_list) != 4:
        return False
    
    for num in number_list:
        if not num.isdigit():
            return False
        if int(num) > 255 or int(num) < 0:
            return False
        if len(num) > 1 and num[0] == '0':
            return False
    return True