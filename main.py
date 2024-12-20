
# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    user_input = input('Enter an alphabet: ').lower()
    vowels = 'aeiou'
    if user_input in vowels and len(user_input) == 1:
        print(f'The letter {user_input} is a vowel')
    elif user_input.isalpha() and len(user_input) == 1:
        print(f'The letter {user_input} is a consonant')
    else:
        print(f'invalid input')

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    user_input = input('Please enter your age: ')
    voting_age = 21

    try:
        if int(user_input) < 0:
            print('Please enter a positive value')
        elif int(user_input) >= voting_age:
            print('Eligible to vote')
        elif int(user_input) < voting_age:
            print('Not eligible to vote')
        else: print('invalid input')

    except ValueError:
        print('Please enter a valid number')

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    user_input = input("Input a dog's age: ")
    try:
        dog_age = int(user_input)

        if dog_age < 0:
            print('Please enter a possible value')

        if dog_age <= 2:
            dog_years = dog_age * 10
        else: dog_years = ((int(user_input) - 2)*7) + 20

        print(dog_years)
    except ValueError:
        print('Please enter a valid number')


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold_input = input('Enter Yes or No to the following questions. Is it cold? ').lower()
    rain_input = input('Is it raining? ').lower()

    if cold_input == 'yes' and rain_input == 'yes':
        print('Wear a waterproof coat.')
    elif cold_input == 'yes' and rain_input == 'no':
        print ('Wear a warm coat.')
    elif cold_input == 'no' and rain_input == 'yes':
        print ('Carry an umbrella.')
    elif cold_input == 'no' and rain_input == 'no':
        print('Wear light clothing.')
    else: print('Invalid input')

# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month_input = input('Enter the month of the year (Jan - Dec): ').capitalize()
    day_input = input('Enter the day of the month: ')
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    try:
        date = int(day_input)
        if month_input not in months_list:
            print('Invalid input for month')
            return

        if date < 1 or date > 31:
            print('Invalid date')
            return

        if (month_input == 'Dec' and 21 <= date <= 31) or (month_input == 'Jan') or (month_input == 'Feb' and date <= 28) or (month_input == 'Mar' and date <= 19):
            print('Winter')
        elif (month_input == 'Mar' and 19 < date <= 31) or (month_input == 'Apr' or 'Jun') or (month_input == 'Jun' and date <= 20):
            print('Spring')
        elif (month_input == 'Jun' and 21 <= date <= 30) or (month_input == 'Jul' or 'Aug') or (month_input == 'Sep' and date <= 21):
            print('Summer')
        elif (month_input == 'Sep' and 22 <= date <= 30) or (month_input == 'Oct' or 'Nov') or (month_input == 'Dec' and date <= 20):
            print('Fall')
        else:
            print('Invalid date')

    except ValueError:
        print('Invalid values')


# Call the function
determine_season()

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    fixed_number = 42
    count = 1
    while count < 6:
        user_input = int(input("Guess a number from 1 - 100: "))
        if user_input == fixed_number:
            print("Congratulations, you guessed correctly!")
        elif count == 4:
            print("Last chance!")
        elif count == 5:
            print("Sorry, you failed to guess the number in five attempts.")
        elif fixed_number - 10 < user_input < fixed_number + 10:
            print("Guess is close")
        elif user_input > fixed_number + 10:
            print("Guess is too high")
        elif user_input < fixed_number - 10:
            print("Guess is too low")
        count += 1
# Call the function
guess_number()




