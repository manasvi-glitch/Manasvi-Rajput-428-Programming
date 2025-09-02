# -------------------------------
# CLI Quiz App in Python
# -------------------------------

def quiz_app():
    # List of questions (each question is a dictionary)
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Paris", "2. Rome", "3. Berlin", "4. Madrid"],
            "answer": "1"  # Correct option number
        },
        {
            "question": "Which language is known as the mother of all programming?",
            "options": ["1. Python", "2. C", "3. Java", "4. Fortran"],
            "answer": "2"
        },
        {
            "question": "Who developed Python?",
            "options": ["1. James Gosling", "2. Dennis Ritchie", "3. Guido van Rossum", "4. Bjarne Stroustrup"],
            "answer": "3"
        },
        {
            "question": "What does RAM stand for?",
            "options": ["1. Read Access Memory", "2. Random Access Memory", "3. Run Access Memory", "4. Read After Memory"],
            "answer": "2"
        },
        {
            "question": "Which one is NOT an OOP concept?",
            "options": ["1. Encapsulation", "2. Abstraction", "3. Compilation", "4. Inheritance"],
            "answer": "3"
        }
    ]
    
    score = 0  # Keep track of correct answers
    
    # Loop through all questions
    for q in questions:
        print("\n" + q["question"])   # Print question
        for option in q["options"]:   # Print all 4 options
            print(option)
        
        # Get user input (answer as option number)
        ans = input("Enter option number: ")
        
        # Check if answer is correct
        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is option {q['answer']}")
    
    # Final score display
    print(f"\nYour final score: {score}/{len(questions)}")

# Run the quiz app
quiz_app()

