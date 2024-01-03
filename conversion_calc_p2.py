"""
Complete "BPA Warm-up  - Temp Conversion 1" first.

Now that you've created a conversion calculator, it's time to record the data. 
Write code to check if "temps_recorded.txt" exists. If it doesn't create it.
Add a function to your code that records the temperature inputted (in F or C), the conversion temp (in F or C) and the date/time it was recorded to the temps_recorded.txt file.
Your function should append temps_recorded.txt to keep a running log of the temps recorded and not overwrite previous recording. 
"""
#? Add imports to read write to text and datetime objects
from datetime import datetime
import os

def record_temperature(original_temp, converted_temp, unit):
    """Record the temperature conversion in temps_recorded.txt."""
    # Determining the filename
    filename = "temps_recorded.txt"

    # Check if the file exists, if not, create it
    if not os.path.exists(filename):
        open(filename, 'w').close()

    # Writing the record to the file
    with open(filename, 'a') as file:
        # Formatting the date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if unit == "F":
            record = f"{current_time}: {original_temp} F -> {converted_temp:.2f} C\n"
        else:
            record = f"{current_time}: {original_temp} C -> {converted_temp:.2f} F\n"
        file.write(record)
        
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
            new_temp = convert_f_to_c(temp)
        #! If it is C, run the function to convert it to F and output to the console.
        elif unit == "C":
            print(f"{temp}° Celsius is {convert_c_to_f(temp):.2f}° Fahrenheit.")
            new_temp = convert_f_to_c(temp)
        # Hmmm... There's an error.
        else:
            print("Invalid unit. Please enter either 'F' for Fahrenheit or 'C' for Celsius.")
        record_temperature(temp, new_temp, unit)
        #! Checking if the user wants to convert another temperature, if so, loop continues, else exits.
        run_again = input("Would you like to convert another temperature? (yes/no): ").lower()
        if run_again != "yes":
            print("Thanks. Stay warm.")
            break

temperature_converter()
