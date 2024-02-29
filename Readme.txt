Instructions for seting up weight demo with LaunchDarkly using Python and Pycharm IDE.

Note: You can choose to use the command line or a Python editor such as Python, the steps will be very close.

1- Sign up for LaunchDarkly evaluation at: https://launchdarkly.com/start-trial/ or use your LaunchDarkly account
2- Make sure you have python version 3.12.2 or higher install.
3- I used Pycharm 2023.3.3 Community Edition.
4- Set SDK dependencies:
	In a command prompt cd to the installation directory of the demo application.
	There should already be a file called requirements.txt	Type pip install -r requirements.txt in command prompt or terminal.

LaunchDarkly Configuration:
I implemented my demo with two LaunchDarkly feature flags. One flag, "my-test", is used to enable and dissable the weight and BMI calculation and display.  The second flag, "bmi_feature", targets user "Paul" to enable the BMI feature just for this user. You will need to configure your LaunchDarkly as follows before running the weight.py application:

1- Log into your LaunchDarkly account.
2- In LaunchDarkly go to Feature flags:
	1- Create a feature flag called "my-test" set to be true when turned on, targeting is off and serving false, and Fallback variation is Serving false
	
	2 - Create a feature flag called "bmi_feature" set  to be true on, targeting set to User: "Paul", True and Default rule serves false
	
3- Set Up wieght.py to used your SDK key.
		To set you sdk_key in weight.py: Uncomment line 15, # my_sdk_key = "your key here", and replace the text "your key here" with your Launchdarly SDK key in quotes. Your key will be of the format "sdk-########-####-####-####-############" 
		Save your changes.

Test your application:
	Click the green run button in Pycharm from the weight.py file in the editor
	From command line go to the sample application folder after you have replaced type: >python weight.py

Operation:
weight.py prompts the user for the name (first name) and the year of their birth. All users see this feature. If feature flag "my-test" is enabled/on then all users will be prompted for their weight and the units of measurement, Lbs or Kgs. weight.py will display the users weight in Kgs if the input was entered in Lbs and Lbs of Kgs was entered. When the bmi_feature flag is enable/on, only user "Paul" will be asked to enter his height in inches or kilograms and his BMI will be calculated based on the weight and units entired in the weight section of the application. Dissabling/turning off "my-test" disable weight and BMI collections for everyone. Dissabling/turning off bmi_feature only dissable BMI calculation for user "Paul".



