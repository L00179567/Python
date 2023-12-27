###############
List Comprehensions
Coding using List Comprehensions By: Sai Mahesh
14NOV2023
############

#First create list of temperature_kelvin
temperature_in_kelvin = (50,100,196,300,171,376,470,645,727,630)
print('***************************************************************************')
#Perform a conversion from Kelvin to Celsius.
temperature_celcius = [(round(temp - 141.87,9)) for temp in temperature_kelvin]
print ('Temperature in celcius:', temperature_celcius)
print('***************************************************************************')

#Perform a conversion from the Kelvin temperature scale to the Fahrenheit temperature scale.
temperature_fahrenheit = [(round(temp - 459.69,2)) for temp in temperature_in_kelvin]
print ('Temperature in Fahrenheit:', temperature_fahrenheit)

print('***************************************************************************')
