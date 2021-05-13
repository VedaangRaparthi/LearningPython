#This is a converter built to obtain the continuous compounding rate from a discrete compounding rate, and vice versa.

import math

which_conv = int(input('''Convert discrete rate to continuous rate: 0
Convert continuous rate to discrete rate: 1
What do you want to do? '''))
if which_conv == 0:
	#discrete to continuous
	years = int(input('Number of years: '))
	times_per_year = int(input('Times compounded per year: '))
	rd = float(input('Discrete rate of compounding per year(%): '))
	cont_rate_per_year = ((times_per_year)*math.log(1+(rd/100)/times_per_year))*100
	print()
	print('Continuous rate of compounding per year (%):', cont_rate_per_year)
	print('Continuous rate of compounding per time period (%):', cont_rate_per_year/times_per_year)
elif which_conv == 1:
	#continuous to discrete
	years = int(input('Number of years: '))
	times_per_year = int(input('Times compounded per year: '))
	rc = float(input('Continuous rate of compounding per year(%): '))
	disc_rate_per_year = (pow(math.exp(rc/100),(1/times_per_year))-1)*times_per_year*100
	print('Discrete rate of compounding per year (%):', disc_rate_per_year)
	print('Discrete rate of compounding per time period (%):', disc_rate_per_year/times_per_year)
else:
	print('Invalid input.')
