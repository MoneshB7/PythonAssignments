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
    list1=list(range(num1,num2+1))
    if num1>=num2:
        max_num=-1
    else:
        for i in list1:
            temp = i
            temp1=0
            while temp!=0:
                temp1+=temp%10
                temp=temp//10    
            if temp1%3==0 and i%5 ==0 and len(str(i)) == 2:
                    list2.append(i)
        if(len(list2)!=0):
            list2.sort()
            max_num = list2[-1]
        else:
            max_num=-1
    return max_num
max_num=find_max(24,29)
print(max_num)
