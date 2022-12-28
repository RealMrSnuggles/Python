# Write a function that accepts a string, and returns 
# the same string with all even indexed characters 
# in each word upper cased

def to_weird_case(words):
    word_list = words.split()
    weird_sentence = []
    for word in word_list:
        weird_word = []
        for i, letter in enumerate(word):
            if i % 2:
                weird_word.append(letter.lower())
            else:
                weird_word.append(letter.upper())
        weird_sentence.append("".join(weird_word))
    return " ".join(weird_sentence)

print(to_weird_case( "Weird string case" ))