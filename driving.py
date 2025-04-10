#conditional statements
name=str(input("enter your name:"))
print(f"{name} please write your age for driving  information. Note only 18 above and less than 60 yeasrs old people can apply for it")
age=int(input("enter your age->:"))
if age >= 18 and age <= 60 :
    message="can drive"
    
elif age < 18 :
    message="can't drive"
elif age >= 60 and age <= 80:
    message="please can't drive your age is like as old man or women"
elif age >= 80 and age <=100:
    message="please can't drive your age is too much"
else:
    message="can't do anything"
print(message)





