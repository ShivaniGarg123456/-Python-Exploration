def quiz():
    questions = [
        {"question": "What is the output of 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},

        {"question": "Which keyword is used to define a function in Python?", "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},

        {"question": "What does the 'len()' function do?", "options": ["A) Returns length of a list", "B) Finds the max value", "C) Sorts a list", "D) None of these"], "answer": "A"},

        {"question": "Which loop is used when the number of iterations is unknown?", "options": ["A) for", "B) while", "C) do-while", "D) None"], "answer": "B"},

        {"question": "How do you start an if statement in Python?", "options": ["A) if condition:", "B) if (condition)", "C) if: condition", "D) condition if:"], "answer": "A"},

        {"question": "Which symbol is used for comments in Python?", "options": ["A) //", "B) --", "C) #", "D) /* */"], "answer": "C"},

        {"question": "What is the default return value of a function that does not have a return statement?", "options": ["A) 0", "B) None", "C) Empty string", "D) Error"], "answer": "B"},

        {"question": "Which function is used to take user input in Python?", "options": ["A) scan()", "B) input()", "C) get()", "D) read()"], "answer": "B"},

        {"question": "Which operator is used for exponentiation in Python?", "options": ["A) ^", "B) **", "C) %", "D) //"], "answer": "B"},
        
        {"question": "How do you declare a function in Python?", "options": ["A) function myFunc():", "B) def myFunc():", "C) define myFunc():", "D) func myFunc():"], "answer": "B"}
    ]
    
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", q["answer"])
    
    print("\nQuiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")

quiz()

        