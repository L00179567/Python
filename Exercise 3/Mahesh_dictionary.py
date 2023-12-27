########################
Dictionaries
Coding with Dictionaries  By: Sai Mahesh
Use below methods-
my_dictionary.keys()
my_dictionary.values()
my_dictionary.items()
21OCT2023
'''

#Make the first dictionary.
print("*********************************************************************************************************")
my_dictionary={"Company Name": "Accenture", "Industry": "IT", "Total Employees": "1000+"}
#Print whole sentence
print('Company details are :' , (my_dictionary))
#Use dict.key to show key 
print (my_dictionary.keys())
#Use dict.values to show actual values
print (my_dictionary.values())
#Use dict.item to show keys and values
print (my_dictionary.items())

print("*********************************************************************************************************")

#Update the company name and employee count now.
my_dictionary["Company Name"] = "Capegemini"
my_dictionary["Total Employees"] = "1500+"

print("Update company name to Capegemini")
print('Company details after update :' , (my_dictionary))

print("*********************************************************************************************************")
