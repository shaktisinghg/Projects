questions = [
    ["What is the output of print(2 + 3 * 4)?",
     "20",
     "14",
     "24",
     "10",
     "2"],

    ["Which data type is used to store True or False values in Python?",
     "int",
     "str",
     "bool",
     "list",
     "3"],

    ["What does len() function do in Python?",
     "Returns data type",
     "Counts number of elements",
     "Adds elements",
     "Removes elements",
     "2"],

    ["Which symbol is used for single-line comments in Python?",
     "//",
     "#",
     "/* */",
     "--",
     "2"],

    ["What is the correct file extension for Python files?",
     ".pt",
     ".pyt",
     ".py",
     ".python",
     "3"]
]


prizes = [100000, 320000,4000000, 5000000, 10000000, ]
i = 0
for question in questions:
    print(question[0])
    print(f'a. {question[1]}')
    print(f'b. {question[2]}')
    print(f'c. {question[3]}')
    print(f'd. {question[4]}')

    check = input('Enter your answer: \n')
    if check == question[5]:
        print('correct answer!')

        print(f'you won {prizes[i]}')
        i += 1
    else:
        print('Better luck next time!')
        break

