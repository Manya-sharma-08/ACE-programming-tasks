# Student result analyzer Project - medium task 2

# making a menu

print("--------------------")
print("        MENU        ")
print("--------------------")
print("Rules : you will be given 10 mcq baised questions with 4 options each")
print("10 points will be rewarded for every right answer")
print("5 points will be deducted for every wrong one")
print("--------------------")

# storing the questions, options and the answers in a list

questions = [
    "1) What does ip in ip address stand for?",
    "2) Which company developed the java programming language originally?",
    "3) What type of memory is volatile?",
    "4) Which shortcut is commonly used to copy text on windows?",
    "5) In binary, what is 1010 equal to in decimal?",
    "6) Which data structure follows FIFO?",
    "7) What does CPU stand for?",
    "8) Which language is known as a markup language?",
    "9) Which of these is an operating system?",
    "10) What is the full form of RAM?"
]

options = [
    ["a) Internet protocol", "b) Internal process", "c) Instant program", "d) Integrated package"],
    ["a) Microsoft", "b) Oracle", "c) Sun Microsystems", "d) IBM"],
    ["a) ROM", "b) RAM", "c) Hard disk", "d) SSD"],
    ["a) ctrl + v", "b) ctrl + x", "c) ctrl + c", "d) ctrl + z"],
    ["a) 8", "b) 10", "c) 12", "d) 15"],
    ["a) Stack", "b) Queue", "c) Tree", "d) Graph"],
    ["a) Central Processing Unit", "b) Computer Personal Unit", "c) Central Program Utility", "d) Control Processing Unit"],
    ["a) Python", "b) Java", "c) HTML", "d) C++"],
    ["a) Python", "b) Windows", "c) MySQL", "d) HTML"],
    ["a) Read Access Memory", "b) Random Access Memory","c) Rapid Access Memory", "d) Run Access Memory"]
]

answers = ["a", "c", "b", "c", "b", "b", "a", "c", "b", "b"]

score = 0
points = 10 

# using for loop to display all the question, options and answers (if correct or not) one by one

for i in range(len(questions)):
    print("\n" + questions[i])
    for opt in options[i]:
        print(opt)
    user_ans = input("your answer: ").lower()
    
    if user_ans == answers[i]:
        print("Correct!")
        print("Plus 10 points")
        score += points
    else:
        print(f"Wrong answer! Correct answer is {answers[i]}")
        print("Minus 5 points")
        score -= 5

# printing the final code

print("\nquiz over!")
print(f"your final score: {score}/{len(questions)*points}")

if score == len(questions) * points:
    print("Excellent! Perfect score!")
elif score >= 50:
    print("Good job!")
else:
    print("Keep practicing!")

#End of code