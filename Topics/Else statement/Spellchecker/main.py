dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
flag = False
for w in dictionary:
    if word == w:
        flag = True

if flag:
    print("Correct")
else:
    print("Incorrect")
