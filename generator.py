import csv
import random
import time
import secrets
from datetime import datetime
from datetime import timedelta


def replace_chars(word):

    word = word.replace('č','c')
    word = word.replace('ć','c')
    word = word.replace('š','s')
    word = word.replace('ž','z')
    word = word.replace('đ','d')

    return word



def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)

    date_final = start + timedelta(seconds=random_second)
    return date_final.date()



def random_oib(num):
	min = pow(10, num-1)
	max = pow(10, num) - 1
	return random.randint(min, max)



def mail_format(name, surname, date, choice):
    name = replace_chars(name.lower())
    surname = replace_chars(surname.lower())

    year_of_birth = str(date.year)

    if choice == 1:
        return name + surname + '@gmail.com'
    
    elif choice == 2:
        return name + surname[0] + '@gmail.com'

    elif choice == 3:
        return name[0] + surname + '@gmail.com'

    elif choice == 4:
        return name[0] + surname + year_of_birth[-2:] +'@gmail.com'
    
    elif choice == 5:
        return name + surname[0] + year_of_birth[-2:] +'@gmail.com'

    elif choice == 6:
        return name[0] + surname + year_of_birth +'@gmail.com'
    
    elif choice == 7:
        return name + surname[0] + year_of_birth +'@gmail.com'



start_time = time.time()



with open('data/names.csv', 'r',encoding='utf-8') as names_csv,\
     open('data/surnames.csv', 'r',encoding='utf-8') as surnames_csv,\
         open('data/people.csv', 'w', encoding='utf-8', newline='') as people_csv:
    name_reader = csv.reader(names_csv, delimiter = ',')
    surname_reader = csv.reader(surnames_csv, delimiter = ';')
    people_writer = csv.writer(people_csv, delimiter = ',')

    people_writer.writerow(['ID', 'Name', 'Surname', 'E-Mail', 'OIB', 'Date_birth'])

    # Skip header
    next(name_reader, None)

    #Skip header
    next(surname_reader, None)
    next(surname_reader, None)
    next(surname_reader, None)

    names_list = []
    surnames_list = []

    for name in name_reader:
        names_list.append(name[0])
    

    for surname in surname_reader:
        surnames_list.extend(surname[3:12])


    names_list = [name for name in names_list if name != '']  
    surnames_list = [surname for surname in surnames_list if surname != '']    

    names_set = set(names_list)
    surnames_set = set(surnames_list)

    id = 0

    date_start = datetime.strptime('1/1/1950', '%d/%m/%Y')
    date_finish = datetime.strptime('31/12/1999', '%d/%m/%Y')

    for person in range(1, 500):
            
        date_of_birth = random_date(date_start, date_finish)

        random_name = random.choice(list(names_set))
        random_surname = random.choice(list(surnames_set))
        
        oib = random_oib(11)

        random_mail = mail_format(random_name, random_surname, date_of_birth, random.randrange(1,5))

        people_writer.writerow([id, random_name.capitalize(), random_surname.capitalize(), random_mail.lower(), oib, date_of_birth])

        id += 1

print('Execution time: %s seconds.' % (time.time() - start_time))