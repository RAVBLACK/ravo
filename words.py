#4)The wordlist I provided, word.txt, doesn’t contain single letter words. So you might want to add “I”, “a”, and the empty string.

with open('word.txt') as f:
    word=set(f.read().split()) | {"|" , "a",""}
print(word)

#Output:
#{'hello', 'welcome', '|', '', 'a', 'hi'}