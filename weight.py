# Import Datetime
import datetime

# Import the LaunchDarkly client.
import ldclient
from ldclient import Context
from ldclient.config import Config

today = datetime.date.today()
this_year = today.year
lb_to_kg = 0.454
allowed_units = ('L','K','l','k')

# Replace "your key here" in my_sdk_key variable declaration with your actual LD SDK Key within quotes
# my_sdk_key = "your key here"

# Create a helper function for rendering messages.

def show_message(s):
    print("\n --- %s" % s)
    print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
    ldclient.set_config(Config(my_sdk_key))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
    show_message("SDK successfully initialized!")
else:
    show_message("SDK failed to initialize")
    exit()

# Have the user enter their name and their year of birth
NAME = input("Enter your name: ")
birth_year = input("Enter your year of birth: ")

user_key = hash(NAME) #used to generate user key for ld context

# Calculate the user's age for the current year
age = this_year - int(birth_year)

# Display the user's name and age
print("Hello ", NAME)
print("You will be ", age," this year")

# Set up the LD evaluation context.
if NAME.casefold() == "paul":
    context = Context.builder("demo-user-1").name(NAME).build()
else:
    context = Context.builder(str(user_key)).name(NAME).build()

# Call LaunchDarkly with the feature flag key to evaluate
flag_value = ldclient.get().variation("my-test", context, False)
# target_value = ldclient.get().variation("my-test", user, False)

show_message("Feature flag 'my-test' is %s for this user" % flag_value)

if flag_value == True:

# Get user input for weigh and units variable and check entries for proper input.
    while True:
        weight = input("Enter your weight: ")
        if weight.isdigit():
            break
        else:
            print("\n INVALID ENTRY: Please enter the numeric value of your weight \n")

    while True:
       units = input("Enter (K)g or (L)bs: ")
       if units not in allowed_units:
           print("\n INVALID ENTRY: Please enter l for Lbs or k for Kgs \n")
       else:
           break
    if units.casefold() == "l":
        print("Your weight in Kg is: ", float(weight) * lb_to_kg)
    elif units.casefold() == "k":
        print("Your weight in Lbs is: ", float(weight) / lb_to_kg)

    target_value = ldclient.get().variation("bmi_feature", context, False)

    show_message("Feature flag 'bmi_feature' is %s for this user \n" % target_value)

    if target_value == True:
    # Calculates BMI based on weight and units (kg or lbs).
        if units.casefold() == "k":
            # BMI formula for weight in kg and height in meters
            height = float(input("Enter your height in meters: "))
            bmi = float(weight) / (height ** 2)
            print("\n You Body Mass Index (BMI) is", bmi)
        elif units.casefold() == "l":
            # BMI formula for weight in lbs and height in inches
            height = float(input("Enter your height in inches: "))
            bmi = (float(weight) * 703) / (height ** 2)
            print("\n You Body Mass Index (BMI) is", bmi)

print("\n Have a great day!")

# Shut down the Launchdarkly SDK.
ldclient.get().close()








