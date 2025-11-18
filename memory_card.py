#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QGroupBox,
    QButtonGroup,
)
from random import randint, shuffle

class Questions():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



#instance of app
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')

#Question
labelquestion = QLabel('Which nationality does not exist?')
layoutline1 = QHBoxLayout()
layoutline1.addWidget(labelquestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

#radiobutton
#create the radiobutton
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
#create groupbox
RadioGroupBox = QGroupBox('Answer Options')

#create RadioGroup
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#manage the QRadio button
layoutansmain = QHBoxLayout()
layoutans_sub1 = QVBoxLayout()
layoutans_sub2 = QVBoxLayout()


layoutans_sub1.addWidget(rbtn_1)
layoutans_sub1.addWidget(rbtn_2)

layoutans_sub2.addWidget(rbtn_3)
layoutans_sub2.addWidget(rbtn_4)

layoutansmain.addLayout(layoutans_sub1)
layoutansmain.addLayout(layoutans_sub2)

#combine groupbox + main layout

RadioGroupBox.setLayout(layoutansmain)

#Test Results
AnswerGroupBox = QGroupBox("Test Result")
label_result = QLabel("Are you correct or not?")
label_correct = QLabel("The answer will be here!")

layout_result = QVBoxLayout()

layout_result.addWidget(label_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(label_correct, alignment = Qt.AlignHCenter, stretch=2)
AnswerGroupBox.setLayout(layout_result)


#create another line
layoutline2 = QHBoxLayout()
layoutline2.addWidget(RadioGroupBox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutline2.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()

#Button
answerbutton = QPushButton('Answer')
layoutline3 = QHBoxLayout()
layoutline3.addWidget(answerbutton, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

#All function we need
def show_Result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    answerbutton.setText("Next Questions")
def show_Question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    answerbutton.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers =  [rbtn_1,rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    labelquestion.setText(q.question)
    label_correct.setText(q.right_answer)
    show_Question()

def show_correct(res):
    label_result.setText(res)
    show_Result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")
        window.score += 1
        print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
        print('Rating: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect!")
            print('Rating: ', (window.score/window.total*100), '%')
def next_questions():
    window.total += 1
    print('Statistics\n-Total Questions: ', window.total, '\n-Right Answers: ', window.score)
    cur_questions = randint(0, len(Questions_list) - 1)
    q = Questions_list[cur_questions]
    ask(q)
def click_OK():
    if answerbutton.text() == 'Answer':
        check_answer()
    else:
        next_questions()


#create groupbox
#main layout app
layoutcard = QVBoxLayout()
layoutcard.addLayout(layoutline1)
layoutcard.addLayout(layoutline2)
layoutcard.addLayout(layoutline3)

window.setLayout(layoutcard)

#ask(
 #   'The national language of Indonesia',
  #  'Bahasa Indonesia',
   # 'English',
    #'Japanese',
    #'Arabic'
#answerbutton.clicked.connect(check_answer)

#q = Questions("Select the most apropriate English name for the programming conecpt to store some data",
 #             "variable",
  #            "variation",
   #           "variant",
    #          "changing",
#)
#ask(q)
Questions_list = []
Questions_list.append(Questions("The state language of Brazil","Portugese","English","Spanish","Brazillian"))
Questions_list.append(Questions("Solve the equation: 12-(-3) x {1/4 ÷ [-1/2]2}","15","2","12","18"))
Questions_list.append(Questions("How many people need to gather for the probability of 2 sharing a birthday to exceed 50%?","23","78","183","365"))
Questions_list.append(Questions("Milk is made from nutrients in a cow’s blood. How many litres of blood are needed to make 1 litre of milk?","450","10","5","20"))
Questions_list.append(Questions("50 zoo animals are flipped over sequentially. What was the lion’s number in the sequence?","17","45","05","21"))


answerbutton.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_questions()

window.show()
app.exec()
