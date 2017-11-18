# Find the largest palindrome made from the product of two 3-digit numbers.


# going the easy string route...easy to read, easy to maintain, easy to understand
def isPalindrome(n):
    m = str(n)
    if( m == m[::-1] ):
        return True;
    else:
        return False;

a = 100
b = 100
largest = 0

while a <= 999:
    while b <= 999:
        product = a * b;
        if(isPalindrome(product) == True):
            if(product > largest): largest = product
        b = b + 1
    a = a + 1
    b = 100

print(largest)


