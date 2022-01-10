v = input()
v = float(v)

if v < 2:
    print("Analytic")
elif 2 <= v <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
