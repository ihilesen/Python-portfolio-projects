name = input('What is your first name? ')
print(f'Welcome to {name}\'s Tip Calculator')
total_bill = float(input('What is the total bill? $'))
tip_percentage = float(
    input('What percentage tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people are splitting the bill? '))
bill_with_tip = total_bill * (1 + tip_percentage / 100)
amount_per_person = bill_with_tip / number_of_people
print(f'Each person should pay: ${amount_per_person:.2f}')
