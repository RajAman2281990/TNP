import random

USER_DATA_FILE = "users.txt"

QUIZ_QUESTIONS = {
    "python": [
        {"question": "What is the output of print(2**3)?", "options": ["6", "8", "9"], "answer": "8"},
        {"question": "Which keyword is used for function in Python?", "options": ["func", "define", "def"],
         "answer": "def"},
        {"question": "What is the correct way to declare a variable?",
         "options": ["int x = 10", "x = 10", "var x = 10"],
         "answer": "x = 10"},
        {"question": "Who developed Python Programming Language?",
         "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum"],
         "answer": "Guido van Rossum"},
        {"question": "Which type of Programming does Python support?",
         "options": ["structured programming", "Object-Oriented programming", "Both"],
         "answer": "Both"},
        {"question": " Is Python case sensitive when dealing with identifiers?", "options": ["no", "yes", "none"],
         "answer": "yes"},
        {"question": "Which of the following is the correct extension of the Python file?",
         "options": [" .python", ".py", ".p"], "answer": ".py"},
        {"question": "Is Python code compiled or interpreted?",
         "options": ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted",
                     "Python code is only compiled"], "answer": "Python code is both compiled and interpreted"},
        {"question": "All keywords in Python are in _________", "options": ["Capitalized", "UPPER CASE", "none"],
         "answer": "none"},
        {"question": "What will be the value of the following Python expression?""\n 4 + 3 % 5",
         "options": ["7", "8", "9"], "answer": "7"},
        {"question": "Which of the following is used to define a block of code in Python language?",
         "options": ["Indentation", "key", "brackets"], "answer": "Indentation"},
        {"question": "Which of the following character is used to give single-line comments in Python?",
         "options": ["//", "/*", "#"], "answer": "#"},
        {"question": "What does pip stand for python?",
         "options": ["Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program"],
         "answer": "Preferred Installer Program"},
        {"question": "Which of the following functions is a built-in function in python?",
         "options": [" factorial()", "print()", "sqrt()"], "answer": "print()"},
        {"question": "Which of the following is not a core data type in Python programming?",
         "options": ["Tuples", "Lists", "Class"], "answer": "Class"},
    ],

    "java": [
        {"question": "Which method is the entry point for a Java program?", "options": ["start()", "main()", "init()"],
         "answer": "main()"},
        {"question": "What is used to compile Java code?", "options": ["gcc", "javac", "python"], "answer": "javac"},
        {"question": "Which keyword is used for inheritance in Java?", "options": ["extends", "inherits", "implements"],
         "answer": "extends"},
        {"question": "Which method is the entry point for a Java program?", "options": ["start()", "main()", "init()"],
         "answer": "main()"},
        {"question": "What is used to compile Java code?", "options": ["gcc", "javac", "python"], "answer": "javac"},
        {"question": "Which keyword is used for inheritance in Java?", "options": ["extends", "inherits", "implements"],
         "answer": "extends"},
        {"question": "Which package is automatically imported in all Java programs?",
         "options": ["java.io", "java.util", "java.lang"], "answer": "java.lang"},
        {"question": "Which data type is used to create a variable that stores text?",
         "options": ["String", "char", "int"], "answer": "String"},
        {"question": "How do you create an object of a class in Java?",
         "options": ["new Object()", "Object obj = new Object()", "create Object()"],
         "answer": "Object obj = new Object()"},
        {"question": "Which of these is not a Java access modifier?", "options": ["private", "public", "internal"],
         "answer": "internal"},
        {"question": "What is the default value of an int variable in Java?", "options": ["0", "null", "undefined"],
         "answer": "0"},
        {"question": "Which method in Java is used to create a thread?", "options": ["start()", "run()", "execute()"],
         "answer": "start()"},
        {"question": "Which of the following is not a valid Java keyword?", "options": ["static", "void", "include"],
         "answer": "include"},
        {"question": "Which interface is used to handle collections in Java?",
         "options": ["Collection", "Collections", "List"], "answer": "Collection"},
        {"question": "What is the size of an int data type in Java?", "options": ["16 bits", "32 bits", "64 bits"],
         "answer": "32 bits"}
    ],
    "aptitude": [
        {"question": "What is 15% of 200?", "options": ["20", "30", "40"], "answer": "30"},
        {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["20", "32", "24"],
         "answer": "32"},
        {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
         "options": ["2 hours", "3 hours", "4 hours"], "answer": "3 hours"},
        {"question": "What is 15% of 200?", "options": ["20", "30", "40"], "answer": "30"},
        {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["20", "32", "24"],
         "answer": "32"},
        {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
         "options": ["2 hours", "3 hours", "4 hours"], "answer": "3 hours"},
        {
            "question": "If 12 men can complete a task in 8 days, how many days will 6 men take to complete the same task?",
            "options": ["16 days", "12 days", "8 days"], "answer": "16 days"},
        {"question": "What is the average of the first five prime numbers?", "options": ["5.6", "6.4", "7.6"],
         "answer": "5.6"},
        {
            "question": "A shopkeeper offers a discount of 20% on a product that costs Rs. 500. What is the selling price?",
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
        {
            "question": "If 5 machines can produce 500 units in 5 hours, how many units can 8 machines produce in 8 hours?",
            "options": ["800 units", "1000 units", "1280 units"], "answer": "1280 units"}

    ]
}
def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    if check_user_exists(username):
        print("Username already exists! Try logging in.")
        return False

    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful!")
    return True
def check_user_exists(username):
    try:
        with open(USER_DATA_FILE, "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",")
                if stored_username == username:
                    return True
    except FileNotFoundError:
        return False
    return False
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not check_user_exists(username):
        print("Username not found! Please register.")
        return False

    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                print("Login successful!")
                return True
    print("Invalid username or password!")
    return False
def start_quiz(topic):
    questions = QUIZ_QUESTIONS[topic]
    random.shuffle(questions)
    score = 0

    for i in range(5):
        question = questions[i]
        print(f"\nQ{i + 1}. {question['question']}")
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

        user_answer = int(input("Enter your answer (1/2/3): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")

    print(f"\nYour score: {score}/5")
def main_menu():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                quiz_menu()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
def quiz_menu():
    while True:
        print("\nSelect a quiz topic:")
        print("1. Python")
        print("2. Java")
        print("3. Aptitude")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_quiz("python")
        elif choice == '2':
            start_quiz("java")
        elif choice == '3':
            start_quiz("aptitude")
        elif choice == '4':
            print("Logging out.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
