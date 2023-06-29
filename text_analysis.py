# text-analysis.py: první projekt do Engeto Online Python Akademie

# author: Dominik Beran
# discord: Dominik B. / Despeerado#8409
# email: d.beran27@gmail.com

# Vyžádá si od uživatele přihlašovací jméno a heslo,
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
# pokud není registrovaný, upozorni jej a ukonči program.**

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

#     Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
#     pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

# Pro vybraný text spočítá následující statistiky:

#     počet slov,
#     počet slov začínajících velkým písmenem,
#     počet slov psaných velkými písmeny,
#     počet slov psaných malými písmeny,
#     počet čísel(ne cifer),
#     sumu všech čísel(ne cifer) v textu.

# Program zobrazí jednoduchý sloupcový graf,
# který bude reprezentovat četnost různých délek slov v textu.

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

    if text.isdigit():
        index = int(text)
        if 1 <= index <= 3:
            element = TEXTS[index - 1]

            # removing punctuation

            punctuation_marks = [".", ",", "!", "?", ":"]

            for mark in punctuation_marks:
                element = element.replace(mark, "")
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

            # vrati list hodnot - kazda predstavuje delku slova
            result = list()
            for i in range(max(word_char_counts)):
                result.append(word_char_counts.count(i))

            # serazeni hodnot ve word_char_counts
            sorted_word_char_counts = sorted(result, reverse=True)

            # puvodni funkce pocitaji vyskyty, ale taky byla spatne

            word_occurence = dict()
            for word in words:
                if word not in word_occurence:
                    word_occurence[word] = 1
                else:
                    word_occurence[word] = word_occurence[word] + 1

            values = word_occurence.values()
            values_list = list(values)
            sorted_values = sorted(values_list, reverse=True)
            top_3_values = sorted_values[:3]

            results = list()

            for occurence in word_occurence:
                if word_occurence[occurence] in top_3_values:
                    results.append((word_occurence[occurence], occurence))

        else:
            print("Text does not exist, terminating the program..")
    else:
        print("You did not enter the number, terminating the program..")
else:
    print("unregistered user, terminating the program..")
