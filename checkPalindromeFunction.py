def check_palindrome(words):

    def is_palindrome(word): # function that check if a word is a palindrome or not

        word = word.lower()
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    results = {} # new dictionary for each word we update its boolean value ( if its a palindrome boolean value==true , other ,false)
    for word in words:
        results[word] = is_palindrome(word)

    return results


if __name__ == "__main__":

 words = ['sheep', 'xenex', 'cow']
 check_if_pal = check_palindrome(words)
 for word, palindrome in check_if_pal.items():
    print(f"'{word}': Palindrome? {palindrome}")
