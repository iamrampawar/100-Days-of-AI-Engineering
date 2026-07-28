# Dictionary Based Quiz

quiz = {
    "What does CPU stand for?": "Central Processing Unit",
    "Which language is popular for AI?": "Python",
    "What is the capital of India?": "New Delhi"
}

score = 0

for question, answer in quiz.items():
    user_answer = input(question + " : ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct Answer: {answer}\n")

print(f"Your Score: {score}/{len(quiz)}")