# import time
# my_time=int(input("enter the time in seconds:"))

# for x in reversed(range (0,my_time)):  
#     print(x)
#     time.sleep(0.1)  # it is used to pause the time 
    
# print("Times up!")

# import time
# my_time=int(input("enter the time in seconds:"))

# for x in range (my_time,0,-1):  
#      print(x)
#      time.sleep(1)
    
# print("Times up!")


import time
my_time=int(input("enter the time in seconds:"))

for x in range (my_time,0,-1):
    
    hours= int(x / 3600) % 24                       # int helps in removing the decimal
    minutes = int(x / 60 ) % 60                     #  the value of x is in seconds
    seconds = x % 60                                #  % is used for remainder 
    print(f"{hours}:{minutes}:{seconds}")           #  in seconds %60 is used for remainder
    time.sleep(0.01)
print("blast!")


