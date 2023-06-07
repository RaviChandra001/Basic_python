# while loop --> same as for loop but number of iteratio is not known in while loop 

# i=0
# while i<10:
#     print(i)  # It gives you a infinte loop 

# To solve it use the break keyword 
i=0
while i<10:
    print(i)
    break  # print 0

# Printing values from 1 to 50 
i=0
while i<50:
    print(i)
    i += 1  # Number from 0 to 49 
else:
    print("Value from 1 to 50 is printed ")

# Another case in python 
while 50 < 50:
    print("hello")
else:
    print("Outsiding the while loop ")


# Another example
i =0
while i<50:
    print(i)
    i=i+1
    break
else:
    print("Done with all the work")
    
# Break statemnt example of while loop

while True:
    response = input("say something: ")
    if (response == 'hii'):
        print("Hello this side ravi!")
    elif(response == 'hi'):
        print("hello here is ravi again")
    elif(response == 'bye' or response == 'Bye'):
        break

