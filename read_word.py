import csv

word_file = "words.txt"

with open(word_file) as csv_file:
    # csv_file is the file handler
    # lines are all the lines from file
    lines = csv.reader(csv_file)
    for data_list in lines:
        question=data_list[0]
        answer = data_list[1]
        print ("question: " + question + "=> answer: " + answer)