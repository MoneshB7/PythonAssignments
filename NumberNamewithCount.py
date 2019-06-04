"""Input given is an integer value. Count number of a particular digit in the integer and append it to a list in the format given below, following the same order of their appearance.
Example:
number = 523115
output_list = ['FIVE-2', 'TWO-1', 'THREE-1', 'ONE-2']"""

num = 523115
str_num = str(num)
list1=[]
list2=[]
value =""
for i in range(0,len(str_num)):
    if str_num[i] == "1":
        value ="ONE-"+str(str_num.count("1"))
        list1.append(value)
        str_num1 = str_num.replace("1","")
    elif str_num[i] == "2":
        value ="TWO-"+str(str_num.count("2"))
        list1.append(value)
        str_num1 = str_num.replace("2","")
    elif str_num[i] == "3":
        value ="THREE-"+str(str_num.count("3"))
        list1.append(value)
        str_num1 =str_num.replace("3","")
    elif str_num[i] == "4":
        value ="FOUR-"+str(str_num.count("4"))
        list1.append(value)
        str_num1 = str_num.replace("4","")
    elif str_num[i] == "5":
        value ="FIVE-"+str(str_num.count("5"))
        list1.append(value)
        str_num1 = str_num.replace("5","")
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
