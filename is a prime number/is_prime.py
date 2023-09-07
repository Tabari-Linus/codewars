def is_prime(num):
    if num <= 1:
        return False
    else:
        if num < 0:
            num = -num
        
        if num <= 3:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True
