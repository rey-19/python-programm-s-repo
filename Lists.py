new_list=['Reyansh','Jhansi',"Pradeep",'Namratha']
print(len(new_list)) #len() finds the length 
new_list.append("Jhansi") #append() method to permanently add an item to the end of a list
print(new_list)
new_list.pop(1) #pop() removes a particular item in a list(u need to add the appropriate index)
print(new_list)
new_list.reverse()#reverses items 
print(new_list)
new_list.sort()#sort's items in an alphabetical order 
print(new_list)

num_1=['1','2','3']
num_2=['4','5','6']
num_3=['7','8','9']
keypad=[num_1,num_2,num_3]
print(keypad[2][1])