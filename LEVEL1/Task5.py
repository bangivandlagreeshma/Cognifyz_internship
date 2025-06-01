def is_palindrome():
    s=input("Give the input:")
    if s==s[::-1]:
        print(f'{s} is a palindrome')
    else:
        print(f'"{s}" is not a palindrome')
is_palindrome()