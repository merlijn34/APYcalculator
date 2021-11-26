#estimated yearly interest 

print('How many years will you be saving?')
years = int(input('Enter years: '))

print('How much money is currently in your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan on investing monthly')
monthly_invest = float(input('Enter amount: '))

print('What is the APY (yearly interest rate)')
interest = float(input('Enter interest in decimal numbers (10% = 0.1): '))

print(' ')

# get yearly investment
monthly_invest = monthly_invest * 12
final_amount = 0

# calculate the yearly interest, if the final amount is 0 then the final amount is principal
for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

# give user the answer
print('This is how much money you would have in your account after {} years: '.format(years) + str(round(final_amount, 3)))