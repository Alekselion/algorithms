def isPrime(num):
    """ Check if number is prime. 
        Return true if number is prime else false.
    """
    if num < 1:
        return False

    d = 2
    while d * d <= int(num) and int(num) % d != 0:
        d += 1
    return d * d > int(num)


def isEven(num):
    """ Check if number is even. 
        Return true if number is even else false.
    """
    return int(num) & 1 == 0
    

def isPalindrome(arr):
    """ Check if arr is palindrome.
        Return true if iterable object is palindrome else false.
    """
    return str(arr) == str(arr)[::-1]


def isPandigital(num):
    """ Check if number is pandigital. 
        Return true if number is pandigital else false. 
    """
    for i in [str(x) for x in range(10)]:
        if i not in list(str(num)):
            return False
    return True


if __name__ == "__main__":
    n1, n2 = 10, 11
    print(f"Prime:\n\tinp {n1}, {n2}\n\tout {isPrime(n1)}, {isPrime(n2)}")
    print(f"Even:\n\tinp {n1}, {n2}\n\tout {isEven(n1)}, {isEven(n2)}")
    
    n1, n2 = 12312, 1221
    print(f"Palindrome:\n\tinp {n1}, {n2}\n\tout {isPalindrome(n1)}, {isPalindrome(n2)}")

    n1, n2 = 118395726, 1234567890
    print(f"Pandigital:\n\tinp {n1}, {n2}\n\tout {isPandigital(n1)}, {isPandigital(n2)}")
