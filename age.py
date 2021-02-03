driving = input('Have you driven vehicles before?')
if driving != 'Yes' and driving !='No':
	print('Please enter Yes or No')
	raise SystemExit

age = input ('How old are you?')
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print ('Ok')
	else:
		print ('You should not have at this age')
elif driving == 'No':
	if age >= 18:
		print('Consider a driving license')
	else:
		print('Consider a driving license after 18')
