weight = float(input("What is your weight? "))
unit = input(" Is your weight in k or l? ")
if unit == "L":
    converted = float (weight /0.45)
    print ( "Weight in Lbs:" + converted)
else:
    converted = float(weight * 0.45)
    print("Weight in Kgs is: " + str(converted))
