import random

score = 0  # score variable
lifes = 3  # lifes variable

# function to ask a question
def ask_question():
    global score, lifes
    
    # check if the player has no lifes left
    if lifes <= 0:
        print("You lost. Total Score:", score)
        exit()  # exit the program

    # generate two random numbers
    number1 = random.randint(5, 7)
    number2 = random.randint(5, 7)
    # variables for addition, subtraction, and multiplication
    result_addition = number1 + number2
    result_subtraction = number1 - number2
    result_multiplication = number1 * number2
    results_array = [result_addition, result_subtraction, result_multiplication]
    random_result = random.choice(results_array)

    # determine the question based on the index
    if results_array.index(random_result) == 0:
        question = f"Addition: {number1} + {number2} = ? "
    elif results_array.index(random_result) == 1:
        question = f"Subtraction: {number1} - {number2} = ? "
    elif results_array.index(random_result) == 2:
        question = f"Multiplication: {number1} * {number2} = ? "

    # ask the question and get the user's response
    user_input = int(input(question))
    # check if the answer is correct or wrong
    check_answer(user_input, random_result)

# function that checks the user's answer
def check_answer(answer, random_result):
    global score, lifes
    
    # if the answer matches the random result
    if answer == random_result:
        # print the correct answer message
        print("Correct!")
        # add +5 to the score
        score += 5
        # print the score
        print("Score:", score)
    else:
        # print the wrong answer message
        print("Incorrect!")
        # remove -1 life
        lifes -= 1
        # print the lifes
        print("Lifes Left:", lifes)

    # continue asking questions
    ask_question()

# start the question
ask_question()