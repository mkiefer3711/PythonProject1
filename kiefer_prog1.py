#Input of weight in pounds
Weight=input("What is your weight in pounds? ")

#Input of height in inches
Height=input("What is your height in inches? ")

#Converting pounds to kilograms
Weight_KG=int(Weight)/2.2

#Converting inches to meters
Height_Meters=int(Height)*0.0254

#Squaring the calculation of height in meters and dividing the weight in kilograms by that value
BMI=Weight_KG/(Height_Meters*Height_Meters)

#Rounding the BMI value to 1 decimal place
BMI_Rounded=round(BMI, 1)

#Displaying the input of weight, input of height, and the calculation of the BMI rounded to 1 decimal place
print("At a weight of" , Weight , "pounds and a height of" , Height , "inches, your BMI is" , BMI_Rounded)