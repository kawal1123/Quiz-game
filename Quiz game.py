def quiz():
    print("Quiz Game")
    print("Do this game with your calculation .don,t use calculater and internet for answers")
    Correct_answer = 0
    wrong_answer = 0
    print("1:What is multiplication of this numbers 5,6,8,2,7 ?")
    print("options")
    first={
        "option1":5262,"option2":3360,"option3":8255,"option4":3365
    }
    print(first)
    answer = 3360
    ans = int(input("Enter your answer: "))
    if ans == answer:
        print("Right", "\U0001f601")
        Correct_answer += 1
    else:
        print("wrong")  
        wrong_answer +=1 
    #Question 2
    print("2 : What is sqaure of  4?")
    print("options") 
    second = {
    "option1":20,"option2":54,"option3":16,"option4":201
    }
    print(second)
    answer2 = 16
    ans2 = int(input("Enter your answer : "))
    if ans2 ==answer2:
        print("your answer is right","\U0001f602")
        Correct_answer += 1
    else:
        print("wrong answer")
        wrong_answer +=1 

    #Question 3
    print("3 How many states in India?")
    print("option")
    third = {
        "option1":20,"option2":27,"option3":32,"option4":29
    }
    print(third)
    answer3 = 29
    ans3= int(input("Enter your answer: "))
    if ans3 ==answer3:
        print("Right answer","\U0001f603")
        Correct_answer += 1
    else:
        print("wrong")
        wrong_answer +=1 
    #Question 4
    print("What is factorial of 5?")
    print("option")
    fourth = {
        "option1":100,"option2":120,"option3":125,"option4":130
    }
    print(fourth)
    answer4 = 120
    ans4 =int(input("Enter the number : "))
    if ans4 ==answer4:
        print("Right answer ","\U0001f604")
        Correct_answer += 1
    else:
        print("wrong")
        wrong_answer +=1 
    #Question5
    print("which one is leap year?")
    print("option")
    fifth ={
        "option1":2003,"option2":2009,"option3":2011,"option4":2020
    }
    print(fifth)
    answer5 =2020
    ans5=int(input("Enter your Answer: "))
    if ans5 == answer5:
        print("Right answer","\U0001f605")
        Correct_answer += 1
    else:
        print("wrong")  
        wrong_answer +=1      
    print("Correct answers" ,"=",Correct_answer) 
    print("Wrong answers","=",wrong_answer)    
    if Correct_answer ==1 and wrong_answer == 4:
        print("Your win percentage is only 20 %")
    elif Correct_answer == 2 and wrong_answer ==3:
        print("Your win percentage is only 40 %")
    elif Correct_answer == 3 and wrong_answer ==2:
        print("Your win percentage is 60 % ")
    elif Correct_answer == 4 and wrong_answer == 1:
        print("Your win percentage is 80 % ")
    elif Correct_answer== 5 and wrong_answer == 0:
        print("Your win percenatge is 100 %","\U0001f606")   
    else:
        print("*******your all answers are wrong*******")

quiz()    
