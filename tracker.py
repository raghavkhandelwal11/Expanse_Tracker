# Monthly expense tracker
import json;

import datetime;
from record import *;
from income_and_budget import income, budget, utilised;

monthly_income = None
monthly_budget = None
monthly_utilised = 0

local_records = []



def update_variables():
    global monthly_budget
    global monthly_income
    global monthly_utilised
    global local_records

    with open('income_and_budget.py', 'r') as f:


        monthly_income = str(f.readline()).split('=')[1].replace('\n', '')
        monthly_budget = str(f.readline()).split('=')[1].replace('\n', '')
        monthly_utilised = str(f.readline()).split('=')[1].replace('\n', '')

        if 'None' in monthly_income:
            monthly_income = None
        else:
            monthly_income = float(monthly_income)

        if 'None' in monthly_budget:
            monthly_budget = None
        else:
            monthly_budget = float(monthly_budget)

        if 'None' in monthly_utilised:
            monthly_utilised = None
        else:
            monthly_utilised = float(monthly_utilised)
        

    with open('record.py', 'r') as f1:
         local_records = json.loads(((f1.readline()).split('=')[1].replace('\n', "")).replace('\'', '\"'))

    #print(monthly_income, monthly_budget, monthly_utilised, local_records)

    print('printing local records', local_records)


def updated_files():
    global monthly_budget
    global monthly_income
    global monthly_utilised
    global local_records

    with open('income_and_budget.py', 'w') as file:
        file.write('income = {0} \nbudget = {1} \nutilised = {2}'.format(monthly_income, monthly_budget, monthly_utilised))

    with open('record.py', 'w+') as f:
        f.write('all_records = {}'.format(local_records))

    


def select_category():
    category_types = ['Food', 'House Rent', 'Medical', 'Tranport', 'EMI', 'Premium', 'Others']
    category = ''
    text = 'Type one of the following and press enter: \n \t Food \n \t House Rent \n \t Medical \n \t Transport \n \t EMI \n \t Premium \n \t Others \n'
     #to take input for monthly expense budget
    while(category not in category_types):
        category = str(input(text))
        if (category not in category_types):
            print("Enter a valid category \n")
        else:
            return category


def enter_amount():
    global monthly_utilised
    amount = None
    text = 'Type a valid amont (numbers only): '
     #to take input for monthly expense budget
    while(type(amount) == None or type(amount) != float):
        amount = input(text)
        if (not amount.isdigit()):
            print("Enter a valid amount \n")
        else:
            with open('income_and_budget.py', 'w+') as file:
                monthly_utilised += float(amount)
                file.write("income = {0} \nbudget = {1} \nutilised = {2}".format(monthly_income, monthly_budget, monthly_utilised))
                updated_files()
            return float(amount)


def add_expense(): 
    global local_records
    category_types = ['Food', 'House Rent', 'Medical', 'Tranport', 'EMI', 'Premium', 'Others']

    date = datetime.datetime.now()
    category = ""
    amount = None
    description = ""

    entry = {
        "date": date.strftime('%d/%m/%Y'),
        "category": select_category(),
        "amount": enter_amount(),
        "description": str(input('Enter a description: '))
    }

    #from record import all_records
    with open('record.py', 'w+') as f:
            local_records.append(entry)
            f.write('all_records = {}'.format(local_records))
            print('\n \n \n Successfully Added \n \n \n')
    

    choose_action()


def reset_tracker():
    global monthly_budget
    global monthly_income
    global monthly_utilised
    global local_records

    with open('record.py', 'w+') as f:
        f.write('all_records = []')

    with open('income_and_budget.py', 'w+') as file:
        file.write('income = {0} \nbudget = {1} \nutilised = {2}'.format(None, None, 0))

    print('reset done')
    
    #update_variables()
    monthly_budget = None
    monthly_income = None
    monthly_utilised = 0
    local_records = []
    set_income_and_budget()


def display_all_entries():

    global monthly_budget
    global monthly_income
    global monthly_utilised
    global income
    global budget
    global utilised

    update_variables()
    
    print('\n \n ---------Summary----------- \n \nIncome = {0} INR \nBudget = {1} INR \nUtilised = {2} INR \n \n -----------All Entries----------- \n'.format(monthly_income, monthly_budget, monthly_utilised))


    for obj in local_records:
        print('\n \n \t {0} =>  {1} Rupees spent on {2}  \n \t Discription => {3} \n'.format(obj['date'], obj['amount'], obj['category'], obj['description']))

    # monthly_budget = budget
    # monthly_income  = income
    # monthly_utilised = utilised

    choose_action();    


def choose_action():

    #update_variables()
    updated_files()

    text = '\n What do you want to do? \t \n - Enter 1 for adding expense \t \n - Enter 2 for checking previous month expenditure \t \n - Enter 3 to reset the tracker \t \n - Enter 4 to see total expense and Budget \n'

    response = 0

    response = int(input(text))

    if(response == 1):
        print('You have chosen to add a new entry to expanse list \n')
        add_expense()
    elif(response == 2):
        print('You have chosen to see old records\n')
        display_all_entries()
    elif(response == 3):
        print('You have chosen to reset \n')
        reset_tracker()
        print('\n \n \n Tracker Data Reset Successful \n \n \n')
    elif(response == 4):
        print('You have chosen t see expense and budget \n')
        show_budget()
        print('\n \n \n')
    else:
        set_income_and_budget()    


def set_income_and_budget(): 

    global monthly_budget
    global monthly_income
    global income
    global budget
    global utilised

    update_variables()
    show_all_variables()

    if(monthly_income == None or monthly_budget == None):

    
        #to take input for monthly income
        while((monthly_income == None) or (type(monthly_income) != int)):
            
            monthly_income = int(input('Enter your monthly income: '))
            if (type(monthly_income) != int):
                print("You can only enter the integer value \n")
            else:
                break

        #to take input for monthly expense budget
        while((monthly_budget == None) or (type(monthly_budget) != int)):
            monthly_budget = int(input('Enter your monthly expense budget: '))
            if (type(monthly_budget) != int):
                print("You can only enter the integer value \n")
            else:
                break

        with open('income_and_budget.py', 'w') as file:
            file.write('income = {0} \nbudget = {1} \nutilised = {2}'.format(monthly_income, monthly_budget, 0))

    else:
        update_variables()

    choose_action()


def show_all_variables():

    print('Monthly budget: ', monthly_budget)
    print('Monthly income: ', monthly_income)
    print('Monthly utilised: ', monthly_utilised)

#reset_tracker()

def show_budget():
    update_variables()
    print('Monthly budget: \n', monthly_budget)
    print('You have spent {0} Rs this month \n'.format(monthly_utilised))
    percent = format((monthly_utilised/monthly_budget), '.2f')
    print('Your have utilised {} percent of remaining budget \n'.format(percent))
    print('Remaining amount you can spend is {0} Rs'.format(monthly_budget-monthly_utilised))

set_income_and_budget()






