color_list1=input("enter colors in list1 separated by comma: ").split(",")
color_list2=input("enter colors in list2 separated by comma: ").split(",")
for color in color_list1:
   if color not in color_list2:
      print(color)


