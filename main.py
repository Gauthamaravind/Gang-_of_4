import random

def generate_question():
    operand1 = random.randint(1, 1000)
    operand2 = random.randint(1, 1000)
    operator = random.choice(['+', '-', '*','^'])
    question = f"{operand1} {operator} {operand2}"
    answer = eval(question)
    return question, answer

def display_score(score):
    print(f"\nYour current score: {score}\n")

def calculator_game():
    print("Welcome to the Calculator Game!")
    print("Try to solve as many math problems as you can.")

    score = 0
    while True:
        question, correct_answer = generate_question()
        print(f"\nQuestion: {question}")

        try:
            user_answer = float(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == correct_answer:
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

        display_score(score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Your final score is:", score)
            break

if __name__ == "__main__":
    calculator_game()

print("This was made by Gautham and Dev (:")