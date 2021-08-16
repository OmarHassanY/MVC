import random

def runQuiz():
        print()
        print("Please enter your name: ",end='')
        name = str(input())
        if (not name or name.isspace()):
                print("Please enter a  name")
                runQuiz()
        correct = 0
        incorrect = 0
        print()

        # Holds all questions and answers for the quiz
        questionAnswerDict = {"What was Al Bundy's job from Married with Kids?\nA. Womens shoe salesman\nB. Bike Salesman\nC. Car Salesman\nD. Mens shoe salesman":"a",
        "What was Andy Taylor's job from The Andy Griffith Show?\nA. Security Guard\nB. Pilot\nC. Bartender\nD. Sheriff":"d",
        "What position did Ron Swanson Parks and recreation hold?\nA. Director\nB. Manager\nC. Coordinator\nD. None of the above":"a",
        "What was Homer Simpson's job from The Simpsons?\nA. Brewrey Worker\nB. Nuclear power plant saftey inspector\nC. He had no job\nD. Cashier":"b",
        "What was Peter Griffin's first job in family guy?\nA. Toy Maker\nB. Bartender\nC. Pool Boy\nD. Fisherman":"c",
        "Which of these was a job that Ned Flanders from the Simpsons had?\nA. Owner of Flancrest Enterprises\nB. Bible Salesman\nC. Calender Salesman\nD. Insurance worker":"a",
        "Where did Fez from that 70’s show work?\nA. Frycook\nB. Public saftey department\nC. He had no job\nD. Department of motor vehicles":"d",
        "What Job did Mike Brady from the brady bunch have?\nA. Carpenter\nB. Architect\nC. Construction worker\nD. Roofer":"b",
        "What job field was Sheldon Cooper from the Big Bang Theory a Part of?\nA. Biology\nB. Chemistry\nC. Physics\nD. Astronomy":"c",
        "What company did Michael Scott from the Office work for?\nA. Dunder Mifflin\nB. Google\nC. Microsoft\nD. None of the above":"a",
        "What Government Agency did Stan Smith from American dad work for?\nA. CIA\nB. FBI\nC. NSA\nD. None of the above":"a",
        "What kind of company did Kramer from Seinfeld work for?\nA. Pizza company\nB. Bagel company\nC. Candy company\nD. Chip Company":"b",
        "What was Archie Bunkers job from All in the Family?\nA. Warehouse worker\nB. Construction worker\nC. Loading dock worker\nD. None of the Above":"Loading dock worker"}

        # Loads a disposable list of all of the questions for the quiz
        questionList = []
        i = 0
        for key in questionAnswerDict:
                questionList.append(key)
                i += 1
        
        # Asks the user 5 questions from the disposable questions list and keeps track of how many
        # they had correct and incorrect

        listAmt = 12 # amount of questions left in the list
        for i in range(5):
                # num = random.randint(0,listAmt)
                # print(questionList[num])
                # print("Enter your answer: ",end='')

                # userAnswer = str(input())
                #(userAnswer.lower()!='a') or (userAnswer.lower()!='b') or (userAnswer.lower()!='c') or (userAnswer.lower()!='d')
                # while (True):
                go = True

                num = random.randint(0,listAmt)
                print(questionList[num])
                print("Enter your answer: ",end='')
                userAnswer = str(input())
                while go == True:
                        if userAnswer.lower() != 'a':
                                print('Answer invalid please try again. ',end='')
                                userAnswer = (input())
                        else:
                                go = False


                # userAnswer = str(input())
                #         print("User answer is invalid")
                #         break
                
                
                print()

                # tests the user answer vs. the true answer to the question
                if str(userAnswer).lower() == str(questionAnswerDict[questionList[num]]).lower():
                        correct += 1
                elif str(userAnswer).lower() != str(questionAnswerDict[questionList[num]]).lower():
                        incorrect += 1
                
                # Removes the question from the list after it is asked andl lowers the listAmt
                questionList.remove(questionList[num])
                listAmt -= 1

                # print("LIST AMT " + str(listAmt)) debug
                # print("LIST LENGTH " + str(len(questionList))) debug

                print()
                print(name + " you got " + str(correct) + " answers correct and " + str(incorrect) + " wrong.")

                # askes the user if they want to retry the quiz
                print("Press any key to take the quiz again. (0 to exit) ",end='')
                userAnswer = str(input())

                if userAnswer == "0":
                        exit()
                elif userAnswer != "0":
                        runQuiz()
                #else:print("User answer is invalid")

runQuiz()

        
