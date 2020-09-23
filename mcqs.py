'''
Consider a multiple choice quiz:
    1. Add question
    2. Show questions
    3. Quiz: 
    4. Exit: How many correct, how many wrong & total no. of questions
'''
def mcq_menu():
    mcqs = {"Questions": input("Enter question: "),
                "choices" : {"a":input("Enter option a: "),
                             "b":input("Enter option b: "),
                             "c":input("Enter option c: "),
                             "d":input("Enter option d: ")},
                "answers" : {"answer":input("Enter correct answer option: ")}
            }
    return mcqs

print('Consider a multiple choice quiz:')
print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
options = {"1":"Add question",
               "2":"Show questions",
               "3":"Quiz",
               "4": "Exit"}
option = input("Select one of the option above (1/2/3/4): ")
quiz = list()
answers = list()
correct_answers = 0
wrong_answers = 0
num_of_questions = 0
while True:
    if option == "1":
        mcqs = mcq_menu()
        num_of_questions += 1
        quiz.append([{"questions": mcqs["Questions"]},
                     {"options": mcqs["choices"]},
                     {"correct answers":mcqs["answers"]}
                    ])
        print("********************************************************")
        print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
        option = input("Select one of the option above (1/2/3/4): ")
        continue
    if option == "2":
        if quiz == []:
            print("No questions to show!")
            print("*****************************************************")
            print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
            option = input("Select one of the option above (1/2/3/4): ")
            continue
        for i in range(num_of_questions):
            print("Question:",quiz[i][0]["questions"])
            print("options are:",quiz[i][1]["options"])
        print("*********************************************************")
        print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
        option = input("Select one of the option above: ")
        continue
    if option == "3":
        if quiz == []:
            print("No Questions!\nAdd some questions..")
            print("*****************************************************")
            print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
            option = input("Select one of the option above (1/2/3/4): ")
            continue
        for j in range(num_of_questions):
            print("Question:",quiz[j][0]["questions"])
            print("options are:",quiz[j][1]["options"])
            answer = input("Enter answer option: ")
            answers.append(answer)
        print("Your answers are:",answers)
        for k in range(num_of_questions):
            if answers[k] == quiz[k][2]["correct answers"]["answer"]:
                correct_answers += 1
            else:
                wrong_answers += 1
        print("************************************************************")
        print('1. Add question\n2. Show questions\n3. Quiz\n4. Exit')
        option = input("Select one of the option above: ")
    if option == "4":
        print("Total number of questions =",num_of_questions)
        print("Your score is " + str(correct_answers) + "/" + str(num_of_questions))
        print("You have Correctly answered "+ str(correct_answers) + " questions.")
        print("You have incorrectly answered "+ str(wrong_answers) + " questions.")
        break



        
        
