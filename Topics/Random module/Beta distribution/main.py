import random


random.seed(3)
# call the function here
alpha = 0.9
beta = 0.1
result = random.betavariate(alpha, beta)
print(result)