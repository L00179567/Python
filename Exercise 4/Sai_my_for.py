###########
Loop- For
Coding using For loop  By: Sai Mahesh
18NOV2023
###############

print ('*******************************************************************************')
#Verify the parity of numbers in a given list.
iterable_variable = [21,22,23,24,25,26,27,28,29,30]

for item in iterable_variable:
     if item %2 != 0:
        print('Odd numbers from list',item)
for item in iterable_variable:
    if item %2 == 0:
        print('Even numbers from list',item)


print ('*******************************************************************************')
#Utilise the scan.items function to obtain the desired output.
scan = {"SITA": "Cloud Engineer", "Optum": "Data Analyst", "Deloitte": "Cloud Architect"}
for Organisation, Department in scan.items():
    print(f"Found best Jobs in Organisation : At {organisation} best Department is {department}")
 
print ('*******************************************************************************')
  

