questions = [
    {"q": "What is 2 + 2?", "ans": "4"},
    {"q": "What is the capital of India?", "ans": "Delhi"},
    {"q": "What comes after B?", "ans": "C"}
]

score = 0

for q in questions:
    answer = input(q["q"] + " ")  # User se input lena
    if answer.lower() == q["ans"].lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print(f"\nQuiz Over! Your score: {score}/{len(questions)}")
