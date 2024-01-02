"""
You may only use W3Schools Python for this or Python.org documentation (https://docs.python.org/3/)

Create a calculator that converts Celsius to Fahrenheit and Fahrenheit to Celsius.
Formulas: 
F = C * (9/5) + 32
C = (F - 32) * (5/9)

* Create a function to convert F to C
* Create a function to convert C to F
* Ask the user the current temperature
* Ask the user if that is in F or C.
* If it is F, run the function to convert it to C and output to the console.
* If it is C, run the function to convert it to F and output to the console.
* Create a loop that asks the user if they would like to convert another temperature. If so, run again, else exit.
Submission:
Commit your code to github and submit the link along with screenshots of your code and it running.
"""
#! Create a function to convert F to C
def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * (5/9)

#! Create a function to convert C to F
def convert_c_to_f(celsius):
    return celsius * (9/5) + 32

# Function to run conversion
def temperature_converter():
    #! Create a loop that asks the user if they would like to convert another temperature. If so, run again, else exit.
    while True:
        # Ask the user the current temperature
        temp = float(input("Enter the temperature: "))
        # Ask the user if that is in F or C.
        unit = input("Is this temperature in Fahrenheit (F) or Celsius (C)? Enter F or C: ").upper()

        #! If it is F, run the function to convert it to C and output to the console.
        if unit == "F":
            print(f"{temp}° Fahrenheit is {convert_f_to_c(temp):.2f}° Celsius.")
        #! If it is C, run the function to convert it to F and output to the console.
        elif unit == "C":
            print(f"{temp}° Celsius is {convert_c_to_f(temp):.2f}° Fahrenheit.")
        # Hmmm... There's an error.
        else:
            print("Invalid unit. Please enter either 'F' for Fahrenheit or 'C' for Celsius.")

        #! Checking if the user wants to convert another temperature, if so, loop continues, else exits.
        run_again = input("Would you like to convert another temperature? (yes/no): ").lower()
        if run_again != "yes":
            print("Thanks. Stay warm.")
            break

temperature_converter()
