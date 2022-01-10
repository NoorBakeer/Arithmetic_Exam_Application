# please work with the preset variable `word`

forward = word
backward = forward[len(forward)::-1]
if forward == backward:
    print("Yes")
else:
    print("No")
