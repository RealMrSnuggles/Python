"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed
 (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
 Spaces will be included only when more than one word is present."""
def spin_words(sentence):
    words = sentence.split()
    processed = []
    for word in words:
        if len(word) > 4:
            processed.append(word[::-1])
        else:
            processed.append(word)
    return " ".join(processed)

print(spin_words("Hi, Hello World"))