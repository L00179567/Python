##########
Loop- If and Else
Coding using If Else loops  By: Sai Mahesh
11NOV2023
############

#Calculate marks scored by student
#Enter your marks
marks=input("Enter your marks:")
print ('Marks obtained', marks)
#Marks Condition
if int(marks) >= 85:
    print ('Grade is Distinction:Excellent')
elif int(marks) >=70 and int(marks) <=80:
    print ('Grade is First Class:Better luck next time')
elif int(marks) >=60 and int(marks) <=69:
    print ('Grade is Second Class:Try hard next time')
elif int(marks) >=50 and int(marks) <=59:
    print ('Grade is Pass Class:Very disappoiting')
else : 
    print ('Failed:Bye Bye')


