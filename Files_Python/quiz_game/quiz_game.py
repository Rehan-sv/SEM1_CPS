import random

def play_quiz(file_path):
    score = 0
    total_questions = 0

    with open(file_path, 'r') as file, open('player_scores.txt', 'a') as player_scores:
        player_name = input("Enter your name: ")
        player_scores.write(f"{player_name}: ")
        for line in file:
            # breakpoint()
            total_questions += 1
            parts = line.strip().split(';')
            question, choices, correct_answer = parts[0], parts[1:-1], parts[-1]
            random.shuffle(choices)
            
            print(question)
            for i, choice in enumerate(choices, start=1):
                print(f"{i}. {choice}")
            
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if choices[user_answer - 1] == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {correct_answer}")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 4.")
            print()
            
        player_scores.write(f"{score}/{total_questions}\n")

    print(f"Quiz finished! Your score: {score}/{total_questions}")

play_quiz('quiz_questions_with_answers.txt')