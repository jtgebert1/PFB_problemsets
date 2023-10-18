numbers=[101,2,15,22,95,33,2,27,72,15,52]

num_sorted=sorted(numbers)

evens=[]
odds=[]
for number in num_sorted:
	if number%2==0:
		evens.append(number)
	else:
		odds.append(number) 
		
print("Sum of evens:", sum(evens))
print("Sum of odds:", sum(odds))


	
