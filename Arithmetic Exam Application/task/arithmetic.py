import random
from typing import Union, Any


def generate_task_1():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    op = random.choice("+-*")
    exp: Union[str, Any] = str(num1) + ' ' + op + ' ' + str(num2)
    return exp


def generate_task_2():
    num = random.randint(11, 29)
    return num


def evaluate_expression(exp):
    a = exp.split(' ')
    num1 = int(a[0])
    num2 = int(a[2])
    op = a[1]
    res = None

    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2

    return res


def check_answer_level1(exp, ans):
    res = evaluate_expression(exp)

    if res == ans:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def check_answer_level2(num, ans):  # TODO : remove redundant code
    res = num ** 2
    if res == ans:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def check_format(num):
    if num.startswith('-') and num[1:].isnumeric():
        return True
    elif num.isnumeric():
        return True
    else:
        return False


def choose_level():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    while True:
        try:
            level = int(input())
            if not (level == 1 or level == 2):
                print("Incorrect format.")
                continue
            return level
        except ValueError:
            print("Incorrect format.")


def get_answer():
    global answer
    while True:
        try:
            answer = input()
            if check_format(answer):
                return int(answer)
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


N = 0
option = choose_level()

for x in range(5):
    task = None
    answer = None
    if option == 1:
        task = generate_task_1()
        print(task)
        answer = get_answer()
        N += check_answer_level1(task, answer)
    else:
        task = generate_task_2()
        print(task)
        answer = get_answer()
        N += check_answer_level2(task, answer)

print(f"Your mark is {N}/5.")

print("Would you like to save your result to the file? Enter yes or no.")
choice = input()
if choice == "yes" or choice == "YES" or choice == "y" or choice == "Yes":
    print("What is your name?")
    name = input()
    description = ""
    if option == 1:
        description = "(simple operations with numbers 2-9)"
    else:
        description = "(integral squares 11-29)"
    with open("results.txt", 'a') as file:
        file.write(name + f": {N}/5 int level {option} {description}.")
        print("The results are saved in 'results.txt'.")
