choice = input("Select conversion method:\n1. From Celsius to Fahrenheit\n2. From Fahrenheit to Celsius\nYour choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in degrees Celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius are equal to {fahrenheit} degrees Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius.")
else:
    print("Wrong choice. Please select 1 or 2.")
