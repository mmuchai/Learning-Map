learning_map_dict= {}
def run():
   x = True
   
   while True:
       ui()
def ui():
   a = input('What do you want to do? \n Select \n "1" to add \n "2" to view: ')
   if a == "1":
       user_input1 = input('Do You want to add a new skill or add a studied skill? \n Select \n "1" to add new skill \n "2" to add studied skill: ')
       if user_input1 == "1":
           new_skill = input('Add your new skill:')
           learning_map_dict[new_skill] = 0
           ui()
               
       elif user_input1 == "2":
           studied_skill = input("Add a studied skill:")
           learning_map_dict[studied_skill]=1
           ui()
       
       else:
           print("Invalid Selection")
   elif a == "2":
       user_input2 = input('Select \n "1" to view all skills \n "2" to view studied skills \n "3" to view unstudied skills \n "4" to view progress: ')
       if user_input2 == "1":
           print("View All Skills: ")
           learning_list=[]
           for skill in learning_map_dict.keys():
               learning_list.append(skill)
           print(learning_list)