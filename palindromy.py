
def palindromy(word):
    '''
    fuction will return True if a word is a palindrome
    else False
    '''
    reverse = ""
    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]
    if word == reverse:
        return True
    else:
        return False
palindromy("kajakz")
