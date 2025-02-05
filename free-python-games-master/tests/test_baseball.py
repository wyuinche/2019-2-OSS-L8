"""Baseball, Guess 4 digit number.

Exercises

1. Guess 4 randomly generated 4 digit numbers which has only one number each. No 0.
2. Hint for the guess ( right number, right number and right position ) is given
3. Guess again until you get a right guess

"""

import random
from turtle import *


"""get number of digits to play"""
def get_num_digit():
    digits = 0
    print("Enter Number of Digits to Play (max 9) : ", end='')
    while True:
        try:
            digits = int(input())
        except ValueError:
            print("You Should Input Only Numbers. Input : ", end='')
        else:
            if digits < 1 or digits > 9:
                print("Invalid Digit. Put a Number Between 1 to 9 : ", end='')
            else:
                break

    return digits


"""generate random number to start game"""
def generate_ran_ans(num_of_digits):
    return random.sample(range(1, 10), num_of_digits)


"""get user answer from user"""
def get_user_ans(right_ans_):
    user_ans = []
    valid = False

    user_input = input("Please Enter %d-digits : " % len(right_ans_))
    for pos in range(len(user_input)):
        if user_input[pos] < '0' or user_input[pos] > '9':
            valid = True

    while valid:
        user_input = input("Please Enter Only Numbers. Enter %d-digits : " % len(right_ans_))
        valid = False
        for pos in range(len(user_input)):
            if user_input[pos] < '0' or user_input[pos] > '9':
                valid = True

    for pos in range(len(user_input)):
        user_ans.append(int(user_input[pos]))

    return user_ans


"""check if user answer is in right format"""
def check_format(user_ans_, right_ans_):
    """return 1 for wrong digit"""
    if len(user_ans_) != len(right_ans_):
        print("Wrong Digit!")
        return False

    """return 2 for not a number"""
    for pos in range(len(user_ans_)):
        if user_ans_[pos] < 1 or user_ans_[pos] > 9:
            print("Not a Valid Number! Zero is Not Included")
            return False

    """return 3 for repeated number"""
    for fix_pos in range(len(user_ans_)):
        for comp_pos in range(fix_pos+1, len(user_ans_)):
            if user_ans_[fix_pos] == user_ans_[comp_pos]:
                print("Repeated Number Included!")
                return False

    """return 0 for right format answer"""
    return True


"""compare user answer with right answer"""
def compare_user_ans(right_ans_, user_ans_):
    check_result = {'right number': 0, 'right position': 0}

    for pos in range(len(right_ans_)):
        if user_ans_[pos] == right_ans_[pos]:
            check_result['right position'] += 1
        elif user_ans_[pos] in right_ans_:
            check_result['right number'] += 1

    return check_result


num_of_digits = get_num_digit()
right_ans = generate_ran_ans(num_of_digits)
correct = False
trials = 1

while not correct:
    user_ans = get_user_ans(right_ans)
    if check_format(user_ans, right_ans):
        checked_ans = compare_user_ans(right_ans, user_ans)

        if checked_ans['right position'] == len(right_ans):
            print("You got right answer : ", end='')
            for position in range(len(user_ans)):
                print(user_ans[position], end='')
            print("  with %d trials" % trials)
            correct = True
        else:
            print("Right Number : %s\nRight Position : %s\n%d Trials"
                  % (checked_ans['right number'], checked_ans['right position'], trials))
            trials += 1

print("The End")