"""Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
 
1. Always num1 should be less than num2

2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied

      a. Sum of the digits of the number is a multiple of 3

      b. Number has only two digits

      c. Number is a multiple of 5

3. Display the maximum element from the list

In case of any invalid data or if the list is empty, display -1."""

def find_max(num1, num2):
    list2=[]
    max_num=-1
    count = 0
    temp = 0
    list1=list(range(num1,num2+1))
    print(list1)
    if num1>num2:
         print("-1")
    else:
        for i in range(0,len(list1)+1):
            temp = list1[i]
            while temp!=0:
                temp=temp//10
                count+=1
            if count%3==0 and temp%5 ==0 and len(str(temp)) == 2:
                    list2.append(temp)
                    print(list2)
            else:
                    pass

        list2.sort()
        max_num = list2[-1]

    return max_num
max_num=find_max(10,15)
print(max_num)
