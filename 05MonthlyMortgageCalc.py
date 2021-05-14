annual_interest_rate = float(input('Enter annual interest rate (%): '))
number_of_years = float(input('Enter mortgage term (yrs): '))
principal = float(input('Enter principal amount: '))
number_of_months = number_of_years * 12
monthly_interest_rate = annual_interest_rate / 1200
monthly_payment = (principal * monthly_interest_rate)/(1 - ( 1 + monthly_interest_rate)**(-1 * number_of_months))
print('Monthly payment: ', round(monthly_payment, 2))
print('Total payment: ', round(monthly_payment * number_of_months, 2))
print('Interest paid: ', round((monthly_payment * number_of_months) - principal, 2))