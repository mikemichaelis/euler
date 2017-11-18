# Find the largest palindrome made from the product of two 3-digit numbers.


# going the easy string route...easy to read, easy to maintain, easy to understand, easy to code.....
def isPalindrome(n):
    m = str(n)
    return m == m[::-1]

a = 100
b = 100
largest = 0

# start with largest numbers first to exclude calling isPalindrome() for smaller products
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        product = a * b
        # check the product is larger than current largest
        if(product > largest):
            if(isPalindrome(product) == True):
                largest = product

print(largest)