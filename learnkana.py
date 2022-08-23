#|==========================================================================================|
#| Name: learnkana.py                                                                       |
#|                                                                                          |
#| Developed By: Tyrell Mcintosh - August 2022                                              |
#|                                                                                          |
#| Purpose: To learn hiragana, katakana, and kanji all in one place and track the results   |
#|           of user performance.                                                           |
#|                                                                                          |
#| Functions: my_function: Responsible for retrieving input for the task to be performed    |
#|                          and then prompt the user for answers to the questions           |
#|            my_calculations: Responsible for calculating the amount of time taken and     |
#|                              how well the user answered the questions                    |
#|                                                                                          |
#| Variables: kana - integer taken from user to determine the characters to learn           |
#|            correct/incorrect/count - tracks performance to calculate a percentage        |
#|            randline - the random line in the textfile that will be the question          |
#|            japanese - the japanese part of the partitioned line                          |
#|            romaji - the romaji part of the partition line                                |
#|            score - the percantage of questions answered correctly                        |
#|            elapsed - the seconds it took to finish the task                              |
#|            wrong - list of incorrect answers                                             |
#|            trigger - program will run until condition is met                             |
#|------------------------------------------------------------------------------------------|
import random
import time

trigger = ''

def my_function():
    #User input taken to determine the task to be performed
    print("Which task today?\n 1: Basic Hiragana\n 2: Hiragana with Dakuten&Handakuten\n", \
      "3: Basic Katakana\n 4: Katakana with Dakuten&Handakuten\n 5: All Kana\n", \
      "6: Kanji\n 7: JLPT N5 Vocabulary (in progress)")
    kana = input("You decide > ")

    # Open textfile and read the lines into a list if the user hasn't picked kanji
    if (kana != "6"):
        txtfile = open("kana.txt","r",encoding='utf-8').read().splitlines()

    # Switch Case to choose the range of lines the user will be using
    match kana:
        case "1":
            txtfile = txtfile[0:46]
            print("You have elected to practice Basic Hiragana, let's begin")
        case "2":
            txtfile = txtfile[46:71]
            print("You have elected to practice Hiragana with Dakuten&Handakuten, let's begin")
        case "3":
            txtfile = txtfile[71:117]
            print("You have elected to practice Basic Katakana, let's begin")
        case "4":
            txtfile = txtfile[117:142]
            print("You have elected to practice Katakana with Dakuten&Handakuten, let's begin")
        case "5":
            txtfile = txtfile
            print("You have elected to practice both Hiragana and Katakana, let's begin")
        case "6":
            txtfile = open("kanji.txt","r",encoding='utf-8').read().splitlines()
            print("You have elected to practice Kanji, let's begin")
        case _:
            exit()

    # Variables to keep track of performance
    correct = incorrect = count = 0
    wrong = []
    start = time.time()

    # Loop that prints each line to prompt the user for an answer to the question
    while True:
        count += 1
        randline = random.choice(txtfile)
        japanese = randline.partition("-")[0]
        answer = input("\nWhat does {} sound like?".format(japanese))
        romaji = randline.partition("-")[2]
        if (answer == romaji):
            correct += 1
            print("Correct! So far you have {} correct answers and {} incorrect answers."
                  .format(correct, incorrect))
            txtfile.remove(randline)
        else:
            incorrect += 1
            wrong.append(japanese)
            print("Incorrect, {} is the correct answer".format(romaji))

        answer2 = input("Press the enter key to continue or x to exit\n")
        if (answer2 == 'x' or not txtfile):
            break
    # Stop timer
    finish = time.time()

    return start,finish,correct,count,wrong

def my_calculations(start,finish,correct,count):
    elapsed = "{:.2f}".format(finish - start)
    score = "{:.0%}".format(correct / count)
    return elapsed,score

while (trigger!= 'x'):
    start,finish,correct,count,wrong = my_function()
    elapsed, score = my_calculations(start,finish,correct,count)

    print("You finished with a score of {} and took {} seconds to finish.".format(score,elapsed))
    print("The following are the ones you got incorrect:",*wrong)
    trigger = input("Would you like to play again? Press enter to proceed to menu or x to quit\n")    

print("Thanks for playing!")
