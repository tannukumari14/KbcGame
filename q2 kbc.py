print(".*.*.*.*.*kaun banega crorepati.*.*.*.*.")
question_list = ["How many continents are there?", "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?", "Who founded Microsoft"]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Bill Gates"]
]

solution_list = [3, 4, 1, 2]

answer = [
    ["2. Nine", "3. Seven"],
    ["3. Chennai", "4. Delhi"],
    ["2. Counseling", "1. Software Engineering"],
    ["2. Jeff Bezos", "4. Bill Gates"]
]

print(".*.*.*.*.*kbc*.*.*.*.*.")
i = 0
s = 0
count = 0

while i < len(question_list):
    print(question_list[i])
    a = 0
    b = i
    while a < len(options_list[i]):
        k = options_list[i][a]
        print(a + 1, k)
        a += 1
    num = input("Do you want 50 50 lifeline")
    if num == "yes":
        print("accept")
        if count < 1:
            print(answer[b])
            num1 = int(input("enter the answer"))
            if num1 == solution_list[i]:
                s += 1
                print("your answer is correct")
                print("YOU WIN Rs/", s)
            else:
                print("incorrect answer")
                print("YOU WIN Rs/", s)
                break
            count += 2000
        else:
            print("you already used lifeline")
            num2 = int(input("enter your answer"))
            if num2 == solution_list[i]:
                print("congrats, your answer is right")
                s += 10
                print("YOU WIN Rs/", s)
            else:
                print("your answer is wrong")
                print("YOU WIN Rs/", s)
                break
    else:
        k = int(input("enter your answer"))
        if k == solution_list[i]:
            print("right answer")
            s += 1000
            print("you win Rs/", s)
        else:
            print("no chance")
            print("your answer is wrong")
            print("you win Rs/", s)
    i += 1

print("congratulations, you participated in the KBC game")
print("you win Rs/", s)
print("thanks for participating")
