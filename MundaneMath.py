min=int(input("Enter the minium value: "))
max=int(input("Enter the maximum value: "))
total=0	
for num in range(min,max):
	if(num%2==0):
# If the reminder of the number comes to be 0, then it is an even number.
		total=total+num
print ("The sum of even numbers between {0} and {1} is".format(min,max),total)