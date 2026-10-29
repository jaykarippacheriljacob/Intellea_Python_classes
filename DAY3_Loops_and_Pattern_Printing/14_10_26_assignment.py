# Level 1 — Basic patterns
""" 
    1. Solid square
    Input: n = 4
    * * * *
    * * * *
    * * * *
    * * * *
"""
n = int(input("1. Enter n for Solid square: ") or 4)
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()

""" 
    2. Right-angled triangle
    Input: n = 5
    *
    * *
    * * *
    * * * *
    * * * * * 
"""
n = int(input("2. Enter n for Right-angled triangle: ") or 5)
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()

""" 
    3. Inverted triangle
    Input: n = 5
    * * * * *
    * * * *
    * * *
    * *
    *
"""
n = int(input("3. Enter n for Inverted triangle: ") or 5)
for i in range(n):
    for j in range(n-i):
        print("*", end = " ")
    print()

""" 
    4. Increasing number triangle
    Input: n = 5
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""
n = int(input("4. Enter n for Increasing number triangle: ") or 5)
for i in range(n):
    for j in range(1, i + 2):
        print(j, end = " ")
    print()

""" 
    5. Repeated row numbers
    Input: n = 5
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
"""
n = int(input("5. Enter n for Repeated row numbers: ") or 5)
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end = " ")
    print()

# Level 2 — Intermediate interview patterns
""" 
    6. Right-aligned triangle
    Input: n = 5
            *
          * *
        * * *
      * * * *
    * * * * *
"""
n = int(input("6. Enter n for Right-aligned triangle: ") or 5)
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()

""" 
    7. Continuous number triangle
    Input: n = 5
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
"""
n = int(input("7. Enter n for Continuous number triangle: ") or 5)
count = 0
for i in range(n):
    for j in range(i + 1):
        count += 1
        print(count, end = " ")
    print()

""" 
    8. Alternating binary triangle
    Input: n = 5
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
"""
n = int(input("8. Enter n for Alternating binary triangle: ") or 5)
for i in range(n):
    if i % 2 == 0:
        checker = True
    else:
        checker = False
    for j in range(i + 1):
        if checker:
            print(1, end = " ")
            checker = False
        else:
            print(0, end = " ")
            checker = True
    print()

""" 
    9. Hollow square
    Input: n = 5
    * * * * *
    *       *
    *       *
    *       *
    * * * * *
"""
n = int(input("9. Enter n for Hollow square: ") or 5)
for i in range(n):
    if i == 0 or i == n-1:
        for j in range(n):
            print("*", end = " ")
    else:
        print("*", end = " ")
        for j in range(n - 2):
            print(" ", end = " ")
        print("*", end = " ")
    print()
        
""" 
    10. Alphabet triangle
    Input: n = 5
    A
    A B
    A B C
    A B C D
    A B C D E
"""
n = int(input("10. Enter n for Alphabet triangle: ") or 5)
for i in range(n):
    l = "A"
    for j in range(i + 1):
        print(chr(ord(l) + j), end = " ")
    print()

# Level 3 — Placement practice
""" 
    11. Full pyramid
    Input: n = 5
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
"""
n = int(input("11. Enter n for Full pyramid: ") or 5)
odd = 1
"""
    # # # # *
    # # # * * *
    # # * * * * *
    # * * * * * * *
    * * * * * * * * *
"""
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(odd):
        print("*", end = " ")
    print()
    odd += 2

""" 
    12. Inverted full pyramid
    Input: n = 5
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
"""
n = int(input("12. Enter n for Inverted full pyramid: ") or 5)
odd = 1 + 2 * (n - 1)
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(odd):
        print("*", end = " ")
    print()
    odd -= 2

""" 
    13. Diamond pattern
    Input: n = 4
          *
        * * *
      * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
"""
n = int(input("13. Enter n for Diamond pattern: ") or 4)
odd = 1
for i in range(n):
    for j in range(n - i -1):
        print(" ", end = " ")
    for j in range(odd):
        print("*", end = " ")
    print()
    odd += 2
odd -= 4
for i in range(n-1):
    for j in range(i + 1):
        print(" ", end = " ")
    for j in range(odd):
        print("*", end = " ")
    print()
    odd -= 2

""" 
    14. Hollow right-angled triangle
    Input: n = 5
    *
    * *
    *   *
    *     *
    * * * * *
