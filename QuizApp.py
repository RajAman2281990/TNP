import random
python_questions = [
    {"question": "What is the output of print(2**3)?", "options": ["6", "8", "9"], "answer": "8"},
    {"question": "Which keyword is used for function in Python?", "options": ["func", "define", "def"],
     "answer": "def"},
    {"question": "What is the correct way to declare a variable?", "options": ["int x = 10", "x = 10", "var x = 10"],
     "answer": "x = 10"},
    {"question": "Who developed Python Programming Language?", "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum"],
     "answer": "Guido van Rossum"},
    {"question": "Which type of Programming does Python support?", "options": ["structured programming", "Object-Oriented programming", "Both"],
     "answer": "Both"},
    {"question": " Is Python case sensitive when dealing with identifiers?", "options": ["no", "yes", "none"], "answer": "yes"},
    {"question": "Which of the following is the correct extension of the Python file?", "options": [" .python", ".py", ".p"], "answer": ".py"},
    {"question": "Is Python code compiled or interpreted?", "options": ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled"], "answer": "Python code is both compiled and interpreted"},
    {"question": "All keywords in Python are in _________", "options": ["Capitalized", "UPPER CASE", "none"], "answer": "none"},
    {"question": "What will be the value of the following Python expression?""\n 4 + 3 % 5", "options": ["7", "8", "9"], "answer": "7"},
    {"question": "Which of the following is used to define a block of code in Python language?", "options": ["Indentation", "key", "brackets"], "answer": "Indentation"},
    {"question": "Which of the following character is used to give single-line comments in Python?", "options": ["//", "/*", "#"], "answer": "#"},
    {"question": "What does pip stand for python?", "options": ["Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program"], "answer": "Preferred Installer Program"},
    {"question": "Which of the following functions is a built-in function in python?", "options": [" factorial()", "print()", "sqrt()"], "answer": "print()"},
    {"question": "Which of the following is not a core data type in Python programming?", "options": ["Tuples", "Lists", "Class"], "answer": "Class"},
]

java_questions = [
    {"question": "Which method is the entry point for a Java program?", "options": ["start()", "main()", "init()"],
     "answer": "main()"},
    {"question": "What is used to compile Java code?", "options": ["gcc", "javac", "python"], "answer": "javac"},
    {"question": "Which keyword is used for inheritance in Java?", "options": ["extends", "inherits", "implements"],
     "answer": "extends"},
    {"question": "Which method is the entry point for a Java program?", "options": ["start()", "main()", "init()"], "answer": "main()"},
    {"question": "What is used to compile Java code?", "options": ["gcc", "javac", "python"], "answer": "javac"},
    {"question": "Which keyword is used for inheritance in Java?", "options": ["extends", "inherits", "implements"], "answer": "extends"},
    {"question": "Which package is automatically imported in all Java programs?", "options": ["java.io", "java.util", "java.lang"], "answer": "java.lang"},
    {"question": "Which data type is used to create a variable that stores text?", "options": ["String", "char", "int"], "answer": "String"},
    {"question": "How do you create an object of a class in Java?", "options": ["new Object()", "Object obj = new Object()", "create Object()"], "answer": "Object obj = new Object()"},
    {"question": "Which of these is not a Java access modifier?", "options": ["private", "public", "internal"], "answer": "internal"},
    {"question": "What is the default value of an int variable in Java?", "options": ["0", "null", "undefined"], "answer": "0"},
    {"question": "Which method in Java is used to create a thread?", "options": ["start()", "run()", "execute()"], "answer": "start()"},
    {"question": "Which of the following is not a valid Java keyword?", "options": ["static", "void", "include"], "answer": "include"},
    {"question": "Which interface is used to handle collections in Java?", "options": ["Collection", "Collections", "List"], "answer": "Collection"},
    {"question": "What is the size of an int data type in Java?", "options": ["16 bits", "32 bits", "64 bits"], "answer": "32 bits"}
]

