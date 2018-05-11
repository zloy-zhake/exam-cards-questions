import random
import re

# прочитать файл с теоретическими вопросами
# прочитать файл с практическими вопросами
# запросить количество требуемых наборов (билетов)
# скомбинировать наборы
# заменить нумерацию на 1. 2. 3.
# сохранить результат в файл

# прочитать файл с теоретическими вопросами
with open(file="lecture_questions", mode='r') as lec_q_file:
    lec_questions = list(lec_q_file)

# прочитать файл с практическими вопросами
with open(file="lab_questions", mode='r') as lab_q_file:
    lab_questions = list(lab_q_file)

# запросить количество требуемых наборов (билетов)
n_cards = int(input("Enter a number of cards needed: "))

cards = []
# скомбинировать наборы
for i in range(n_cards):
    l1 = random.sample(population=lec_questions, k=2)
    l2 = random.sample(population=lab_questions, k=1)
    cards.append(l1 + l2)

# заменить нумерацию на 1. 2. 3.
numbers_in_beginning = "^[0-9]+\.? ?"
for card in cards:
    # вычистить старую нумерацию
    for i in range(len(card)):
        if re.match(pattern=numbers_in_beginning, string=card[i]):
            card[i] = re.sub(pattern=numbers_in_beginning,
                             repl='',
                             string=card[i])
    # добавить новую нумерацию
    for i in range(len(card)):
        card[i] = str(i + 1) + ". " + card[i]

# сохранить результат в файл
with open(file="exam cards", mode='w') as res_file:
    for card in cards:
        for question in card:
            res_file.write(question)
        res_file.write('\n')