"""
n = int(input("14. Enter n for Hollow right-angled triangle: ") or 5)
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(i + 1):
            print("*", end = " ")#
    else:
        for j in range(i + 1):
            if j == 0 or j == i:
                print("*", end = " ")
            else:
                print(" ", end = " ")
    print()


""" 
    15. Floyd's triangle
    Input: n = 5
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
"""
n = int(input("15. Enter n for Floyd's triangle: ") or 5)
count = 0
for i in range(n):
    for j in range(i + 1):
        count += 1
        print(count, end = " ")
    print()

# Level 4 — Logic-building challenges
""" 
    16. Palindrome number pyramid
    Input: n = 5
        1
       121
      12321
     1234321
    123454321
"""
n = int(input("16. Enter n for Palindrome number pyramid: ") or 5)
"""
    ####1
    ###121
    ##12321
    #1234321
    123454321
"""
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = "")
    ptr = 0
    for j in range(i + 1):
        ptr += 1
        print(ptr, end = "")    
    for j in range(i):
        ptr -= 1
        print(ptr, end = "")
    print()

""" 
    17. Butterfly pattern
    Input: n = 4
    *             *
    * *         * *
    * * *     * * *
    * * * * * * * *
    * * *     * * *
    * *         * *
    *             *
"""
n = int(input("17. Enter n for Butterfly pattern: ") or 4)
for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    for j in range(2 * (n - i - 1)):
        print(" ", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()
"""
    * 1 1 1 1 1 1 *
    * * 1 1 1 1 * *
    * * * 1 1 * * *
    * * * * * * * *
    * * * 1 1 * * *
    * * 1 1 1 1 * *
    * 1 1 1 1 1 1 *
"""
for i in range(n - 1):
    for j in range(n - i - 1):
        print("*", end = " ")
    for j in range(2 * (i + 1)):
        print(" ", end = " ")
    for j in range(n - i - 1):
        print("*", end = " ")
    print()

""" 
    18. Hollow pyramid
    Input: n = 5
            *
          *   *
        *       *
      *           *
    * * * * * * * * *
"""
n = int(input("18. Enter n for Hollow pyramid: ") or 5)
odd = 1
"""
    # # # # *
    # # # *   *
    # # *       *
    # *           *
    * * * * * * * * *
"""
for i in range(n):
    if i == n - 1:
        for j in range(odd):
            print("*", end = " ")
    else:
        for j in range(n - i - 1):
            print(" ", end = " ")
        for j in range(odd):
            if j == 0 or j == odd - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
    print()
    odd += 2

""" 
    19. Number pyramid
    Input: n = 5
            1
          1 2 1
        1 2 3 2 1
      1 2 3 4 3 2 1
    1 2 3 4 5 4 3 2 1
"""
n = int(input("19. Enter n for Number pyramid: ") or n)
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    ptr = 0
    for j in range(i + 1):
        ptr += 1
        print(ptr, end = " ")    
    for j in range(i):
        ptr -= 1
        print(ptr, end = " ")
    print()
""" 
    20. X pattern
    Input: n = 5
    *       *
      *   *
        *
      *   *
    *       *
"""
n = int(input("20. Enter n for X pattern: ") or 5)
"""
    * 7 7 7 *
    0 * 7 *
    0 0 *
    0 * 7 *
    * 7 7 7 *
"""
odd = n
reverse = False
for i in range(n):
    if not reverse:
        for j in range(i):
            print(" ", end = " ")
        for j in range(odd):
            if j == 0 or j == odd - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        odd -= 2
    else:
        indent = n - 1 - i
        # n = left blanks + width + right blanks
        # n = indent + width + indent
        # width = n - 2 × indent
        # width = n - 2 × (n - 1 - i)
        #       = n - 2n + 2 + 2i
        #       = 2i - n + 2
        width = n - 2 * indent
        for j in range(indent):
            print(" ", end = " ")
        for j in range(width):
            if j == 0 or j == width - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
    if odd <= 0:
        reverse = True
    
    print()
