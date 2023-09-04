import time
from question_model import Question  # it has two attributes qn and ans
from data import question_data as q_data  # all qn collection
from quiz_brain import Brain as Brain  # literally the brain
import graphics  # for the graphics
import os

print(graphics.img)

q_bank = []

for i, question in enumerate(q_data):  # repeats till end of list and  stores the iteration number in i
    qn_to_obj = (Question(q_data[i]["text"], q_data[i]["answer"]))  # passing qn and ans from
    # q_data as question object to qn_to_obj instance of the class Question
    q_bank.append(qn_to_obj)  # the passed question objects are appended(which contains qn and & rly of each qn)
# after the loop the q_bank is filled with Question object that contain both ans and qn

ask = Brain(q_bank)  # creating an instance ask for class brain and passing q_bank

for i in range(0, len(q_bank)):
    ask.next_q(i)  # accessing next method in class brain through ask instance
    ask.checker(i)  # accessing checker method in class brain through ask instance
    if "yes" != input("Do you want to continue:- ").lower():  # option to quit in middle
        break
    print("\n")
    os.system('CLS')
print(f"Your final score is :- {ask.score} on {i+1}")  # printing final score
time.sleep(3)
