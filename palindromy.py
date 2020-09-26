
def palindromy(word):
    '''
    fuction will return True if a word is a palindrome
    else False
    '''
    ##reverse = ""
    for i in range(len(word)):
        if word[i] != word[len(word) - (i +1)]:
            return False 
    return True  

print(palindromy("kajak"))
print(palindromy("test"))