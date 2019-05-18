"""Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input      Expected Output

AAAABBBBCCCCCCCC  4A4B8C"""

def encode(message):
    
    name = message
    output = ''
    count = 1

    for i in range(len(name)):
        if i < len(name)-1 and name[i] == name[i+1]:
            count += 1
        else:
            output += str(count) + name[i]  
            count = 1
    
    return output        
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
