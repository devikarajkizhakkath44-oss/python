user_input= input("enter the list of integers separated spaces :")
result = []
for num in user_input.split():
 if int(num)>100:
   result.append('over')
 else:
   result.append(int(num))
print("modified list",result)