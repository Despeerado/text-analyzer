from task_template import TEXTS
# users

users = {"bob": "123", "ann": "pass123",
         "mike": "password123", "liz": "pass123"}

# login

user_name = input("Login:")
user_password = input("password:")

# login validation

if users.get(user_name) == user_password:
    print("Welcome to the app,", user_name)
    print("We have 3 texts to be analyzed.")
    text = input("Enter a number btw. 1 and 3 to select:")

# Tuto cast jsem  opravil jen castecne, i kdyz jsem ji mel zmenit "pri takto nizkem poctu voleb bych sel radeji cestou
# "if text in ["1", "2", "3"]" - potom nemusis kontrolovat rozsah a ani format"
# duvodem je pozadovana operace v zadani - bud "input je jine cislo –> upozorni uzivatele a ukonci program",
# nebo "vstup je neciselny znak -> upozorni uzivatele a ukonci program".

    if text.isdigit():
        index = int(text)
        if 1 <= index <= 3:
            element = TEXTS[index - 1]

            # removing punctuation

            # punctuation_marks = [".", ",", "!", "?", ":", "\n"]
            punctuation_marks = r"[., ?!:\n]"

            for mark in punctuation_marks:
                element = element.replace(mark, " ")
            words = element.split()
            word_count = len(words)
            print("There are", word_count, "words in the selected text.")

            title_case = 0
            upper_case = 0
            lower_case = 0
            digit_count = 0
            numeric = list()

            words_length = {}

            for word in words:
                if word.istitle():
                    title_case += 1
                elif word.isupper():
                    upper_case += 1
                elif word.islower():
                    lower_case += 1
                elif word.isdigit():
                    digit_count += 1
                    numeric.append(word)
            print("There are", title_case, "titlecase words.")
            print("There are", upper_case, "uppercase words.")
            print("There are", lower_case, "lowercase words.")
            print("There are", digit_count, "numeric strings.")

            total_sum = 0
            for num in numeric:
                total_sum += int(num)
            print("The sum of all the numbers is", total_sum)

            # pocet vyskytu

            # pracuji s promennou words, kde je text ocisten o interpunkcni znamenka
            # vrati list hodnot - kazda predstavuje delku kazdeho jednotliveho slova

            word_char_counts = list()

            for i in words:
                word_char_counts.append(len(i))

            dictionary = {}

            for z in word_char_counts:
                if z in dictionary:
                    dictionary[z] += 1
                else:
                    dictionary[z] = 1

            ordered = dict(sorted(dictionary.items()))

            # vytiskne tabulku

            print("LEN".ljust(3), "|", "OCCURENCES".ljust(12), "|", "NR.")
            print("-" * 25)

            for key, value in ordered.items():
                print('{:<5} {:<15} {}'.format(key, '*' * value, value))

        else:
            print("Text does not exist, terminating the program..")
    else:
        print("You did not enter the number, terminating the program..")
else:
    print("unregistered user, terminating the program..")
