#CT Assignment 8: Weather Forecast Application
#Version 1.0
#All hail the omnisiah
#**********************************************************************************************************************

#Build function to do the temp conversion
def far_to_cel(far):
    cel = (far - 32) * 5.0/9.0
    return cel

#Build main function to handle all the gross stuff like user input and output (ick. . users)
#The emperor protects. .even from users and their sticky fingers.

def main():
    try:
        #Get the user input
        far = float(input("Please enter the temperature in Fahrenheit: "))
        #Call the conversion function
        cel = far_to_cel(far)
        

    except ValueError:
        print("You must enter a number. . .") #because. . duh
    else:
        print(f"{far} degrees Fahrenheit is equal to {cel} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")
        print("Go away now. . .")

#Call the main function
if __name__ == "__main__":
    main()