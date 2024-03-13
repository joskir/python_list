#an empty list
my_list=[]
#print the list
print(my_list)
#appending items to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#printing the list after appending
print(my_list)
#insert a value at the second position
my_list.insert(1, 15)
#Print the inserted list
print(my_list)
#another list
my_list2=[50,60,70]
#Extend list
my_list.extend(my_list2)
#print extended list
print(my_list)
#remove last element in the list
del my_list[-1]
print(my_list)
#sort my_list in ascending order
my_list.sort()
print(my_list)
#Getting and printing value of 30
value=30
index0f30=my_list.index(value)
print("the idex of 30 is:", index0f30)




