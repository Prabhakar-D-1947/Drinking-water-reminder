import time
print(time.strftime("%H:%M:%S"))
if(0<int(time.strftime("%H"))<12):
 print("Good morning")
elif(12<=int(time.strftime("%H"))<20):
 print("Good Evening")
else:
 print("Good Night")
print(time.strftime("%D   %h %m"))

