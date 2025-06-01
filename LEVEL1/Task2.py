unit=input("Enter the unit of temperature (C/F):" )
temp=float(input("Enter the Temperature to convert:" ))
if unit=='C':
    convert_into_Fahrenheit= (9/5 * temp) + 32
    print("Temperature converted from Celsius to fahrenheit is" ,convert_into_Fahrenheit)
elif unit == 'F':
    convert_into_Celsius = (5/9 * temp) - 32
    print("Temperature converted from Fahrenheit to Celsius is:" ,convert_into_Celsius)
else:
    print("Invalid unit")
 