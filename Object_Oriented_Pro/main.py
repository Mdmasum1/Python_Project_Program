
from question_model import Questions
from data import question_data

question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    #Now create this new question object and saved it in the varoable 
    #new_question
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_question():#if quiz still has questions remaining;
    
    quiz.next_question()