aptitude_questions = [
    {"question": "What is 15% of 200?", "options": ["20", "30", "40"], "answer": "30"},
    {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["20", "32", "24"], "answer": "32"},
    {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
     "options": ["2 hours", "3 hours", "4 hours"], "answer": "3 hours"},
    {"question": "What is 15% of 200?", "options": ["20", "30", "40"], "answer": "30"},
    {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["20", "32", "24"], "answer": "32"},
    {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
     "options": ["2 hours", "3 hours", "4 hours"], "answer": "3 hours"},
    {"question": "If 12 men can complete a task in 8 days, how many days will 6 men take to complete the same task?",
     "options": ["16 days", "12 days", "8 days"], "answer": "16 days"},
    {"question": "What is the average of the first five prime numbers?", "options": ["5.6", "6.4", "7.6"],
     "answer": "5.6"},
    {"question": "A shopkeeper offers a discount of 20% on a product that costs Rs. 500. What is the selling price?",
     "options": ["Rs. 400", "Rs. 450", "Rs. 500"], "answer": "Rs. 400"},
    {
        "question": "In a class of 50 students, 28 like mathematics and 36 like science. How many students like both subjects?",
        "options": ["14", "16", "18"], "answer": "14"},
    {
        "question": "A man walks 10 meters north, then turns right and walks 20 meters. Finally, he turns left and walks 10 meters. How far is he from the starting point?",
        "options": ["20 meters", "30 meters", "40 meters"], "answer": "30 meters"},
    {"question": "The sum of two numbers is 50 and their difference is 20. What are the two numbers?",
     "options": ["35 and 15", "30 and 20", "40 and 10"], "answer": "35 and 15"},
    {"question": "What is the simple interest on Rs. 2000 at 5% per annum for 2 years?",
     "options": ["Rs. 100", "Rs. 200", "Rs. 300"], "answer": "Rs. 200"},
    {"question": "A person buys an article for Rs. 100 and sells it for Rs. 120. What is the percentage profit?",
     "options": ["10%", "20%", "25%"], "answer": "20%"},
    {"question": "If 5 machines can produce 500 units in 5 hours, how many units can 8 machines produce in 8 hours?",
     "options": ["800 units", "1000 units", "1280 units"], "answer": "1280 units"}

]

users_db = {}
def register():
    print("\n--- Registration ---")
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Try logging in or choose another username.")
    else:
        password = input("Enter a new password: ")
        users_db[username] = password
        print("Registration successful!")
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def choose_quiz():
    print("\n--- Choose Quiz ---")
    print("1. Python")
    print("2. Java")
    print("3. Aptitude")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        return python_questions
    elif choice == '2':
        return java_questions
    elif choice == '3':
        return aptitude_questions
    else:
        print("Invalid choice. Please select again.")
        return choose_quiz()
def conduct_quiz(questions):
    print("\n--- Quiz Started ---")
    selected_questions = random.sample(questions, 10)
    score = 0

    index = 1
    for i in selected_questions:
        print(f"\nQ{index}. {i['question']}")

        option_index = 1
        for option in i['options']:
            print(f"{option_index}. {option}")
            option_index += 1

        answer = input("Enter your answer (1/2/3): ")
        if i['options'][int(answer) - 1] == i['answer']:
            score += 1
        index += 1

    print(f"\nQuiz Completed! Your score is {score}/10.")
    return score
def main():
    while True:
        print("\n--- Welcome to the Quiz App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            register()
        elif option == '2':
            if login():
                while True:
                    questions = choose_quiz()
                    conduct_quiz(questions)
                    again = input("\nDo you want to attempt again? (yes/no): ")
                    if again.lower() != 'yes':
                        break
            else:
                print("Login failed. Try again.")
        elif option == '3':
            print("Exiting the quiz app. Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")
if __name__ == "__main__":
    main()
