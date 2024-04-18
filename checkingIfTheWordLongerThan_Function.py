def words_longer_than_n(myString, n):

    words = myString.split() # dividing the string to words , each word separately
    myWords = [word for word in words # entering to this array all the words of the string that have a length greater than n )
                     if len(word) > n]
    return myWords

if __name__ == "__main__":
    myString = 'The quick brown fox jumps over the lazy dog'
    n = 4
    result = words_longer_than_n(myString, n)
    print(result)
